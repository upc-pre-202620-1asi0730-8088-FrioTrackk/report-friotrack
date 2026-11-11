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
  const broken=[...document.images].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src'));
  for(const t of document.querySelectorAll('table')){
   const title=t.querySelector('thead')?.innerText||'';
   if(title.includes('Evidence / Review Notes')) t.classList.add('backlog');
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
  const cover=document.querySelector('.report-cover'); if(cover){const next=cover.nextElementSibling;if(next?.getAttribute('style')?.includes('page-break'))next.remove();cover.remove();}
  return {broken,images:document.images.length,tables:document.querySelectorAll('table').length};
 });
 if(stats.broken.length) throw new Error('Broken images: '+JSON.stringify(stats.broken));
 await page.pdf({path:path.join(repo,'tmp/report-body.pdf'),printBackground:true,preferCSSPageSize:true,tagged:true,outline:true});
 fs.writeFileSync(path.join(repo,'tmp/report-render.json'),JSON.stringify(stats,null,2));
 console.log(JSON.stringify(stats)); await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
