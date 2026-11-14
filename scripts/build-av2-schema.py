"""Document the initial AV2 EF Core migration without connecting to a database."""
from pathlib import Path
from xml.etree import ElementTree as ET
from html import escape
import argparse
import hashlib
import json
import re

REPO = Path(__file__).resolve().parents[1]
CONTEXTS = {
    'Shipment Management': ['shipments', 'shipment_history'],
    'Monitoring and Telemetry': ['shipment_monitorings', 'sensor_readings', 'position_reports'],
    'Fleet and Resources': ['vehicles', 'drivers', 'sensors', 'fleet_allocations'],
    'Alert and Reporting': ['alerts', 'corrective_actions', 'notifications', 'incidents', 'thermal_reports'],
    'IAM': ['organizations', 'users', 'auth_sessions', 'password_reset_tokens'],
}
COLORS = ['#fff2cc', '#e1f0ff', '#e4f1df', '#fce4d6', '#ede3f4']


def parse_migration(path):
    raw = path.read_bytes().replace(b'\r\n', b'\n')
    text = raw.decode('utf-8-sig').split('protected override void Down', 1)[0]
    tables = []
    for block in text.split('migrationBuilder.CreateTable(')[1:]:
        name = re.search(r'name: "([^"]+)"', block)[1]
        fields = []
        for line in block.split('constraints:', 1)[0].splitlines():
            match = re.search(r'(\w+) = table.Column<[^>]+>\(type: "([^"]+)".*nullable: (true|false)', line)
            if match:
                fields.append({'name': match[1], 'type': match[2], 'nullable': match[3] == 'true'})
        primary = re.search(r'table.PrimaryKey\("[^"]+", x => x\.(\w+)\)', block)[1]
        foreign = []
        for fk in re.finditer(r'table.ForeignKey\(\s*name: "([^"]+)",\s*column: x => x\.(\w+),\s*principalTable: "([^"]+)",\s*principalColumn: "([^"]+)",\s*onDelete: ReferentialAction\.(\w+)\)', block):
            foreign.append({'name': fk[1], 'column': fk[2], 'parentTable': fk[3], 'parentColumn': fk[4], 'onDelete': fk[5]})
        checks = [{'name': m[1], 'expression': m[2].replace('\\"', '"')} for m in re.finditer(r'table.CheckConstraint\("([^"]+)", "((?:[^"\\]|\\.)*)"\)', block)]
        tables.append({'table': name, 'primaryKey': primary, 'fields': fields, 'foreignKeys': foreign, 'checks': checks, 'indexes': []})
    lookup = {t['table']: t for t in tables}
    for match in re.finditer(r'migrationBuilder.CreateIndex\(\s*name: "([^"]+)",\s*table: "([^"]+)",\s*(column: "([^"]+)"|columns: new\[\] \{ ([^}]+) \})(,\s*unique: true)?\)', text):
        columns = [match[4]] if match[4] else re.findall(r'"([^"]+)"', match[5])
        lookup[match[2]]['indexes'].append({'name': match[1], 'columns': columns, 'unique': bool(match[6])})
    assert set(lookup) == {t for ts in CONTEXTS.values() for t in ts}, 'Update the context map for a schema change.'
    for context, names in CONTEXTS.items():
        for name in names:
            lookup[name]['context'] = context
    return {'status': 'av2_ef_core_migration_source_not_cloud_deployment', 'migration': path.name, 'migrationSha256': hashlib.sha256(raw).hexdigest(), 'tables': [lookup[t] for names in CONTEXTS.values() for t in names]}


def abbreviated_type(value):
    return value.replace('character varying', 'varchar').replace('timestamp with time zone', 'timestamptz').replace('double precision', 'float8')


def marks(table, field):
    result = []
    if table['primaryKey'] == field['name']:
        result.append('PK')
    if any(f['column'] == field['name'] for f in table['foreignKeys']):
        result.append('FK')
    if any(i['unique'] and i['columns'] == [field['name']] for i in table['indexes']):
        result.append('UK')
    if field['nullable']:
        result.append('nullable')
    return ', '.join(result)


def svg_text(x, y, value, size=17, bold=False):
    return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="#233142">{escape(value)}</text>'


def mx_vertex(root, ident, value, x, y, width, height, style):
    cell = ET.SubElement(root, 'mxCell', id=ident, value=value, style=style, vertex='1', parent='1')
    ET.SubElement(cell, 'mxGeometry', x=str(x), y=str(y), width=str(width), height=str(height), **{'as': 'geometry'})


def diagram(context, tables, lookup, color, overview=False):
    # Relationship identifiers keep dense cross-context references readable in print.
    width = 2380 if overview else 2350
    card_width = 540 if overview else 650
    columns = 4 if overview else 2
    gap = 40 if overview else 65
    left = 40
    top = 145
    graph = ET.Element('mxGraphModel', grid='1', gridSize='20', page='0', pageWidth=str(width), pageHeight='1800', background='#ffffff')
    root = ET.SubElement(graph, 'root')
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')
    shapes = []
    positions = {}
    y = top
    row = []
    for index, table in enumerate(tables):
        fields = [f for f in table['fields'] if set(marks(table, f).split(', ')) & {'PK', 'FK', 'UK'}] if overview else table['fields']
        lines = [f"{f['name']}: {abbreviated_type(f['type'])}" + (f" [{marks(table,f)}]" if marks(table, f) else '') for f in fields]
        if overview:
            lines = [f"{f['name']} [{marks(table,f)}]" for f in fields]
        header = table['table']
        height = 66 + len(lines) * 25
        row.append((table, lines, height))
        if len(row) < columns and index != len(tables) - 1:
            continue
        max_height = max(t[2] for t in row)
        for col, (item, lines, height) in enumerate(row):
            x = left + col * (card_width + gap)
            current_color = COLORS[list(CONTEXTS).index(item['context'])] if overview else color
            shapes.extend([f'<rect x="{x}" y="{y}" width="{card_width}" height="{height}" fill="white" stroke="#81909f"/>', f'<rect x="{x}" y="{y}" width="{card_width}" height="38" fill="{current_color}" stroke="#81909f"/>', svg_text(x+14, y+26, item['table'], 21, True)])
            shapes.extend(svg_text(x+14, y+63+i*25, line, 17 if overview else 18) for i, line in enumerate(lines))
            if overview:
                shapes.append(svg_text(x+14, y+height-9, f"{len(item['fields'])} columns · {item['context']}", 14))
            text = '<b>' + escape(item['table']) + '</b><br><br>' + '<br>'.join(escape(line) for line in lines)
            mx_vertex(root, item['table'], text, x, y, card_width, height, f'rounded=0;whiteSpace=wrap;html=1;fillColor={current_color};strokeColor=#81909f;fontFamily=Arial;fontSize=18;align=left;verticalAlign=top;spacing=12;')
            positions[item['table']] = (x, y, card_width, height)
        y += max_height + 45
        row = []
    core_bottom = y
    if not overview:
        external_names = sorted({fk['parentTable'] for table in tables for fk in table['foreignKeys']} - {table['table'] for table in tables})
        external_y = top
        for name in external_names:
            external = lookup[name]
            x, ew, eh = 1535, 770, 102
            shapes.extend([f'<rect x="{x}" y="{external_y}" width="{ew}" height="{eh}" fill="#f4f5f6" stroke="#81909f" stroke-dasharray="5 3"/>', svg_text(x+14, external_y+28, name, 21, True), svg_text(x+14, external_y+56, 'External reference · '+external['context'], 17), svg_text(x+14, external_y+82, external['primaryKey']+': varchar(100) [PK]', 18)])
            mx_vertex(root, name, '<b>'+name+'</b><br>External reference · '+external['context']+'<br>'+external['primaryKey']+': varchar(100) [PK]', x, external_y, ew, eh, 'rounded=0;whiteSpace=wrap;html=1;fillColor=#f4f5f6;strokeColor=#81909f;dashed=1;fontFamily=Arial;fontSize=18;align=left;verticalAlign=top;spacing=12;')
            positions[name] = (x, external_y, ew, eh)
            external_y += eh + 45
        y = max(core_bottom, external_y)
    edge_shapes = []
    routes = {}
    core_names = {table['table'] for table in tables}
    edge_number = 0
    for i, table in enumerate(tables):
        for j, fk in enumerate(table['foreignKeys']):
            if fk['parentTable'] not in positions:
                continue
            ax, ay, aw, ah = positions[table['table']]
            bx, by, bw, bh = positions[fk['parentTable']]
            field_index = next(k for k, field in enumerate(table['fields']) if field['name'] == fk['column'])
            if not overview and fk['parentTable'] not in core_names:
                sx, sy, tx, ty = ax+aw, ay+58+field_index*25, bx, by+20
                lane = 112 + (edge_number % 5)*6
                before = ax+aw+20+(edge_number%3)*6
                after = 1450+(edge_number%5)*12
                route = [(sx,sy),(before,sy),(before,lane),(after,lane),(after,ty),(tx,ty)]
            elif ax != bx:
                if ax < bx:
                    sx, tx = ax+aw, bx
                else:
                    sx, tx = ax, bx+bw
                sy, ty = ay+58+field_index*25, by+58
                mid = (sx+tx)/2
                route = [(sx,sy),(mid,sy),(mid,ty),(tx,ty)]
            else:
                sx, tx = ax+aw*.88, bx+bw*.88
                sy, ty = (ay, by+bh) if ay > by else (ay+ah, by)
                mid = (sy+ty)/2
                route = [(sx,sy),(sx,mid),(tx,mid),(tx,ty)]
            routes[(table['table'],fk['name'])] = route
            points = ' '.join(f'{x},{y}' for x,y in route)
            if not overview:
                edge_shapes.append(f'<polyline points="{points}" fill="none" stroke="#526577" stroke-width="1.8" marker-end="url(#arrow)"/>')
            edge_number += 1
    shapes = edge_shapes + shapes
    y += 15
    shapes.append(svg_text(left, y, 'RELATIONSHIPS · child FK → parent PK · parent cardinality / child cardinality', 20, True))
    mx_vertex(root, 'relations-title', 'RELATIONSHIPS · child FK → parent PK · parent / child cardinality', left, y-25, width-80, 35, 'text;html=1;align=left;fontSize=20;fontStyle=1;')
    y += 34
    relations = []
    for table in tables:
        for fk in table['foreignKeys']:
            field = next(f for f in table['fields'] if f['name'] == fk['column'])
            unique = any(i['unique'] and i['columns'] == [fk['column']] for i in table['indexes'])
            parent_cardinality = '0..1' if field['nullable'] else '1'
            child_cardinality = '0..1' if unique else '0..*'
            relations.append((table, fk, parent_cardinality, child_cardinality))
    relation_columns = 2 if overview else 1
    rel_width = (width - 100) / relation_columns
    rows_per_column = (len(relations) + relation_columns - 1) // relation_columns
    for i, (table, fk, parent_cardinality, child_cardinality) in enumerate(relations):
        col, row = divmod(i, rows_per_column)
        label = f"{i+1:02d}  {table['table']}.{fk['column']} → {fk['parentTable']}.{fk['parentColumn']}  ({parent_cardinality} / {child_cardinality})"
        x, ry = left + col * rel_width, y + row * 29
        shapes.append(svg_text(x, ry, label, 16 if overview else 18))
        mx_vertex(root, f'relation-{i}', label, x, ry-20, rel_width-10, 28, 'text;html=1;align=left;fontSize=17;')
        if fk['parentTable'] in positions:
            start_arrow = 'ERzeroToOne' if child_cardinality == '0..1' else 'ERmany'
            end_arrow = 'ERzeroToOne' if parent_cardinality == '0..1' else 'ERone'
            edge = ET.SubElement(root, 'mxCell', id=f'edge-{i}', value=fk['column'], style=f'edgeStyle=orthogonalEdgeStyle;endArrow={end_arrow};startArrow={start_arrow};strokeColor=#526577;fontSize=13;', edge='1', parent='1', source=table['table'], target=fk['parentTable'])
            geometry = ET.SubElement(edge, 'mxGeometry', relative='1', **{'as':'geometry'})
            waypoints = ET.SubElement(geometry, 'Array', **{'as':'points'})
            for px, py in routes[(table['table'],fk['name'])][1:-1]:
                ET.SubElement(waypoints, 'mxPoint', x=str(px), y=str(py))
    y += rows_per_column * 29 + 25
    subtitle = 'EF Core 10 / PostgreSQL 17 · source migration; cloud publication is recorded separately.'
    shapes.insert(0, svg_text(left, 86, subtitle, 19))
    shapes.insert(0, svg_text(left, 45, 'FríoTrack · AV2 · ' + context, 29, True))
    mx_vertex(root, 'title', 'FríoTrack · AV2 · ' + context, left, 10, width-80, 50, 'text;html=1;align=left;fontSize=29;fontStyle=1;')
    mx_vertex(root, 'subtitle', subtitle, left, 65, width-80, 35, 'text;html=1;align=left;fontSize=19;')
    footer = 'PK primary · FK foreign · UK unique · nullable optional · entity IDs varchar(100) · overview omits non-key columns'
    shapes.append(svg_text(left, y, footer, 17))
    mx_vertex(root, 'legend', footer, left, y-20, width-80, 35, 'text;html=1;align=left;fontSize=17;')
    height = y + 40
    graph.set('pageHeight', str(height))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><defs><marker id="arrow" viewBox="0 0 12 10" refX="11" refY="5" markerWidth="9" markerHeight="8" orient="auto"><path d="M0 0 L12 5 L0 10" fill="none" stroke="#526577"/></marker></defs><rect width="100%" height="100%" fill="white"/>' + ''.join(shapes) + '</svg>'
    return svg, graph


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--migration', type=Path, default=REPO.parent/'friotrack-api/Shared/Infrastructure/Migrations/20261113144845_InitialAv2Relational.cs')
    args = parser.parse_args()
    model = parse_migration(args.migration)
    out = REPO/'assets/architecture/av2'
    out.mkdir(parents=True, exist_ok=True)
    (out/'schema.json').write_text(json.dumps(model, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    lookup = {t['table']: t for t in model['tables']}
    pages = ET.Element('mxfile', host='app.diagrams.net', version='24.7.17')
    views = [('00-erd-overview', 'Relational schema overview', model['tables'], '#ffffff', True)]
    for i, (context, names) in enumerate(CONTEXTS.items(), 1):
        views.append((f'{i:02d}-erd-'+['shipment','monitoring','fleet','alerts-reporting','iam'][i-1], context, [lookup[n] for n in names], COLORS[i-1], False))
    manifest = []
    for ident, title, tables, color, overview in views:
        svg, graph = diagram(title, tables, lookup, color, overview)
        (out/(ident+'.svg')).write_text(svg, encoding='utf-8', newline='\n')
        page = ET.SubElement(pages, 'diagram', id=ident, name=title)
        page.append(graph)
        single = ET.Element('mxfile', host='app.diagrams.net')
        single_page = ET.SubElement(single, 'diagram', id=ident, name=title)
        single_page.append(ET.fromstring(ET.tostring(graph)))
        ET.ElementTree(single).write(out/(ident+'.drawio'), encoding='utf-8', xml_declaration=True)
        manifest.append({'id':ident, 'title':title, 'svg':ident+'.svg', 'drawio':ident+'.drawio', 'sha256':hashlib.sha256(svg.encode('utf-8')).hexdigest()})
    ET.ElementTree(pages).write(out/'FrioTrack-AV2-Database.drawio', encoding='utf-8', xml_declaration=True)
    (out/'schema-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    doc = ['# Esquema relacional AV2', '', 'Este catálogo se deriva de la migración EF Core del repositorio canónico `friotrack-api`; identifica las fuentes y no acredita por sí solo despliegue cloud ni aceptación del sprint.', '', f"Migración: `{model['migration']}`. SHA-256: `{model['migrationSha256']}`.", '', f"**{len(model['tables'])} tablas y {sum(len(t['foreignKeys']) for t in model['tables'])} claves foráneas.** La tabla interna `__EFMigrationsHistory` registra EF Core y no es una entidad de negocio.", '', '[Documento editable de seis páginas](FrioTrack-AV2-Database.drawio). Descargar y abrir en Archivo → Abrir de [diagrams.net](https://app.diagrams.net/). Las tablas y conectores son formas nativas; las relaciones se muestran como catálogo FK → PK para facilitar la lectura impresa.', '', '| Vista | Imagen | Editable |', '| --- | --- | --- |']
    doc.extend(f"| {v['title']} | [SVG]({v['svg']}) | [drawio]({v['drawio']}) |" for v in manifest)
    doc += ['', '## Diferencias respecto al diseño TB1', '', '- `auth_sessions` añade sesiones revocables persistentes. La clave primaria es el hash del token, no el token emitido.', '- Los identificadores de entidad usan `varchar(100)`, compatibles con el contrato histórico. Los tipos de cada referencia constan en el catálogo; `thermal_reports.generated_by` usa `varchar(2000)`. No se convierten los identificadores históricos a UUID.', '- El campo `version` del envío es un token de concurrencia. La reserva opera en una transacción y utiliza un bloqueo asesor por organización; las FK no impiden por sí solas el solapamiento.', '- `thermal_reports.snapshot` utiliza `jsonb`: es la copia autorizada e inmutable del reporte al solicitarlo, no el almacén general de operaciones. La descarga implementada es JSON, además del CSV del frontend.', '- Los roles y estados tienen restricciones CHECK. El aislamiento por empresa y por cliente se aplica también en el servicio de aplicación; una FK no sustituye autorización.', '- La presencia de `password_reset_tokens` permite conservar el modelo previsto. No demuestra envío de correo ni un flujo de recuperación operativo.', '- Las lecturas son de demostración y las evaluaciones de pérdida de señal se solicitan expresamente. No se afirma ingesta física ni evaluación automática en segundo plano.', '', '## Catálogo de columnas', '']
    for context, names in CONTEXTS.items():
        doc += [f'### {context}', '']
        for name in names:
            table = lookup[name]
            doc += [f'#### `{name}`', '', '| Columna | Tipo PostgreSQL | Restricciones |', '| --- | --- | --- |']
            doc.extend(f"| `{f['name']}` | `{f['type']}` | {marks(table,f) or 'NOT NULL'} |" for f in table['fields'])
            doc += ['']
            for check in table['checks']:
                doc.append(f"- CHECK `{check['name']}`: `{check['expression']}`.")
            for index in table['indexes']:
                doc.append(f"- {'UNIQUE' if index['unique'] else 'INDEX'} `{index['name']}`: `{'`, `'.join(index['columns'])}`.")
            doc += ['']
    doc += ['## Referencias de integridad', '', '| Hija | FK | Padre | PK | Eliminación |', '| --- | --- | --- | --- | --- |']
    doc.extend(f"| `{t['table']}` | `{f['column']}` | `{f['parentTable']}` | `{f['parentColumn']}` | {f['onDelete']} |" for t in model['tables'] for f in t['foreignKeys'])
    doc += ['', '## Reproducción', '', 'Con ambos repositorios en directorios hermanos, ejecutar `python scripts/build-av2-schema.py`. Puede indicarse otra ruta con `--migration`. El script solo lee la migración y escribe documentación; no inicia servicios, crea bases de datos ni accede a credenciales.', '']
    (out/'README.md').write_text('\n'.join(doc), encoding='utf-8', newline='\n')
    print(json.dumps({'tables':len(model['tables']), 'foreignKeys':sum(len(t['foreignKeys']) for t in model['tables']), 'views':len(views), 'migrationSha256':model['migrationSha256']}))


if __name__ == '__main__':
    main()
