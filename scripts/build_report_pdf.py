import re
import os
import subprocess
import html
import base64

ROOT_DIR = r"d:\Data Science\Rakamin"
MD_FILE = os.path.join(ROOT_DIR, "MONOZUKURI_SUBMISSION_REPORT.md")
HTML_FILE = os.path.join(ROOT_DIR, "MONOZUKURI_SUBMISSION_REPORT_TMP.html")
PDF_FILE = os.path.join(ROOT_DIR, "MONOZUKURI_SUBMISSION_REPORT.pdf")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with open(MD_FILE, "r", encoding="utf-8") as f:
    md_content = f.read()

# Helper to encode images to base64
def image_replacer(match):
    alt = match.group(1)
    src = match.group(2)
    full_path = os.path.normpath(os.path.join(ROOT_DIR, src))
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_f:
            encoded = base64.b64encode(img_f.read()).decode("utf-8")
        ext = os.path.splitext(full_path)[1].lower().replace(".", "")
        mime = "image/png" if ext == "png" else "image/jpeg"
        return f'<div class="screenshot-box"><img src="data:{mime};base64,{encoded}" alt="{alt}" class="screenshot-img" /></div>'
    return f'<p class="error">[Image not found: {src}]</p>'

# Simple Markdown to HTML Parser
lines = md_content.split("\n")
html_parts = []
in_code = False
in_table = False
table_rows = []
in_list = False
list_type = "ul"

for line in lines:
    stripped = line.strip()
    
    # Code block
    if stripped.startswith("```"):
        if in_code:
            in_code = False
            html_parts.append("</pre>")
            continue
        else:
            in_code = True
            lang = stripped[3:].strip()
            html_parts.append(f'<pre class="code-block {lang}">')
            continue
            
    if in_code:
        html_parts.append(html.escape(line))
        continue

    # Close table if moving away from table row
    if in_table and not stripped.startswith("|"):
        in_table = False
        html_parts.append("</tbody></table>")

    # Close list if moving away from list
    if in_list and not (stripped.startswith("- ") or stripped.startswith("* ") or re.match(r"^\d+\.\s", stripped)):
        in_list = False
        html_parts.append(f"</{list_type}>")

    if not stripped:
        continue

    # Horizontal Rule
    if stripped in ["---", "***", "___"]:
        html_parts.append("<hr />")
        continue

    # Headings
    if stripped.startswith("# "):
        html_parts.append(f"<h1>{stripped[2:]}</h1>")
        continue
    elif stripped.startswith("## "):
        html_parts.append(f"<h2>{stripped[3:]}</h2>")
        continue
    elif stripped.startswith("### "):
        html_parts.append(f"<h3>{stripped[4:]}</h3>")
        continue
    elif stripped.startswith("#### "):
        html_parts.append(f"<h4>{stripped[5:]}</h4>")
        continue

    # Blockquotes
    if stripped.startswith("> "):
        content = stripped[2:]
        html_parts.append(f'<div class="callout">{content}</div>')
        continue

    # Table handling
    if stripped.startswith("|"):
        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if not in_table:
            in_table = True
            html_parts.append("<table><thead><tr>")
            for c in cells:
                html_parts.append(f"<th>{c}</th>")
            html_parts.append("</tr></thead><tbody>")
            continue
        elif all(set(c).issubset({"-", ":", " "}) for c in cells):
            # separator row
            continue
        else:
            html_parts.append("<tr>")
            for c in cells:
                html_parts.append(f"<td>{c}</td>")
            html_parts.append("</tr>")
            continue

    # Unordered Lists
    if stripped.startswith("- ") or stripped.startswith("* "):
        if not in_list or list_type != "ul":
            if in_list:
                html_parts.append(f"</{list_type}>")
            in_list = True
            list_type = "ul"
            html_parts.append("<ul>")
        item_text = stripped[2:]
        html_parts.append(f"<li>{item_text}</li>")
        continue

    # Ordered Lists
    m_ol = re.match(r"^(\d+)\.\s+(.*)$", stripped)
    if m_ol:
        if not in_list or list_type != "ol":
            if in_list:
                html_parts.append(f"</{list_type}>")
            in_list = True
            list_type = "ol"
            html_parts.append("<ol>")
        item_text = m_ol.group(2)
        html_parts.append(f"<li>{item_text}</li>")
        continue

    # Paragraph with image / inline markdown
    html_parts.append(f"<p>{stripped}</p>")

if in_table:
    html_parts.append("</tbody></table>")
if in_list:
    html_parts.append(f"</{list_type}>")
if in_code:
    html_parts.append("</pre>")

body_html = "\n".join(html_parts)

# Inline formatting replacements
body_html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', image_replacer, body_html)
body_html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', body_html)
body_html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', body_html)
body_html = re.sub(r'`([^`]+)`', r'<code>\1</code>', body_html)
body_html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', body_html)

# Add badges for P0-P3
body_html = body_html.replace('<td>P0</td>', '<td><span class="badge badge-p0">P0</span></td>')
body_html = body_html.replace('<td>P1</td>', '<td><span class="badge badge-p1">P1</span></td>')
body_html = body_html.replace('<td>P2</td>', '<td><span class="badge badge-p2">P2</span></td>')
body_html = body_html.replace('<td>P3</td>', '<td><span class="badge badge-p3">P3</span></td>')

full_html = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>MONOZUKURI PRODUCT & ENGINEERING SUBMISSION REPORT</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4;
      margin: 18mm 14mm 18mm 14mm;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      font-family: 'Inter', sans-serif;
      font-size: 9pt;
      line-height: 1.55;
      color: #1e293b;
      margin: 0;
      padding: 0;
    }}
    h1, h2, h3, h4 {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      color: #0f172a;
      page-break-after: avoid;
    }}
    h1 {{
      font-size: 16pt;
      font-weight: 800;
      color: #007E88;
      border-bottom: 2px solid #01959F;
      padding-bottom: 6px;
      margin-top: 0;
    }}
    h2 {{
      font-size: 12pt;
      color: #01959F;
      border-left: 4px solid #01959F;
      padding-left: 8px;
      margin-top: 1.4em;
      margin-bottom: 0.4em;
    }}
    h3 {{
      font-size: 10pt;
      font-weight: 700;
      margin-top: 1.2em;
      margin-bottom: 0.3em;
    }}
    p, li {{
      color: #334155;
      text-align: justify;
      margin-top: 0.25em;
      margin-bottom: 0.45em;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 8pt;
      page-break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 8px;
      text-align: left;
      vertical-align: top;
    }}
    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    tr:nth-child(even) {{
      background-color: #f8fafc;
    }}
    code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1.5px 4px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}
    pre.code-block {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      background-color: #0f172a;
      color: #f8fafc;
      padding: 10px 12px;
      border-radius: 6px;
      overflow-x: auto;
      line-height: 1.4;
      page-break-inside: avoid;
      margin: 8px 0;
    }}
    .callout {{
      border-left: 4px solid #01959F;
      background-color: #f0fdfa;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 10px 0;
      font-size: 8.5pt;
    }}
    .screenshot-box {{
      margin: 10px 0;
      text-align: center;
      page-break-inside: avoid;
    }}
    .screenshot-img {{
      max-width: 100%;
      max-height: 250px;
      object-fit: contain;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}
    .badge {{
      display: inline-block;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 7.5pt;
      font-weight: 700;
    }}
    .badge-p0 {{ background-color: #fee2e2; color: #b91c1c; }}
    .badge-p1 {{ background-color: #ffedd5; color: #c2410c; }}
    .badge-p2 {{ background-color: #fef9c3; color: #a16207; }}
    .badge-p3 {{ background-color: #e0f2fe; color: #0369a1; }}
    hr {{
      border: 0;
      border-top: 1px solid #e2e8f0;
      margin: 14px 0;
    }}
    a {{
      color: #01959F;
      text-decoration: none;
      font-weight: 600;
    }}
  </style>
</head>
<body>
{body_html}
</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated HTML from Markdown successfully.")

# Run Edge headless to compile PDF
cmd = [
    EDGE_PATH,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_FILE}",
    HTML_FILE
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(PDF_FILE):
    size_kb = os.path.getsize(PDF_FILE) / 1024
    print(f"Generated PDF from Markdown successfully: {PDF_FILE} ({size_kb:.1f} KB)")
    # Cleanup temporary HTML
    if os.path.exists(HTML_FILE):
        os.remove(HTML_FILE)
else:
    print(f"Failed to generate PDF. Stderr: {res.stderr}")
