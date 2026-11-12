from pathlib import Path
from urllib.parse import unquote
import re,json,csv,html,collections,hashlib
import xml.etree.ElementTree as ET

repo=Path(__file__).resolve().parents[1]
text=(repo/'README.md').read_text(encoding='utf-8-sig')
def line(s): return text[:text.index(s)].count('\n')+1
def slug(s):
    s=html.unescape(s).lower()
    s=re.sub(r'<[^>]+>','',s)
    return re.sub(r'[^\w\- ]','',s,flags=re.UNICODE).replace(' ','-')
anchors=set(); counts=collections.Counter()
for heading in re.findall(r'^#{1,6} (.+)$',text,re.M):
    anchor=slug(heading); n=counts[anchor]; counts[anchor]+=1
    anchors.add(anchor+(f'-{n}' if n else ''))
anchors.update(re.findall(r'(?:id|name)=["\']([^"\']+)',text))
broken=[]; local=0
links=re.findall(r'!?\[[^\]]*\]\(([^\s]+?)(?:\s+"[^"]*")?\)',text)
links+=re.findall(r'(?:src|href)=["\']([^"\']+)',text)
pending=()
for raw in links:
    link=html.unescape(raw.strip('<>'))
    if re.match(r'^[a-zA-Z]+:',link):continue
    local+=1
    path,_,anchor=link.partition('#')
    if path and not (repo/unquote(path)).exists():
        if not any(p in path for p in pending): broken.append((raw,'missing local file'))
    elif not path and anchor and unquote(anchor) not in anchors: broken.append((raw,'missing README anchor'))

ch3=text[text.index('# Capítulo III:'):text.index('# Capítulo IV:')]
stories=ch3[ch3.index('## 3.1.'):ch3.index('## 3.2.')]
storyrows=[x for x in stories.splitlines() if re.match(r'\| \*\*(US|TS)\d+',x)]
gherkin=[]
for row in storyrows:
    ident=re.search(r'\*\*((?:US|TS)\d+)\*\*',row)[1]
    scenes=re.split(r'\*\*Escenario \d+:\*\*',row)[1:]
    if len(scenes)<2 or any(not all(word in s.lower() for word in ('dado','cuando','entonces')) for s in scenes): gherkin.append(ident)
sprints={}
for n in (1,2):
    rows=list(csv.DictReader((repo/f'assets/annexes/sprint{n}-backlog.csv').open(encoding='utf-8-sig',newline='')))
    sprints[str(n)]={'tasks':len(rows),'hours':sum(int(x['Estimation (Hours)']) for x in rows),'invalidHours':[x['Task Id'] for x in rows if not 4<=int(x['Estimation (Hours)'])<=8],'invalidStatus':[x['Task Id'] for x in rows if x['Status'] not in ['To Do','In Process','To Review','Done']],'status':dict(collections.Counter(x['Status'] for x in rows))}
results={'localLinksChecked':local,'brokenLinks':broken,'stories':len(storyrows),'scenarioMarkers':len(re.findall(r'\*\*Escenario \d+:\*\*',stories)),'incompleteGherkin':gherkin,'storyIds':[re.search(r'\*\*((?:US|TS)\d+)\*\*',x)[1] for x in storyrows],'sprints':sprints,'boundedContextHeadings':re.findall(r'^#### BC.+$',text,re.M)}

assert not broken, broken
assert len(storyrows)==43 and results['scenarioMarkers']==86 and not gherkin, 'Incomplete story scenarios'
assert all(not s['invalidHours'] and not s['invalidStatus'] for s in sprints.values()), 'Invalid backlog values'
assert 'IAM' in results['boundedContextHeadings'][-1], 'Generic context must follow operational contexts'
for phrase in ['Our focus is on','We believe it delivers','This will be confirmed when']:
    assert text.count(phrase)>=2, 'Missing Sprint Goal template clause: '+phrase
architecture=repo/'assets/architecture/chapter-04'
manifest=json.loads((architecture/'manifest.json').read_text(encoding='utf-8-sig'))
assert len(manifest)==22 and len({d['id'] for d in manifest})==22, 'Expected22distinctarchitectureviews'
for entry in manifest:
    for kind in ('svg','png'):
        asset=(architecture/entry[kind]).resolve()
        assert asset.is_relative_to(repo.resolve()) and asset.is_file(), 'Missing architecture image: '+entry['id']
        assert hashlib.sha256(asset.read_bytes()).hexdigest()==entry['sha256'][kind], 'Architecture image differs from manifest: '+entry['id']
    diagram=ET.parse(architecture/entry['drawio']).getroot()
    assert diagram.tag=='mxfile' and len(diagram.findall('diagram'))==1, 'Invalid native editable: '+entry['id']
    assert (architecture/'fuentes'/f"{entry['id']}.json").is_file(), 'Missing model source: '+entry['id']
    assert '/revision-2026-11-11/'+entry['id']+'.png' in text, 'Architecture view missing from report: '+entry['id']
results['architectureViews']=len(manifest)
for n in (1,2):
    planning=text.split(f'#### 5.2.{n}.{1}. Sprint Planning {n}',1)[1].split(f'#### 5.2.{n}.2.',1)[0]
    assert all(f'| {field} |' in planning for field in ('Date','Time','Location')), 'Separate planning date/time/location required'
print(json.dumps(results,ensure_ascii=True,indent=2))
