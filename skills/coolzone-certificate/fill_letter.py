#!/usr/bin/env python3
"""Fill the Coolzone Declaration Letter template.

Usage:
  python3 fill_letter.py <template.docx> <content.json> <output.docx>

content.json:
{
  "date": "30/10/2026",
  "to": "Megah Constructions",
  "address": "15 Walkers Rd, Nunawading VIC, Australia",
  "ref": "JB13647",
  "body": [
    "We hereby certify that ...",
    "- AS1668.2-2012 ...",          # leading "- " = indented item
    "Should you have any questions ..."
  ],
  "signer": "Lawrence J.J. Lao",     # optional, default keeps template
  "sign_date": "30/10/2026"           # optional, Date: line under signature; default = date
}

Only the letter text is replaced; the letterhead (header), footer, fonts and
spacing all come from the template. A blank line is put between body paragraphs.
"""
import json, re, shutil, sys, tempfile, zipfile, os
from xml.sax.saxutils import escape


def set_text(p, text):
    """Replace all text in paragraph p with text, keeping the first run's format."""
    runs = re.findall(r'<w:r>.*?</w:r>', p, re.S)
    if not runs:
        raise SystemExit('paragraph has no run')
    first = runs[0]
    rpr = re.search(r'<w:rPr>.*?</w:rPr>', first, re.S)
    rpr = rpr.group(0) if rpr else ''
    new_run = f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    start = p.index(runs[0])
    end = p.rindex(runs[-1]) + len(runs[-1])
    return p[:start] + new_run + p[end:]


def indent(p, left=567, hanging=283):
    ind = f'<w:ind w:left="{left}" w:hanging="{hanging}"/>'
    return p.replace('<w:jc w:val="start"/>', ind + '<w:jc w:val="start"/>', 1)


def main(tpl, js, out):
    c = json.load(open(js, encoding='utf-8'))
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(tpl) as z:
        z.extractall(tmp)
    path = os.path.join(tmp, 'word', 'document.xml')
    x = open(path, encoding='utf-8').read()
    bstart = x.index('<w:body>') + len('<w:body>')
    sect = x.index('<w:sectPr', bstart)
    body = x[bstart:sect]
    ps = re.findall(r'<w:p>.*?</w:p>', body, re.S)
    txt = [re.sub(r'<[^>]+>', '', p) for p in ps]

    def find(pred, name):
        for i, t in enumerate(txt):
            if pred(t):
                return i
        raise SystemExit(f'template paragraph not found: {name}')

    i_date = 0
    i_to = find(lambda t: t.startswith('To:'), 'To:')
    i_addr = find(lambda t: t.startswith('Project Address:'), 'Project Address:')
    i_ref = find(lambda t: t.startswith('Ref Number:'), 'Ref Number:')
    i_body = find(lambda t: t.startswith('We hereby certify'), 'body')
    i_sign = find(lambda t: t.strip() == 'Lawrence J.J. Lao', 'signer')
    blank = ps[i_body - 1]  # empty paragraph with body spacing

    ps[i_date] = set_text(ps[i_date], c['date'])
    ps[i_to] = set_text(ps[i_to], 'To: ' + c['to'])
    ps[i_addr] = set_text(ps[i_addr], 'Project Address: ' + c['address'])
    ps[i_ref] = set_text(ps[i_ref], 'Ref Number: ' + c['ref'])
    if c.get('signer'):
        ps[i_sign] = set_text(ps[i_sign], c['signer'])
    # Rev 3+: "Date:" line under the signature gets the same date as the top
    for i in range(i_sign + 1, len(ps)):
        if txt[i].startswith('Date:'):
            ps[i] = set_text(ps[i], 'Date: ' + c.get('sign_date', c['date']))
            break

    tmpl = ps[i_body]
    new = []
    for k, para in enumerate(c['body']):
        if k:
            prev_item = c['body'][k - 1].startswith('- ')
            if not (prev_item and para.startswith('- ')):
                new.append(blank)
        if para.startswith('- '):
            new.append(indent(set_text(tmpl, '•\t' + para[2:])))
        else:
            new.append(set_text(tmpl, para))
    ps[i_body:i_body + 1] = new

    # rebuild body keeping anything between paragraphs (none in this template)
    x = x[:bstart] + ''.join(ps) + x[sect:]
    open(path, 'w', encoding='utf-8').write(x)
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                full = os.path.join(root, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)
    print('written', out)


if __name__ == '__main__':
    main(*sys.argv[1:4])
