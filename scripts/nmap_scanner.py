
#!/usr/bin/env python3

"""
SNIT Nmap Automation Tool
Purpose: Automate basic network scanning in an authorized lab.
"""

import argparse
import ipaddress
import shutil
import subprocess
from pathlib import Path
from datetime import datetime


def validate_target(target):
    """Accept private IP addresses only."""

    try:
        address = ipaddress.ip_address(target)

        if not address.is_private:
            raise ValueError("Only private lab IP addresses are allowed.")

        return str(address)

    except ValueError:
        try:
            network = ipaddress.ip_network(target, strict=False)

            if not network.is_private:
                raise ValueError("Only private lab networks are allowed.")

            if network.num_addresses > 256:
                raise ValueError("Network range is too large. Maximum: 256 addresses.")

            return str(network)

        except ValueError as error:
            raise ValueError(f"Invalid target: {error}")


def run_scan(target, output_dir):
    """Run Nmap and save scan results."""

    if not shutil.which("nmap"):
        print("[ERROR] Nmap is not installed.")
        return False

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = output_dir / f"snit_scan_{timestamp}"

    command = [
        "nmap",
        "-sV",
        "-T3",
        "-p", "1-1000",
        "-oA", str(report_name),
        target
    ]

    print("\n[SNIT] Starting authorized lab scan...")
    print(f"[SNIT] Target: {target}")
    print(f"[SNIT] Output: {report_name}")

    try:
        subprocess.run(command, check=True)
        print("\n[SNIT] Scan completed successfully.")
        print("[SNIT] Reports saved in text, XML and grepable formats.")
        return True

    except subprocess.CalledProcessError as error:
        print(f"[ERROR] Nmap failed: {error}")
        return False

    except KeyboardInterrupt:
        print("\n[SNIT] Scan interrupted by user.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="SNIT Nmap Automation Tool"
    )

    parser.add_argument(
        "target",
        help="Private lab IP address or network range"
    )

    parser.add_argument(
        "-o", "--output",
        default="reports",
        help="Output directory (default: reports)"
    )

    args = parser.parse_args()

    try:
        target = validate_target(args.target)
    except ValueError as error:
        parser.error(str(error))

    print("=" * 45)
    print("       SNIT NMAP AUTOMATION TOOL")
    print("=" * 45)

    run_scan(target, args.output)


if __name__ == "__main__":
    main()
