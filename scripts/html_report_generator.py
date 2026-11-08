
#!/usr/bin/env python3

"""
SNIT HTML Report Generator
Converts parsed Nmap JSON results into an HTML report.
"""

import argparse
import json
from pathlib import Path
from datetime import datetime
from html import escape


def load_json(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def generate_html(data):
    target = escape(str(data.get("target", "Unknown")))
    status = escape(str(data.get("status", "Unknown")))
    open_ports = data.get("open_ports", [])
    filtered = data.get("filtered_ports", 0)
    closed = data.get("closed_ports", 0)
    duration = data.get("scan_duration", "Unknown")

    rows = ""

    for item in open_ports:
        rows += f"""
        <tr>
            <td>{escape(str(item.get("port", "")))}</td>
            <td>{escape(str(item.get("protocol", "")))}</td>
            <td>{escape(str(item.get("service", "")))}</td>
            <td>{escape(str(item.get("version", "")))}</td>
        </tr>
        """

    if not rows:
        rows = '<tr><td colspan="4">No open ports detected</td></tr>'

    generated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>SNIT Network Scanning Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f3f6fa;
    color: #243447;
    margin: 0;
    padding: 30px;
}}

.container {{
    max-width: 1000px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}}

.header {{
    background: #17365d;
    color: white;
    padding: 25px;
    border-radius: 8px;
}}

.header h1 {{
    margin: 0;
}}

.subtitle {{
    color: #dce6f1;
    margin-bottom: 0;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin: 25px 0;
}}

.card {{
    background: #edf3f9;
    padding: 18px;
    border-radius: 8px;
    text-align: center;
}}

.card h2 {{
    margin: 5px 0;
    color: #17365d;
}}

.card p {{
    margin: 0;
    font-size: 13px;
}}

h2 {{
    color: #17365d;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
}}

th, td {{
    padding: 13px;
    border: 1px solid #dce3eb;
    text-align: left;
}}

th {{
    background: #17365d;
    color: white;
}}

tr:nth-child(even) {{
    background: #f5f8fb;
}}

.footer {{
    margin-top: 30px;
    padding-top: 15px;
    border-top: 1px solid #ddd;
    color: #667788;
    font-size: 13px;
}}

@media (max-width: 650px) {{
    body {{ padding: 10px; }}
    .container {{ padding: 15px; }}
    .cards {{ grid-template-columns: repeat(2, 1fr); }}
    table {{ font-size: 12px; }}
}}
</style>
</head>

<body>

<div class="container">

<div class="header">
    <h1>SNIT Training Institute</h1>
    <p class="subtitle">Network Scanning Assessment Report</p>
</div>

<h2>Assessment Summary</h2>

<p><strong>Target IP:</strong> {target}</p>
<p><strong>Host Status:</strong> {status}</p>
<p><strong>Generated On:</strong> {generated_at}</p>

<div class="cards">
    <div class="card">
        <p>Open Ports</p>
        <h2>{len(open_ports)}</h2>
    </div>

    <div class="card">
        <p>Filtered Ports</p>
        <h2>{filtered}</h2>
    </div>

    <div class="card">
        <p>Closed Ports</p>
        <h2>{closed}</h2>
    </div>

    <div class="card">
        <p>Scan Duration</p>
        <h2>{duration}s</h2>
    </div>
</div>

<h2>Detected Services</h2>

<table>
<thead>
<tr>
    <th>Port</th>
    <th>Protocol</th>
    <th>Service</th>
    <th>Version</th>
</tr>
</thead>

<tbody>
{rows}
</tbody>
</table>

<div class="footer">
    <p>Prepared by SNIT Training Institute</p>
    <p>Generated automatically using SNIT Nmap Automation Toolkit.</p>
    <p>For authorized security assessment and educational use only.</p>
</div>

</div>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser(
        description="SNIT HTML Report Generator"
    )

    parser.add_argument(
        "json_file",
        help="Path to parsed Nmap JSON file"
    )

    parser.add_argument(
        "-o", "--output",
        default="snit_scanning_report.html",
        help="HTML output filename"
    )

    args = parser.parse_args()

    try:
        data = load_json(args.json_file)
        html = generate_html(data)

        Path(args.output).write_text(
            html,
            encoding="utf-8"
        )

        print("[SNIT] HTML report generated successfully.")
        print(f"[SNIT] Report location: {args.output}")

    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
