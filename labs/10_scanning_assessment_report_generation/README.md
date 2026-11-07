# Lab 10: Scanning Assessment & Report Generation

## 1. Objective

Perform a complete network scanning assessment against an authorized lab environment, analyze the results, and prepare a structured technical scanning report.

## 2. Topics Covered

- Scanning assessment methodology
- Target identification
- Host discovery
- TCP port scanning
- UDP port scanning
- Service and version detection
- OS fingerprinting
- Firewall behavior analysis
- Nmap output formats
- Technical report preparation

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Netcat
- Authorized vulnerable lab VM
- Text editor or document editor

## 4. Assessment Scenario

You are working as a junior security analyst.

Your task is to perform a basic network scanning assessment against an isolated lab network containing intentionally vulnerable virtual machines.

You must identify active hosts, discover exposed ports, identify services, estimate operating systems, and document your findings.

**Assessment scope:**

| Parameter | Details |
|---|---|
| Target | Authorized lab VM |
| Network | Isolated virtual network |
| Scanner | Kali Linux |
| Scanning tool | Nmap |
| Traffic analysis | Wireshark |
| Output | Technical scanning report |

## 5. Practical Assessment

### Exercise 1: Host Discovery

Identify active systems in your authorized lab network.

```bash
nmap -sn <LAB-NETWORK-RANGE>
```

Record the discovered IP addresses.

### Exercise 2: TCP Port Scanning

Perform a TCP SYN scan against the selected lab target.

```bash
sudo nmap -sS -p- <TARGET-IP>
```

Record open, closed, and filtered ports.

### Exercise 3: UDP Port Scanning

Perform a UDP scan against selected common ports.

```bash
sudo nmap -sU -p 53,67,123,161 <TARGET-IP>
```

Record the port states and any response details.

### Exercise 4: Service and Version Detection

Identify services and their versions.

```bash
nmap -sV -p <PORT-LIST> <TARGET-IP>
```

Document the detected service names and version information.

### Exercise 5: OS Detection

Perform operating system detection.

```bash
sudo nmap -O <TARGET-IP>
```

Record the estimated operating system and confidence level, if provided.

### Exercise 6: Save Scan Results

Save a normal text report:

```bash
nmap -sV -oN scanning-report.txt <TARGET-IP>
```

Save XML output:

```bash
nmap -sV -oX scanning-report.xml <TARGET-IP>
```

Save all standard output formats together:

```bash
nmap -sV -oA scanning-assessment <TARGET-IP>
```

Nmap creates output files that can be used for further analysis and reporting.

## 6. Traffic Analysis Using Wireshark

Capture the scanning traffic during the assessment.

Useful display filters:

**TCP traffic**

```text
tcp
```

**UDP traffic**

```text
udp
```

**ICMP traffic**

```text
icmp
```

**Traffic involving the target**

```text
ip.addr == <TARGET-IP>
```

Analyze packet responses and document any unusual behavior.

## 7. Technical Scanning Report Template

Prepare your final report using the following structure.

### A. Assessment Information

- Assessment title
- Assessment date
- Analyst name
- Target IP address
- Authorized scope
- Tools used

### B. Executive Summary

Write a short overview of the assessment, including the target environment, scanning activities, and major observations.

### C. Methodology

Describe the steps performed:

1. Host discovery
2. TCP port scanning
3. UDP port scanning
4. Service and version detection
5. OS fingerprinting
6. Firewall behavior analysis
7. Traffic analysis

### D. Host Discovery Results

| Host IP | Status | Observation |
|---|---|---|
| | | |

### E. Port Scanning Results

| Port | Protocol | State | Service |
|---|---|---|---|
| | | | |

### F. Service Detection Results

| Port | Service | Version | Observation |
|---|---|---|---|
| | | | |

### G. OS Detection Results

- Target IP:
- Estimated operating system:
- Detection confidence:
- Additional observations:

### H. Security Observations

Document exposed services, unexpected open ports, outdated software indicators, and firewall-related observations.

Do not automatically classify every open port as a vulnerability. Validate findings before assigning risk.

### I. Recommendations

Provide practical recommendations based on the observed results, such as:

- Disable unnecessary services.
- Restrict access to management ports.
- Review firewall configurations.
- Update outdated software.
- Monitor unusual network activity.
- Repeat assessments after remediation.

### J. Conclusion

Summarize the assessment results and identify recommended next steps.

## 8. Final Assessment Checklist

- [ ] Identified active hosts.
- [ ] Completed TCP port scanning.
- [ ] Completed selected UDP port scanning.
- [ ] Identified available services.
- [ ] Performed OS detection.
- [ ] Reviewed firewall behavior.
- [ ] Captured network traffic.
- [ ] Saved Nmap scan outputs.
- [ ] Prepared a technical scanning report.

## 9. Assessment Questions

1. What is the purpose of a network scanning assessment?
2. Why should host discovery be performed before port scanning?
3. What is the difference between TCP and UDP scanning?
4. What does service version detection identify?
5. Why can OS detection be inaccurate?
6. What is the purpose of Nmap output formats?
7. Why should open ports be validated before reporting security risks?
8. What information should a technical scanning report contain?

## 10. Learning Outcomes

After completing this lab, students will be able to:

- Perform a structured network scanning assessment.
- Identify active hosts and exposed ports.
- Detect services and estimate operating systems.
- Analyze network traffic using Wireshark.
- Save and interpret Nmap output files.
- Prepare a professional technical scanning report.
- Recommend basic security improvements based on findings.

## 11. Safety Guidelines

- Scan only systems within the approved assessment scope.
- Use isolated virtual machines for practical exercises.
- Do not scan public or third-party systems without explicit authorization.
- Do not perform destructive testing.
- Store assessment reports securely.
