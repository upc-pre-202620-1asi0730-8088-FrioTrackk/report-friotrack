from pathlib import Path
from pypdf import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
import io,json
repo=Path(__file__).resolve().parents[1]
writer=PdfWriter();writer.append(str(repo/'deliverables/upc-pre-202620-1asi0730-8088-blackstartup-report-cover-tb1.pdf'));writer.append(str(repo/'tmp/report-body.pdf'))
writer.add_metadata({'/Title':'FríoTrack Informe del Trabajo Final TB1','/Author':'Alexander1Alexander2','/Subject':'Revisión documental de TB1 del 10 de noviembre de 2026'})
for n,page in enumerate(writer.pages[1:],2):
 data=io.BytesIO(); w=float(page.mediabox.width); h=float(page.mediabox.height)
 c=canvas.Canvas(data,pagesize=(w,h));c.setFont('Helvetica',8);c.setFillColorRGB(.4,.4,.4);c.drawCentredString(w/2,20,str(n));c.save();data.seek(0);page.merge_page(PdfReader(data).pages[0])
output=repo/'deliverables/upc-pre-202620-1asi0730-8088-blackstartup-report-tb1.pdf'
writer.write(output)
reader=PdfReader(output);sections={}
for n,p in enumerate(reader.pages,1):
 text=p.extract_text() or ''
 for label in ['Capítulo III: Requirements Specification','4.6. Domain-Driven Software Architecture','4.7. Software Object-Oriented Design','5.2.1. Sprint 1','5.2.2. Sprint 2','Revisión de repositorios y releases']:
  if label in text:sections.setdefault(label,[]).append(n)
(repo/'tmp/pdf-sections.json').write_text(json.dumps({'pages':len(reader.pages),'sections':sections},ensure_ascii=False,indent=2),encoding='utf-8')
print(output);print('pages',len(reader.pages));print(json.dumps(sections,ensure_ascii=True))
