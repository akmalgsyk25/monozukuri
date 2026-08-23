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

# Vector SVG 1: Technical Option Evaluation Tree
SVG_STRATEGY_TREE = """
<div class="diagram-container">
  <svg viewBox="0 0 760 170" width="100%" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
    <defs>
      <linearGradient id="selectedGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#01959F"/>
        <stop offset="100%" stop-color="#006C74"/>
      </linearGradient>
      <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
        <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.08"/>
      </filter>
    </defs>
    
    <!-- Connecting Lines -->
    <path d="M 380 44 L 380 65 L 125 65 L 125 85" fill="none" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4"/>
    <path d="M 380 44 L 380 85" fill="none" stroke="#01959F" stroke-width="2.5"/>
    <path d="M 380 65 L 635 65 L 635 85" fill="none" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="4,4"/>

    <!-- Root Node -->
    <rect x="260" y="8" width="240" height="38" rx="8" fill="#0D141F" filter="url(#cardShadow)"/>
    <text x="380" y="32" fill="#FFFFFF" font-size="11" font-weight="700" text-anchor="middle">Revamp Strategies Evaluated</text>

    <!-- Option A -->
    <rect x="15" y="85" width="220" height="74" rx="8" fill="#FFF5F5" stroke="#FEB2B2" stroke-width="1.5" filter="url(#cardShadow)"/>
    <text x="125" y="108" fill="#9B1C1C" font-size="10.5" font-weight="700" text-anchor="middle">Option A: Ad-Hoc Hotfixing</text>
    <text x="125" y="128" fill="#6B7280" font-size="8.5" text-anchor="middle">Low Cost • High Fragility</text>
    <text x="125" y="144" fill="#9B1C1C" font-size="8" font-weight="600" text-anchor="middle">❌ Rejected (Tech Debt Remains)</text>

    <!-- Option B (Selected) -->
    <rect x="255" y="85" width="250" height="76" rx="8" fill="url(#selectedGrad)" stroke="#01959F" stroke-width="2" filter="url(#cardShadow)"/>
    <text x="380" y="108" fill="#FFFFFF" font-size="11" font-weight="800" text-anchor="middle">Option B: Monozukuri Fullstack</text>
    <text x="380" y="128" fill="#E6FFFA" font-size="9" text-anchor="middle">Balanced Cost • High Rigor • Resilient UX</text>
    <rect x="315" y="136" width="130" height="18" rx="4" fill="#FBC037"/>
    <text x="380" y="149" fill="#0D141F" font-size="8" font-weight="800" text-anchor="middle">★ SELECTED APPROACH</text>

    <!-- Option C -->
    <rect x="525" y="85" width="220" height="74" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" filter="url(#cardShadow)"/>
    <text x="635" y="108" fill="#334155" font-size="10.5" font-weight="700" text-anchor="middle">Option C: Microservices Extraction</text>
    <text x="635" y="128" fill="#6B7280" font-size="8.5" text-anchor="middle">Extreme Complexity • 2+ Weeks</text>
    <text x="635" y="144" fill="#64748B" font-size="8" font-weight="600" text-anchor="middle">❌ Rejected (Over-Engineered)</text>
  </svg>
</div>
"""

# Vector SVG 2: Architectural Sequence Flowchart
SVG_SEQUENCE_FLOW = """
<div class="diagram-container">
  <svg viewBox="0 0 760 175" width="100%" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
    <defs>
      <linearGradient id="flowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#01959F"/>
        <stop offset="100%" stop-color="#005F66"/>
      </linearGradient>
    </defs>
    
    <!-- Flow Boxes -->
    <!-- 1: Candidate / Web -->
    <rect x="10" y="15" width="135" height="65" rx="8" fill="#F0FDFA" stroke="#01959F" stroke-width="1.5"/>
    <circle cx="26" cy="30" r="9" fill="#01959F"/>
    <text x="26" y="33.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">1</text>
    <text x="75" y="33" fill="#007E88" font-size="9" font-weight="700">Candidate / Web</text>
    <text x="75" y="50" fill="#475569" font-size="7.5">Pre-flight check &amp;</text>
    <text x="75" y="62" fill="#475569" font-size="7.5">audio streaming start</text>

    <!-- Arrow 1->2 -->
    <path d="M 145 47 L 165 47" fill="none" stroke="#01959F" stroke-width="2" marker-end="url(#arrowhead)"/>
    <polygon points="168,47 160,43 160,51" fill="#01959F"/>

    <!-- 2: Rails WebSocket -->
    <rect x="170" y="15" width="135" height="65" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <circle cx="186" cy="30" r="9" fill="#0F172A"/>
    <text x="186" y="33.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">2</text>
    <text x="235" y="33" fill="#0F172A" font-size="9" font-weight="700">Rails 7 (/cable)</text>
    <text x="235" y="50" fill="#475569" font-size="7.5">Bidi streaming bridge &amp;</text>
    <text x="235" y="62" fill="#475569" font-size="7.5">silence pump (30ms)</text>

    <!-- Arrow 2->3 -->
    <polygon points="328,47 320,43 320,51" fill="#01959F"/>
    <path d="M 305 47 L 325 47" fill="none" stroke="#01959F" stroke-width="2"/>

    <!-- 3: Gemini Live -->
    <rect x="330" y="15" width="135" height="65" rx="8" fill="#EFF6FF" stroke="#3B82F6" stroke-width="1.5"/>
    <circle cx="346" cy="30" r="9" fill="#3B82F6"/>
    <text x="346" y="33.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">3</text>
    <text x="395" y="33" fill="#1D4ED8" font-size="9" font-weight="700">Gemini Live (v1alpha)</text>
    <text x="395" y="50" fill="#475569" font-size="7.5">Native audio 2.5-flash &amp;</text>
    <text x="395" y="62" fill="#475569" font-size="7.5">real-time VAD voice</text>

    <!-- Arrow 3->Down to 4 -->
    <path d="M 465 47 L 490 47 L 490 120 L 145 120" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-dasharray="3,3"/>
    <polygon points="145,120 153,116 153,124" fill="#01959F"/>

    <!-- 4: Sidekiq Background -->
    <rect x="10" y="95" width="135" height="65" rx="8" fill="#FAF5FF" stroke="#A855F7" stroke-width="1.5"/>
    <circle cx="26" cy="110" r="9" fill="#9333EA"/>
    <text x="26" y="113.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">4</text>
    <text x="75" y="113" fill="#6B21A8" font-size="9" font-weight="700">Sidekiq Queue</text>
    <text x="75" y="130" fill="#475569" font-size="7.5">PortfolioGeneratorWorker</text>
    <text x="75" y="142" fill="#475569" font-size="7.5">Idempotent transaction</text>

    <!-- Arrow 4->5 -->
    <path d="M 145 127 L 165 127" fill="none" stroke="#01959F" stroke-width="2"/>
    <polygon points="168,127 160,123 160,131" fill="#01959F"/>

    <!-- 5: Gemini 3.1 Pro -->
    <rect x="170" y="95" width="135" height="65" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5"/>
    <circle cx="186" cy="110" r="9" fill="#D97706"/>
    <text x="186" y="113.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">5</text>
    <text x="235" y="113" fill="#B45309" font-size="9" font-weight="700">Gemini 3.1 Pro</text>
    <text x="235" y="130" fill="#475569" font-size="7.5">Verbatim quote extract &amp;</text>
    <text x="235" y="142" fill="#475569" font-size="7.5">L1-L5 behavioral match</text>

    <!-- Arrow 5->6 -->
    <path d="M 305 127 L 325 127" fill="none" stroke="#01959F" stroke-width="2"/>
    <polygon points="328,127 320,123 320,131" fill="#01959F"/>

    <!-- 6: Fit/Gap & PDF Export -->
    <rect x="330" y="95" width="135" height="65" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
    <circle cx="346" cy="110" r="9" fill="#059669"/>
    <text x="346" y="113.5" fill="#FFFFFF" font-size="8.5" font-weight="800" text-anchor="middle">6</text>
    <text x="395" y="113" fill="#047857" font-size="9" font-weight="700">Fit/Gap &amp; PDF</text>
    <text x="395" y="130" fill="#475569" font-size="7.5">Null-safe vacancy delta &amp;</text>
    <text x="395" y="142" fill="#475569" font-size="7.5">1-click Prawn dossier</text>
  </svg>
</div>
"""

# Image replacer function
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

# Clean Markdown to HTML Parser
lines = md_content.split("\n")
html_parts = []
in_mermaid = False
mermaid_type = ""
in_code = False
in_table = False
in_ol = False
in_ul = False

for line in lines:
    stripped = line.strip()
    
    # Mermaid block detection
    if stripped.startswith("```mermaid"):
        in_mermaid = True
        mermaid_type = "strategy" if len(html_parts) < 150 else "sequence"
        continue
    elif in_mermaid:
        if stripped.startswith("```"):
            in_mermaid = False
            if mermaid_type == "strategy":
                html_parts.append(SVG_STRATEGY_TREE)
            else:
                html_parts.append(SVG_SEQUENCE_FLOW)
        continue

    # Code block detection
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

    # Close table if moving away
    if in_table and not stripped.startswith("|"):
        in_table = False
        html_parts.append("</tbody></table>")

    # Close lists if empty line or non-list
    is_list_item = stripped.startswith("- ") or stripped.startswith("* ") or bool(re.match(r"^\d+\.\s", stripped))
    if not is_list_item:
        if in_ul:
            in_ul = False
            html_parts.append("</ul>")
        if in_ol:
            in_ol = False
            html_parts.append("</ol>")

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

    # Tables
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
            continue
        else:
            html_parts.append("<tr>")
            for c in cells:
                html_parts.append(f"<td>{c}</td>")
            html_parts.append("</tr>")
            continue

    # Ordered list
    m_ol = re.match(r"^(\d+)\.\s+(.*)$", stripped)
    if m_ol:
        if in_ul:
            in_ul = False
            html_parts.append("</ul>")
        if not in_ol:
            in_ol = True
            html_parts.append("<ol>")
        html_parts.append(f"<li>{m_ol.group(2)}</li>")
        continue

    # Unordered list (bullets)
    if stripped.startswith("- ") or stripped.startswith("* "):
        if not in_ul:
            in_ul = True
            html_parts.append("<ul>")
        html_parts.append(f"<li>{stripped[2:]}</li>")
        continue

    # Regular paragraph
    html_parts.append(f"<p>{stripped}</p>")

if in_table:
    html_parts.append("</tbody></table>")
if in_ul:
    html_parts.append("</ul>")
if in_ol:
    html_parts.append("</ol>")
if in_code:
    html_parts.append("</pre>")

body_html = "\n".join(html_parts)

# Inline format replacements
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
      margin: 16mm 14mm 16mm 14mm;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      font-family: 'Inter', sans-serif;
      font-size: 8.5pt;
      line-height: 1.5;
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
      font-size: 15pt;
      font-weight: 800;
      color: #007E88;
      border-bottom: 2px solid #01959F;
      padding-bottom: 5px;
      margin-top: 0;
      margin-bottom: 6px;
    }}
    h2 {{
      font-size: 11.5pt;
      color: #01959F;
      border-left: 4px solid #01959F;
      padding-left: 8px;
      margin-top: 1.1em;
      margin-bottom: 0.35em;
    }}
    h3 {{
      font-size: 9.5pt;
      font-weight: 700;
      margin-top: 0.9em;
      margin-bottom: 0.25em;
    }}
    p {{
      color: #334155;
      text-align: justify;
      margin-top: 0.2em;
      margin-bottom: 0.35em;
    }}
    ul, ol {{
      margin-top: 0.2em;
      margin-bottom: 0.4em;
      padding-left: 18px;
    }}
    li {{
      color: #334155;
      margin-bottom: 0.15em;
      line-height: 1.45;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0;
      font-size: 7.5pt;
      page-break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 5px 7px;
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
      font-size: 7.5pt;
      background-color: #f1f5f9;
      color: #0f172a;
      padding: 1px 3.5px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
    }}
    pre.code-block {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      background-color: #0f172a;
      color: #f8fafc;
      padding: 8px 10px;
      border-radius: 6px;
      overflow-x: auto;
      line-height: 1.35;
      page-break-inside: avoid;
      margin: 6px 0;
    }}
    .callout {{
      border-left: 4px solid #01959F;
      background-color: #f0fdfa;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin: 8px 0;
      font-size: 8pt;
    }}
    .diagram-container {{
      margin: 10px 0;
      padding: 8px;
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      text-align: center;
      page-break-inside: avoid;
    }}
    .screenshot-box {{
      margin: 8px 0 12px 0;
      text-align: center;
      page-break-inside: avoid;
    }}
    .screenshot-img {{
      max-width: 100%;
      max-height: 240px;
      object-fit: contain;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
      box-shadow: 0 2px 5px rgba(0,0,0,0.06);
    }}
    .badge {{
      display: inline-block;
      padding: 1px 5px;
      border-radius: 4px;
      font-size: 7pt;
      font-weight: 700;
    }}
    .badge-p0 {{ background-color: #fee2e2; color: #b91c1c; }}
    .badge-p1 {{ background-color: #ffedd5; color: #c2410c; }}
    .badge-p2 {{ background-color: #fef9c3; color: #a16207; }}
    .badge-p3 {{ background-color: #e0f2fe; color: #0369a1; }}
    hr {{
      border: 0;
      border-top: 1px solid #e2e8f0;
      margin: 10px 0;
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
    print(f"Generated PDF successfully: {PDF_FILE} ({size_kb:.1f} KB)")
    if os.path.exists(HTML_FILE):
        os.remove(HTML_FILE)
else:
    print(f"Failed to generate PDF. Stderr: {res.stderr}")
