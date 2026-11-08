
#!/usr/bin/env python3

"""
SNIT Scan Summary Dashboard
Displays Nmap scan statistics and detected services.
"""

import argparse
import json
from pathlib import Path
from html import escape


def load_results(filename):
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def create_dashboard(data):

    target = escape(str(data.get("target", "Unknown")))
    status = escape(str(data.get("status", "Unknown")))

    open_ports = data.get("open_ports", [])
    filtered = data.get("filtered_ports", 0)
    closed = data.get("closed_ports", 0)
    duration = data.get("scan_duration", "Unknown")

    service_rows = ""

    for item in open_ports:
        service_rows += f"""
        <tr>
            <td>{escape(str(item.get('port', '')))}</td>
            <td>{escape(str(item.get('protocol', '')))}</td>
            <td>{escape(str(item.get('service', '')))}</td>
            <td>{escape(str(item.get('version', '')))}</td>
        </tr>
        """

    if not service_rows:
        service_rows = "<tr><td colspan='4'>No open ports found</td></tr>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>SNIT Scan Dashboard</title>

<style>
* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f1f4f8;
    color: #243447;
}}

header {{
    background: #172f50;
    color: white;
    padding: 25px 5%;
}}

header h1 {{
    margin: 0;
}}

header p {{
    color: #cbd7e6;
}}

.container {{
    max-width: 1100px;
    margin: 30px auto;
    padding: 0 20px;
}}

.info {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-bottom: 25px;
}}

.card {{
    background: white;
    padding: 22px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}}

.card p {{
    color: #68778a;
    margin: 0;
}}

.card h2 {{
    font-size: 30px;
    margin: 12px 0 0;
}}

.section {{
    background: white;
    padding: 22px;
    border-radius: 10px;
    margin-bottom: 20px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
}}

th, td {{
    padding: 13px;
    text-align: left;
    border-bottom: 1px solid #e3e8ef;
}}

th {{
    background: #edf2f8;
}}

footer {{
    text-align: center;
    padding: 25px;
    color: #718096;
}}

@media(max-width: 700px) {{
    .cards {{
        grid-template-columns: repeat(2, 1fr);
    }}

    table {{
        font-size: 12px;
    }}
}}
</style>
</head>

<body>

<header>
    <h1>SNIT Scan Dashboard</h1>
    <p>Network Scanning Summary & Service Analysis</p>
</header>

<div class="container">

<div class="info">
    <h2>Target Information</h2>
    <p><strong>Target IP:</strong> {target}</p>
    <p><strong>Host Status:</strong> {status}</p>
</div>

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

<div class="section">
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
            {service_rows}
        </tbody>
    </table>
</div>

</div>

<footer>
    SNIT Training Institute | Network Scanning Toolkit
</footer>

</body>
</html>
"""


def main():

    parser = argparse.ArgumentParser(
        description="SNIT Scan Dashboard Generator"
    )

    parser.add_argument(
        "json_file",
        help="Parsed Nmap JSON file"
    )

    parser.add_argument(
        "-o", "--output",
        default="snit_scan_dashboard.html"
    )

    args = parser.parse_args()

    try:
        data = load_results(args.json_file)
        html = create_dashboard(data)

        Path(args.output).write_text(
            html,
            encoding="utf-8"
        )

        print("[SNIT] Dashboard generated successfully.")
        print("[SNIT] Output:", args.output)

    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
