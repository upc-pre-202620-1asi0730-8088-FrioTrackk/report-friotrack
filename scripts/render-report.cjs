const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
(async()=>{
 const repo=path.resolve(__dirname,'..');
 fs.mkdirSync(path.join(repo,'tmp'),{recursive:true});
 const browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
 const page=await browser.newPage({viewport:{width:1100,height:900}});
 await page.goto(pathToFileURL(path.join(repo,'report.html')).href,{waitUntil:'networkidle'});
 const stats=await page.evaluate(async()=>{
  await Promise.all([...document.images].map(i=>i.decode().catch(()=>null)));
  // Keep the published Markdown PNGs, and use vector originals for PDF zoom.
  for(const img of [...document.images]) {
   if(!['/revision-2026-11-11/','/architecture/av2/'].some(folder=>img.getAttribute('src').includes(folder)))continue;
   img.src=img.getAttribute('src').replace(/\.png$/,'.svg');
   await img.decode();
   const figure=document.createElement('figure');figure.className='architecture-figure';
   const parent=img.parentElement;
   const preceding=parent.previousElementSibling;
   const intro=[];
   if(preceding?.matches('h3,h4'))intro.unshift(preceding);
   else if(preceding?.matches('p')){
    const heading=preceding.previousElementSibling;
    if(heading?.matches('h3,h4'))intro.push(heading,preceding);
    else if(preceding.children.length===1&&preceding.firstElementChild?.matches('strong'))intro.push(preceding);
    else if(preceding.querySelector('strong')&&preceding.textContent.startsWith('Detalle de'))intro.push(preceding);
   }
   const following=parent.nextElementSibling;
   parent.before(figure);
   for(const node of intro)figure.append(node);
   figure.append(img);
   const caption=document.createElement('figcaption');caption.textContent=img.alt;figure.append(caption);
   if(following?.matches('p')&&!following.querySelector('img')&&following.textContent.length<1100&&!(following.children.length===1&&following.firstElementChild?.matches('strong'))&&!following.textContent.startsWith('Detalle de'))figure.append(following);
   if(!parent.textContent.trim()&&!parent.children.length)parent.remove();
  }
  const broken=[...document.images].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src'));
  for(const img of [...document.images].filter(i=>i.getAttribute('src').includes('/chapter-05/av2/'))) {
   if(img.closest('table'))continue;
   const parent=img.parentElement;
   const figure=document.createElement('figure');figure.className=img.alt.startsWith('Evidencia H-')?'heuristic-evidence':'execution-figure';
   parent.before(figure);figure.append(img);
   const caption=document.createElement('figcaption');caption.textContent=img.alt;figure.append(caption);
   if(!parent.textContent.trim()&&!parent.children.length)parent.remove();
  }
  for(const t of document.querySelectorAll('table')){
   const title=t.querySelector('thead')?.innerText||'';
   if(title.includes('Task Id') && title.includes('Task Description')) {
    t.classList.add('backlog');
    t.classList.add(t.querySelectorAll('thead th').length===8?'backlog-eight':'backlog-nine');
   }
   if(title.includes('Criterios de Aceptación'))t.classList.add('stories');
  }
  for(const t of document.querySelectorAll('table.backlog')) {
   let first=t.previousElementSibling;
   while(first && !/^H[1-6]$/.test(first.tagName)) first=first.previousElementSibling;
   if(first && first.textContent.includes('Sprint Backlog')) {
    const wrapper=document.createElement('section');wrapper.className='backlog-section';first.before(wrapper);
    let node=first;while(node){const next=node.nextElementSibling;wrapper.append(node);if(node===t)break;node=next;}
   }
  }
  for(const first of [...document.querySelectorAll('div[align="center"]')]) {
   const img=first.querySelector('img');const next=first.nextElementSibling;
   if(img && /\/(user-persona|user-persona-segmento2)\.jpg$/.test(img.getAttribute('src')) && next?.querySelector('img')){
    const wrap=document.createElement('div');wrap.className='persona-composite';first.before(wrap);wrap.append(first,next);
   }
  }
  for(const caption of [...document.querySelectorAll('p')]) {
   if(!/^(?:(Figura|Tabla)\s+\d|Panel de)/.test(caption.textContent.trim()))continue;
   caption.classList.add('figure-caption');
   let next=caption.nextElementSibling;
   for(let i=0;i<3 && next;i++,next=next.nextElementSibling){
    if(next.matches('p') && !next.querySelector('img'))next.classList.add('figure-caption');
    else break;
   }
  }
  const registry=document.getElementById('registro-de-versiones-del-informe');
  if(registry){const cover=document.createElement('section');cover.className='markdown-cover';document.body.prepend(cover);let node=cover.nextElementSibling;while(node&&node!==registry){const next=node.nextElementSibling;cover.append(node);node=next;}}
  const memberTable=document.querySelector('.markdown-cover table');
  if(memberTable){
   const members=document.createElement('div');members.className='cover-members';
   for(const row of memberTable.querySelectorAll('tr')){
    const cells=row.querySelectorAll('td');if(cells.length!==2)continue;
    const line=document.createElement('p');
    line.textContent=cells[1].textContent.trim()+' ('+cells[0].textContent.trim()+')';
    members.append(line);
   }
   memberTable.replaceWith(members);
  }
  for(const heading of [...document.querySelectorAll('h4')].filter(h=>/^H-0[123]\./.test(h.textContent))){
   const section=document.createElement('section');section.className='heuristic-finding';heading.before(section);
   let node=heading;
   while(node){const next=node.nextElementSibling;section.append(node);if(!next||/^H[1-4]$/.test(next.tagName))break;node=next;}
  }
  const summary=[...document.querySelectorAll('h4')].find(h=>h.textContent==='Resumen de hallazgos');
  if(summary&&summary.nextElementSibling?.matches('table')){
   const table=summary.nextElementSibling,group=document.createElement('section');group.className='keep-together';summary.before(group);group.append(summary,table);
  }
  for(const heading of [...document.querySelectorAll('h2')].filter(h=>/^5\.[45]\. Video/.test(h.textContent))){
   const group=document.createElement('section');group.className='keep-together';heading.before(group);
   let node=heading;while(node){const next=node.nextElementSibling;group.append(node);if(!next||/^H[12]$/.test(next.tagName))break;node=next;}
  }
  // PDF references must remain usable after downloading the report.
  const publicRepo='https://github.com/upc-pre-202620-1asi0730-8088-FrioTrackk/report-friotrack/';
  for(const link of document.querySelectorAll('a[href]')){
   const target=link.getAttribute('href');
   if(!target||target.startsWith('#')||/^[a-z][a-z0-9+.-]*:/i.test(target))continue;
   link.href=publicRepo+'blob/v3.0.0/'+target.replace(/^\.\//,'');
  }
  return {broken,images:document.images.length,tables:document.querySelectorAll('table').length};
 });
 if(stats.broken.length) throw new Error('Broken images: '+JSON.stringify(stats.broken));
 await page.pdf({path:path.join(repo,'tmp/report-body.pdf'),printBackground:true,preferCSSPageSize:true,tagged:true,outline:true});
 fs.writeFileSync(path.join(repo,'tmp/report-render.json'),JSON.stringify(stats,null,2));
 console.log(JSON.stringify(stats)); await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
