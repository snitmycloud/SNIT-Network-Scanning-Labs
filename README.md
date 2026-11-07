# SNIT Network Scanning Labs

### Practical Network Scanning & Nmap Training for Cybersecurity

**SNIT Network Scanning Labs** is a hands-on cybersecurity training project developed by SNIT Training Institute. It provides practical exercises for understanding network scanning, host discovery, TCP/UDP port scanning, service identification and network traffic analysis.

The project uses Kali Linux, Nmap, Wireshark and vulnerable virtual machines to provide practical learning in controlled laboratory environments.

## 1. Learning Objectives

Students will learn to:

- Understand network scanning concepts and methodologies.
- Identify live hosts and network devices.
- Perform TCP and UDP port scanning.
- Understand open, closed and filtered port states.
- Identify running services and versions.
- Understand operating system fingerprinting.
- Analyze network traffic using Wireshark.
- Understand firewall and IDS responses.
- Generate network scanning reports.

## 2. Training Curriculum

| Module | Topics |
|---|---|
| 01 | Scanning Fundamentals |
| 02 | Vulnerable Lab Setup |
| 03 | Nmap Fundamentals |
| 04 | TCP Port Scanning |
| 05 | UDP Port Scanning |
| 06 | Service & Version Detection |
| 07 | OS Detection |
| 08 | Firewall and IDS Analysis |
| 09 | Practical Scanning & Reporting |

## 3. Tools & Technologies

- Nmap
- Zenmap
- Wireshark
- Netcat
- Kali Linux
- Metasploitable 2
- VirtualBox / VMware
- Python 3

## 4. Project Structure

```text
SNIT-Network-Scanning-Labs/
│
├── README.md
├── requirements.txt
│
├── labs/
│   ├── README.md
│   └── practical_exercises/
│
├── scripts/
│   └── README.md
│
├── lab_environment/
│   └── README.md
│
├── reports/
│   └── README.md
│
└── screenshots/
    └── README.md
```

## 5. Lab Environment Requirements

Recommended environment:

- Kali Linux
- VirtualBox or VMware Workstation
- Metasploitable 2 vulnerable virtual machine
- Minimum 8 GB RAM recommended for a comfortable virtual lab
- Two isolated virtual machines on an internal or host-only network

Never expose vulnerable lab machines directly to public networks.

## 6. Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/snitmycloud/SNIT-Network-Scanning-Labs.git
```

### Step 2: Navigate to the Project

```bash
cd SNIT-Network-Scanning-Labs
```

### Step 3: Update Kali Linux

```bash
sudo apt update
```

### Step 4: Install Nmap and Wireshark

```bash
sudo apt install nmap wireshark netcat-openbsd -y
```

### Step 5: Verify Nmap Installation

```bash
nmap --version
```

### Step 6: Display Nmap Help

```bash
nmap --help
```

## 7. Practical Exercises

The practical exercises cover:

1. Host discovery in an isolated lab.
2. Basic Nmap scanning.
3. TCP SYN and TCP Connect scanning.
4. UDP port scanning.
5. Open, closed and filtered port analysis.
6. Service and version detection.
7. Operating system detection.
8. Packet analysis using Wireshark.
9. Firewall response analysis.
10. Network scanning report preparation.

## 8. Assessment & Project

**Project Title:** Network Scanning & Service Enumeration Assessment

Students will perform a controlled network scanning assessment against a vulnerable virtual machine.

**Expected Deliverables:**

- Live host discovery results.
- TCP/UDP scan results.
- Open port identification.
- Service and version information.
- Wireshark packet analysis.
- Technical scanning report.

## 9. Security Disclaimer

This repository is intended for cybersecurity education, research and authorized security testing.

- Scan only systems you own or have explicit permission to assess.
- Perform practical exercises inside isolated virtual lab environments.
- Obtain authorization before scanning organizational or third-party networks.
- Do not use scanning techniques to disrupt or access unauthorized systems.

SNIT Training Institute is not responsible for unauthorized use of the training materials.

## 10. Author

**SNIT Training Institute**

GitHub: https://github.com/snitmycloud

Project: SNIT Network Scanning Labs

**Learn. Practice. Analyze. Secure.**

## 📚 Student Resources

Useful resources for students and trainers:

- [Practical Lab Index](labs/README.md)
- [Student Assessment Checklist](STUDENT_ASSESSMENT.md)
- [Troubleshooting Guide](TROUBLESHOOTING.md)

## 🎯 Learning Path

Follow the practical labs in numerical order, complete each exercise, capture screenshots, and maintain your scan reports.

## 📋 Student Guidelines

1. Complete all practical exercises in the specified order.
2. Use only authorized lab targets.
3. Save Nmap scan results.
4. Maintain screenshots of practical activities.
5. Submit the final scanning assessment report.
6. Review the troubleshooting guide whenever you encounter lab issues.
