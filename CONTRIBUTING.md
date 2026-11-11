# Contribution and report verification

Use commits that describe one coherent correction. Keep the author configured to the person doing the work. Preserve historical contribution records, acceptance records and release tags; never invent another member's activity or task acceptance.

Feature work normally starts in `feature/*`, integrates into `develop`, and publishes to `main` after validation. Use a pull request when an integration needs review or a protected branch requires it. A release identifies an exact reviewed commit and describes its scope and verification. Source releases do not establish an Azure deployment.

## Structural checks

```shell
python scripts/check-report.py
```

The check validates local references and anchors, complete story scenarios, standard backlog states and the documented review estimate range. It does not certify external links, team acceptance or live deployments.

## Rebuilding the cover and PDF

The retained DOCX template controls the cover. `python scripts/build-cover.py` changes only documented text slots and verifies the template hash and preserved package parts. Export the resulting cover to the adjacent `report-cover-tb1.pdf` with Word or a compatible document renderer and inspect its page against the reference. The build script does not establish visual validation on its own.

Full report export requires Pandoc, Node with Playwright/Chromium, and Python with pypdf and reportlab. `CHROME_PATH` may select an installed Chrome executable.

```shell
pandoc README.md -f gfm -t html5 --standalone --metadata title="FríoTrack Informe TB1" --css scripts/report.css -o report.html
node scripts/render-report.cjs
python scripts/assemble-report.py
```

The assembly adds the cover and page numbers to the body. Render the resulting PDF pages and inspect captions, tables, diagrams and complete figures before publishing it. Keep new review receipts separate from historical evidence.
