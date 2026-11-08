
#!/usr/bin/env python3

import argparse
import re
import json
from pathlib import Path
from datetime import datetime


def parse_nmap_report(file_path):

    report = Path(file_path)

    if not report.exists():
        raise FileNotFoundError(f"Report not found: {file_path}")

    content = report.read_text(errors="replace")

    result = {
        "target": None,
        "status": "Unknown",
        "open_ports": [],
        "filtered_ports": 0,
        "closed_ports": 0,
        "scan_duration": None,
        "services": []
    }

    host = re.search(r"Nmap scan report for (.+)", content)

    if host:
        result["target"] = host.group(1)

    if "Host is up" in content:
        result["status"] = "Up"

    filtered = re.search(
        r"Not shown:\s+(\d+)\s+filtered",
        content
    )

    if filtered:
        result["filtered_ports"] = int(filtered.group(1))

    closed = re.search(
        r"Not shown:\s+(\d+)\s+closed",
        content
    )

    if closed:
        result["closed_ports"] = int(closed.group(1))

    for line in content.splitlines():

        match = re.match(
            r"^\s*(\d+)/(tcp|udp)\s+open\s+(\S+)\s*(.*)$",
            line
        )

        if match:
            port, protocol, service, version = match.groups()

            result["open_ports"].append({
                "port": int(port),
                "protocol": protocol,
                "service": service,
                "version": version.strip() or "Not identified"
            })

    result["services"] = sorted(
        {item["service"] for item in result["open_ports"]}
    )

    duration = re.search(
        r"scanned in ([\d.]+) seconds",
        content
    )

    if duration:
        result["scan_duration"] = float(duration.group(1))

    return result


def main():

    parser = argparse.ArgumentParser(
        description="SNIT Nmap Scan Result Parser"
    )

    parser.add_argument(
        "report",
        help="Path to Nmap .nmap report"
    )

    parser.add_argument(
        "-o", "--output",
        default="parsed_scan_results.json",
        help="JSON output filename"
    )

    args = parser.parse_args()

    try:
        data = parse_nmap_report(args.report)

        print("\n===== SNIT SCAN RESULT PARSER =====")
        print("Target:", data["target"])
        print("Host Status:", data["status"])
        print("Open Ports:", len(data["open_ports"]))
        print("Filtered Ports:", data["filtered_ports"])
        print("Closed Ports:", data["closed_ports"])
        print("Scan Duration:", data["scan_duration"])

        print("\nDetected Services:")

        for item in data["open_ports"]:
            print(
                f'{item["port"]}/{item["protocol"]} | '
                f'{item["service"]} | {item["version"]}'
            )

        data["parsed_at"] = datetime.now().isoformat()

        Path(args.output).write_text(
            json.dumps(data, indent=4)
        )

        print("\nJSON report saved:", args.output)

    except (FileNotFoundError, OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
