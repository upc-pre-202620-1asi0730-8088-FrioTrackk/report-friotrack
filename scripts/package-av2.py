from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import json
import subprocess

repo = Path(__file__).resolve().parents[1]
prefix = 'upc-pre-202620-1asi0730-8088-blackstartup-'
previous = repo / 'tmp/previous' / (prefix + 'artifacts-av2.zip')
output = repo / 'tmp' / (prefix + 'artifacts-av2.zip')
paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=repo).decode('utf-8').split('\0')
with ZipFile(previous) as source, ZipFile(output, 'w', ZIP_DEFLATED) as target:
    for entry in source.infolist():
        if entry.filename.split('/')[0] in ('friotrack-api', 'friotrack-frontend', 'friotrack-landing'):
            target.writestr(entry, source.read(entry.filename))
    for name in paths:
        if name and not name.startswith('.idea/'):
            target.write(repo / name, 'report-friotrack/' + name)
    pdf = repo / 'deliverables' / (prefix + 'report-av2.pdf')
    if str(pdf.relative_to(repo)).replace('\\', '/') not in paths:
        target.write(pdf, 'report-friotrack/deliverables/' + pdf.name)
assets = sorted((repo / 'deliverables').glob('*-av2.*'))
assets = [p for p in assets if p.suffix in ('.pdf', '.pptx', '.docx')]
assets.append(output)
manifest = {'version': 'v3.0.0', 'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo).decode().strip(), 'retainedProductSources': 'v3.0.0-av2.5', 'assets': [{'name': p.name, 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in assets]}
(repo / 'tmp/release-manifest-v3.0.0.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
print(output)
