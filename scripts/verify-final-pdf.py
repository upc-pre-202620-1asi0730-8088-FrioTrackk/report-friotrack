from pathlib import Path
from pypdf import PdfReader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--pdf', type=Path)
args = parser.parse_args()
repo = Path(__file__).resolve().parents[1]
pdf = args.pdf or repo / 'deliverables/upc-pre-202620-1asi0730-8088-blackstartup-report-av2.pdf'
reader = PdfReader(pdf)
cover = reader.pages[0].extract_text() or ''
assert 'Informe de Trabajo Final' in cover
assert all(name in cover for name in ('Atauje Barreto', 'Daga Chávez', 'Saavedra Flores', 'Vera Solsol'))
assert 'Código' not in cover and 'Apellidos y Nombres' not in cover, 'PDF cover still contains the member table'
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
for required in ('H-01. Reporte', 'H-02. Confusión', 'H-03. Instrucciones', 'Carol Solsol', 'Anexo G.'):
    assert required in text, 'Missing final report content: ' + required
assert '<table align="center">' in (repo / 'README.md').read_text(encoding='utf-8'), 'Markdown cover must retain its table'
print(f'Final PDF verified: {len(reader.pages)} pages; cover and evaluation complete.')
