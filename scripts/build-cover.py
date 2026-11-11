"""Build the TB1 cover by replacing text in the retained UPC template."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree
import hashlib
import html
import json
import re


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "assets/templates/upc-report-cover-reference.docx"
OUTPUT = ROOT / "deliverables/upc-pre-202620-1asi0730-8088-blackstartup-report-cover-tb1.docx"
RECEIPT = ROOT / "assets/evidence/cover-fidelity.json"
REFERENCE_SHA256 = "c56b8590d5a9cac1e8a9980c8865aa210b1a6247d61fd15939d12cc3a3819f50"

# Paragraph positions include table-cell paragraphs in document order.
REPLACEMENTS = {
    7: "8088",
    10: "Bautista Ubillús, Efraín Ricardo",
    15: "FríoTrack",
    20: "u20241f246", 21: "Atauje Barreto, Alexander Sebastián",
    22: "u202421137", 23: "Bardales Rodriguez, Benjamin Elias (retirado)",
    24: "u202219829", 25: "Daga Chávez, Joaquín Leonardo",
    26: "u20241D811", 27: "Saavedra Flores, Rodrigo Andree",
    28: "u20231H17", 29: "Vera Solsol, Nayely Macarena",
    30: "", 31: "", 35: "Octubre 2026",
}
TEXT_PATTERN = re.compile(r"(<w:t(?:\s[^>]*)?>)(.*?)(</w:t>)", re.S)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert sha256(REFERENCE.read_bytes()) == REFERENCE_SHA256, "Reference changed"
    with ZipFile(REFERENCE) as source:
        original = source.read("word/document.xml").decode("utf-8")
        paragraphs = list(re.finditer(r"<w:p(?:\s[^>]*)?>.*?</w:p>", original, re.S))
        assert len(paragraphs) == 36, "Unexpected template paragraph inventory"
        patched = original
        for index in sorted(REPLACEMENTS, reverse=True):
            paragraph = paragraphs[index]
            nodes = 0

            def replace(match):
                nonlocal nodes
                nodes += 1
                value = html.escape(REPLACEMENTS[index], quote=False) if nodes == 1 else ""
                return match[1] + value + match[3]

            value = TEXT_PATTERN.sub(replace, paragraph[0])
            assert nodes, f"No text slot in paragraph {index}"
            patched = patched[:paragraph.start()] + value + patched[paragraph.end():]
        ElementTree.fromstring(patched)
        without_text = lambda value: TEXT_PATTERN.sub(lambda m: m[1] + m[3], value)
        assert without_text(original) == without_text(patched), "Non-text structure changed"
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(OUTPUT, "w") as target:
            for entry in source.infolist():
                target.writestr(entry, patched.encode("utf-8") if entry.filename == "word/document.xml" else source.read(entry))

    with ZipFile(REFERENCE) as source, ZipFile(OUTPUT) as target:
        changed = [name for name in source.namelist() if source.read(name) != target.read(name)]
        assert changed == ["word/document.xml"]
        preserved = len(source.namelist()) - len(changed)

    receipt = {
        "reference": REFERENCE.relative_to(ROOT).as_posix(),
        "reference_sha256": REFERENCE_SHA256,
        "output": OUTPUT.relative_to(ROOT).as_posix(),
        "output_sha256": sha256(OUTPUT.read_bytes()),
        "changed_parts": changed,
        "preserved_parts_byte_identical": preserved,
        "non_text_document_structure_identical": True,
        "editable_slots": {str(k): v for k, v in REPLACEMENTS.items()},
        "visual_validation": "Export and compare reference and final in Word before publishing the PDF preview.",
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT).as_posix()}; preserved {preserved} package parts.")


if __name__ == "__main__":
    main()
