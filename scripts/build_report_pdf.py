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

# Exact dark-theme Mermaid Flowchart SVG (Step 4)
SVG_FLOWCHART = """
<div class="diagram-box">
  <svg viewBox="0 0 820 280" width="100%" xmlns="http://www.w3.org/2000/svg" style="background-color: #0D141F; font-family: 'Inter', -apple-system, sans-serif; border-radius: 8px;">
    <defs>
      <marker id="cyanArrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M 0 1 L 7 4 L 0 7 z" fill="#0284C7"/>
      </marker>
    </defs>
    
    <!-- Level 1: Root Node -->
    <g transform="translate(325, 20)">
      <rect width="170" height="42" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="85" y="26" fill="#F1F5F9" font-size="11.5" font-weight="600" text-anchor="middle">Revamp Strategies Evaluated</text>
    </g>

    <!-- Connector Paths from Root to Level 2 -->
    <!-- Left path to Option A -->
    <path d="M 360 62 C 360 95, 145 75, 145 105" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>
    <!-- Center path to Option B -->
    <path d="M 410 62 L 410 103" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>
    <!-- Right path to Option C -->
    <path d="M 460 62 C 460 95, 675 75, 675 105" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>

    <!-- Level 2: 3 Options -->
    <!-- Option A -->
    <g transform="translate(45, 107)">
      <rect width="200" height="52" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="100" y="32" fill="#F1F5F9" font-size="11.5" font-weight="600" text-anchor="middle">Option A: Ad-Hoc Hotfixing</text>
    </g>
    <!-- Option B -->
    <g transform="translate(305, 107)">
      <rect width="210" height="64" rx="4" fill="#132032" stroke="#0284C7" stroke-width="2"/>
      <text x="105" y="28" fill="#F1F5F9" font-size="11.5" font-weight="600" text-anchor="middle">Option B: Monozukuri Fullstack</text>
      <text x="105" y="48" fill="#38BDF8" font-size="11.5" font-weight="700" text-anchor="middle">Pivot - SELECTED</text>
    </g>
    <!-- Option C -->
    <g transform="translate(575, 107)">
      <rect width="200" height="64" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="100" y="28" fill="#F1F5F9" font-size="11.5" font-weight="600" text-anchor="middle">Option C: Microservices</text>
      <text x="100" y="48" fill="#F1F5F9" font-size="11.5" font-weight="600" text-anchor="middle">Separation</text>
    </g>

    <!-- Connector Paths from Level 2 to Level 3 -->
    <path d="M 145 160 L 145 198" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>
    <path d="M 410 172 L 410 198" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>
    <path d="M 675 172 L 675 198" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#cyanArrow)"/>

    <!-- Level 3: Consequences -->
    <!-- Low Cost -->
    <g transform="translate(45, 202)">
      <rect width="200" height="52" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="100" y="32" fill="#94A3B8" font-size="10.5" text-anchor="middle">Low Cost, High Long-term Fragility</text>
    </g>
    <!-- Balanced Cost -->
    <g transform="translate(305, 202)">
      <rect width="210" height="58" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="105" y="26" fill="#F1F5F9" font-size="10.5" font-weight="500" text-anchor="middle">Balanced Cost, High Reliability,</text>
      <text x="105" y="44" fill="#38BDF8" font-size="10.5" font-weight="600" text-anchor="middle">Robust UX</text>
    </g>
    <!-- Extreme Complexity -->
    <g transform="translate(575, 202)">
      <rect width="200" height="58" rx="4" fill="#132032" stroke="#0284C7" stroke-width="1.5"/>
      <text x="100" y="26" fill="#94A3B8" font-size="10.5" text-anchor="middle">Extreme Complexity, High Ops</text>
      <text x="100" y="44" fill="#94A3B8" font-size="10.5" text-anchor="middle">Overhead</text>
    </g>
  </svg>
</div>
"""

# Exact dark-theme Mermaid Sequence Diagram SVG (Step 5)
SVG_SEQUENCE = """
<div class="diagram-box">
  <svg viewBox="0 0 920 620" width="100%" xmlns="http://www.w3.org/2000/svg" style="background-color: #0D141F; font-family: 'Inter', -apple-system, sans-serif; border-radius: 8px;">
    <defs>
      <marker id="seqArrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M 0 1 L 7 4 L 0 7 z" fill="#38BDF8"/>
      </marker>
      <marker id="seqArrowDashed" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
        <path d="M 0 1 L 7 4 L 0 7 z" fill="#64748B"/>
      </marker>
    </defs>

    <!-- Lifeline Columns Coordinates:
         Candidate: 60
         React 18 SPA: 170
         Rails 7 API: 295
         Gemini Live: 485
         Sidekiq: 605
         Gemini Pro: 740
         Assessor/Recruiter: 855
    -->

    <!-- Top Participants -->
    <!-- Candidate -->
    <g transform="translate(42, 15)">
      <circle cx="18" cy="8" r="6" fill="none" stroke="#38BDF8" stroke-width="1.5"/>
      <path d="M 18 14 L 18 26 M 8 18 L 28 18 M 18 26 L 10 37 M 18 26 L 26 37" fill="none" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="18" y="48" fill="#94A3B8" font-size="9" text-anchor="middle">Candidate</text>
    </g>
    <!-- React 18 SPA -->
    <g transform="translate(130, 22)">
      <rect width="80" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="40" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">React 18 SPA (Vite)</text>
    </g>
    <!-- Rails 7 API -->
    <g transform="translate(265, 22)">
      <rect width="60" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="30" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Rails 7 API</text>
    </g>
    <!-- Gemini Live -->
    <g transform="translate(440, 22)">
      <rect width="90" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="45" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Gemini Live (v1alpha)</text>
    </g>
    <!-- Sidekiq Worker -->
    <g transform="translate(565, 22)">
      <rect width="80" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="40" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Sidekiq Worker Queue</text>
    </g>
    <!-- Gemini Pro -->
    <g transform="translate(705, 22)">
      <rect width="70" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="35" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Gemini Pro (v1beta)</text>
    </g>
    <!-- Assessor / Recruiter -->
    <g transform="translate(820, 22)">
      <rect width="70" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="35" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Assessor / Recruiter</text>
    </g>

    <!-- Vertical Lifelines -->
    <line x1="60" y1="58" x2="60" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="170" y1="52" x2="170" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="295" y1="52" x2="295" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="485" y1="52" x2="485" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="605" y1="52" x2="605" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="740" y1="52" x2="740" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
    <line x1="855" y1="52" x2="855" y2="560" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>

    <!-- Step 1: Candidate -> Web -->
    <line x1="60" y1="90" x2="165" y2="90" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="68" cy="90" r="4.5" fill="#E2E8F0"/>
    <text x="115" y="82" fill="#E2E8F0" font-size="8" text-anchor="middle">Start Interview Session</text>

    <!-- Step 2: Web -> Rails -->
    <line x1="170" y1="125" x2="290" y2="125" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="170" cy="125" r="4.5" fill="#E2E8F0"/>
    <text x="232" y="117" fill="#E2E8F0" font-size="8" text-anchor="middle">WebSocket Connection (/cable)</text>

    <!-- Step 3: Rails -> GeminiWS -->
    <line x1="295" y1="160" x2="480" y2="160" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="295" cy="160" r="4.5" fill="#E2E8F0"/>
    <text x="388" y="152" fill="#E2E8F0" font-size="7.5" text-anchor="middle">BidiGenerateContent Handshake (gemini-2.5-flash-native-audio-latest)</text>

    <!-- Step 4: GeminiWS --> Rails -->
    <line x1="485" y1="190" x2="300" y2="190" stroke="#94A3B8" stroke-width="1.3" stroke-dasharray="3,3" marker-end="url(#seqArrowDashed)"/>
    <circle cx="485" cy="190" r="4.5" fill="#E2E8F0"/>
    <text x="390" y="182" fill="#94A3B8" font-size="8" text-anchor="middle">setupComplete { }</text>

    <!-- Note over Candidate, GeminiWS -->
    <rect x="50" y="210" width="445" height="26" rx="3" fill="#1E293B" stroke="#475569" stroke-width="1"/>
    <text x="272" y="227" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Real-time Audio Exchange &amp; Waveform Streaming</text>

    <!-- Step 5: Candidate -> Web -->
    <line x1="60" y1="265" x2="165" y2="265" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="68" cy="265" r="4.5" fill="#E2E8F0"/>
    <text x="115" y="257" fill="#E2E8F0" font-size="8" text-anchor="middle">Finish Interview</text>

    <!-- Step 6: Web -> Rails -->
    <line x1="170" y1="298" x2="290" y2="298" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="170" cy="298" r="4.5" fill="#E2E8F0"/>
    <text x="232" y="290" fill="#E2E8F0" font-size="8" text-anchor="middle">Complete Session</text>

    <!-- Step 7: Rails -> Sidekiq -->
    <line x1="295" y1="330" x2="600" y2="330" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="295" cy="330" r="4.5" fill="#E2E8F0"/>
    <text x="450" y="322" fill="#E2E8F0" font-size="8" text-anchor="middle">Enqueue PortfolioGeneratorWorker</text>

    <!-- Step 8: Sidekiq -> GeminiREST -->
    <line x1="605" y1="365" x2="735" y2="365" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="605" cy="365" r="4.5" fill="#E2E8F0"/>
    <text x="670" y="357" fill="#E2E8F0" font-size="7.5" text-anchor="middle">Evaluate Transcript &amp; Behavioral Anchors (gemini-3.1-pro-preview)</text>

    <!-- Step 9: GeminiREST --> Sidekiq -->
    <line x1="740" y1="400" x2="610" y2="400" stroke="#94A3B8" stroke-width="1.3" stroke-dasharray="3,3" marker-end="url(#seqArrowDashed)"/>
    <circle cx="740" cy="400" r="4.5" fill="#E2E8F0"/>
    <text x="675" y="392" fill="#94A3B8" font-size="8" text-anchor="middle">Structured Evidence JSON</text>

    <!-- Step 10: Sidekiq -> Rails -->
    <line x1="605" y1="435" x2="300" y2="435" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="605" cy="435" r="4.5" fill="#E2E8F0"/>
    <text x="450" y="427" fill="#E2E8F0" font-size="8" text-anchor="middle">Save PortfolioSkills &amp; Evidence Quotes</text>

    <!-- Step 11: Recruiter -> Web -->
    <line x1="855" y1="470" x2="175" y2="470" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="855" cy="470" r="4.5" fill="#E2E8F0"/>
    <text x="515" y="462" fill="#E2E8F0" font-size="8" text-anchor="middle">Open Candidate Portfolio</text>

    <!-- Step 12: Web -> Rails -->
    <line x1="170" y1="502" x2="290" y2="502" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="170" cy="502" r="4.5" fill="#E2E8F0"/>
    <text x="232" y="494" fill="#E2E8F0" font-size="8" text-anchor="middle">GET /api/v1/sessions/:id/portfolio</text>

    <!-- Step 13: Recruiter -> Web -->
    <line x1="855" y1="532" x2="175" y2="532" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="855" cy="532" r="4.5" fill="#E2E8F0"/>
    <text x="515" y="524" fill="#E2E8F0" font-size="8" text-anchor="middle">Trigger Fit/Gap &amp; Download PDF</text>

    <!-- Step 14: Rails -> Web -->
    <line x1="295" y1="560" x2="175" y2="560" stroke="#38BDF8" stroke-width="1.3" marker-end="url(#seqArrow)"/>
    <circle cx="295" cy="560" r="4.5" fill="#E2E8F0"/>
    <text x="235" y="552" fill="#E2E8F0" font-size="8" text-anchor="middle">Stream Prawn-generated PDF Dossier</text>

    <!-- Bottom Participants -->
    <!-- Candidate -->
    <g transform="translate(42, 575)">
      <circle cx="18" cy="8" r="6" fill="none" stroke="#38BDF8" stroke-width="1.5"/>
      <path d="M 18 14 L 18 26 M 8 18 L 28 18 M 18 26 L 10 37 M 18 26 L 26 37" fill="none" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="18" y="48" fill="#94A3B8" font-size="9" text-anchor="middle">Candidate</text>
    </g>
    <!-- React 18 SPA -->
    <g transform="translate(130, 582)">
      <rect width="80" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="40" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">React 18 SPA (Vite)</text>
    </g>
    <!-- Rails 7 API -->
    <g transform="translate(265, 582)">
      <rect width="60" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="30" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Rails 7 API</text>
    </g>
    <!-- Gemini Live -->
    <g transform="translate(440, 582)">
      <rect width="90" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="45" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Gemini Live (v1alpha)</text>
    </g>
    <!-- Sidekiq Worker -->
    <g transform="translate(565, 582)">
      <rect width="80" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="40" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Sidekiq Worker Queue</text>
    </g>
    <!-- Gemini Pro -->
    <g transform="translate(705, 582)">
      <rect width="70" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="35" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Gemini Pro (v1beta)</text>
    </g>
    <!-- Assessor / Recruiter -->
    <g transform="translate(820, 582)">
      <rect width="70" height="28" rx="3" fill="#132032" stroke="#0284C7" stroke-width="1.2"/>
      <text x="35" y="18" fill="#F1F5F9" font-size="8.5" font-weight="600" text-anchor="middle">Assessor / Recruiter</text>
    </g>
  </svg>
</div>
"""

# Image replacer
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

# Clean markdown parser with zero extra spacing and zero broken tags
lines = md_content.split("\n")
html_parts = []
in_mermaid = False
mermaid_kind = ""
in_code = False
in_table = False
list_stack = []

def close_all_lists():
    res = []
    while list_stack:
        tag = list_stack.pop()
        res.append(f"</{tag}>")
    return res

for line in lines:
    raw_stripped = line.strip()
    
    # Handle Mermaid blocks
    if raw_stripped.startswith("```mermaid"):
        in_mermaid = True
        mermaid_kind = "flowchart" if "graph" in lines[lines.index(line)+1] else "sequence"
        continue
    elif in_mermaid:
        if raw_stripped.startswith("```"):
            in_mermaid = False
            if mermaid_kind == "flowchart":
                html_parts.append(SVG_FLOWCHART)
            else:
                html_parts.append(SVG_SEQUENCE)
        continue

    # Code blocks
    if raw_stripped.startswith("```"):
        if in_code:
            in_code = False
            html_parts.append("</pre>")
            continue
        else:
            in_code = True
            lang = raw_stripped[3:].strip()
            html_parts.append(f'<pre class="code-block {lang}">')
            continue
            
    if in_code:
        html_parts.append(html.escape(line))
        continue

    # Close table if left
    if in_table and not raw_stripped.startswith("|"):
        in_table = False
        html_parts.append("</tbody></table>")

    if not raw_stripped:
        continue

    # Horizontal Rule
    if raw_stripped in ["---", "***", "___"]:
        html_parts.extend(close_all_lists())
        html_parts.append("<hr />")
        continue

    # Headings
    if raw_stripped.startswith("# "):
        html_parts.extend(close_all_lists())
        html_parts.append(f"<h1>{raw_stripped[2:]}</h1>")
        continue
    elif raw_stripped.startswith("## "):
        html_parts.extend(close_all_lists())
        html_parts.append(f"<h2>{raw_stripped[3:]}</h2>")
        continue
    elif raw_stripped.startswith("### "):
        html_parts.extend(close_all_lists())
        html_parts.append(f"<h3>{raw_stripped[4:]}</h3>")
        continue
    elif raw_stripped.startswith("#### "):
        html_parts.extend(close_all_lists())
        html_parts.append(f"<h4>{raw_stripped[5:]}</h4>")
        continue

    # Blockquotes
    if raw_stripped.startswith("> "):
        html_parts.extend(close_all_lists())
        content = raw_stripped[2:]
        html_parts.append(f'<div class="callout">{content}</div>')
        continue

    # Tables
    if raw_stripped.startswith("|"):
        html_parts.extend(close_all_lists())
        cells = [c.strip() for c in raw_stripped.split("|")[1:-1]]
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
    m_ol = re.match(r"^(\d+)\.\s+(.*)$", raw_stripped)
    if m_ol:
        if not list_stack or list_stack[-1] != "ol":
            html_parts.extend(close_all_lists())
            html_parts.append("<ol>")
            list_stack.append("ol")
        html_parts.append(f"<li>{m_ol.group(2)}</li>")
        continue

    # Unordered list (nested or root)
    if raw_stripped.startswith("- ") or raw_stripped.startswith("* "):
        if not list_stack or list_stack[-1] != "ul":
            html_parts.append("<ul>")
            list_stack.append("ul")
        html_parts.append(f"<li>{raw_stripped[2:]}</li>")
        continue

    # Plain paragraph
    html_parts.extend(close_all_lists())
    html_parts.append(f"<p>{raw_stripped}</p>")

html_parts.extend(close_all_lists())
if in_table:
    html_parts.append("</tbody></table>")
if in_code:
    html_parts.append("</pre>")

body_html = "\n".join(html_parts)

# Inline formatting without creating empty boxes
body_html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', image_replacer, body_html)
body_html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', body_html)
body_html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', body_html)

# Only match non-empty code strings to prevent rogue bubbles
body_html = re.sub(r'`([^`\n]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>' if m.group(1).strip() else '', body_html)
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
      margin: 15mm 13mm 15mm 13mm;
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
      padding-bottom: 4px;
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
      margin-top: 0.85em;
      margin-bottom: 0.25em;
    }}
    p {{
      color: #334155;
      text-align: justify;
      margin-top: 0.15em;
      margin-bottom: 0.3em;
    }}
    ul, ol {{
      margin-top: 0.15em;
      margin-bottom: 0.35em;
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
      background-color: #f8fafc;
      color: #0f172a;
      padding: 1px 3px;
      border-radius: 3px;
      border: 1px solid #e2e8f0;
      display: inline;
    }}
    pre.code-block {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.5pt;
      background-color: #0D141F;
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
      padding: 7px 11px;
      border-radius: 0 6px 6px 0;
      margin: 7px 0;
      font-size: 8pt;
    }}
    .diagram-box {{
      margin: 10px 0;
      border-radius: 8px;
      overflow: hidden;
      page-break-inside: avoid;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
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
      margin: 9px 0;
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
