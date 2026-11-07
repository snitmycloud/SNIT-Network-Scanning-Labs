# Lab 05: Service & Version Detection

## 1. Lab Objective

Learn how to identify services running on open ports, detect application versions, understand service fingerprinting and validate scan results using network tools.

## 2. Topics Covered

- Introduction to Service Enumeration
- Service Identification
- Service and Version Detection
- Nmap Service Fingerprinting
- Banner Grabbing
- Port-to-Service Mapping
- Service Detection Accuracy and Limitations
- Manual Service Verification
- Nmap Output Analysis

## 3. Tools Required

- Kali Linux
- Nmap
- Netcat
- Wireshark
- Metasploitable 2

## 4. Understanding Service Detection

Port scanning identifies accessible ports. Service detection attempts to determine which application is listening on those ports.

Examples:

| Port | Common Service |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |

Port numbers are conventional assignments. A service may run on a different port, so identification should not rely on port numbers alone.

## 5. Practical Exercises

### Exercise 1: Basic Service Detection

```bash
nmap -sV <TARGET-IP>
```

Observe the service names and version information.

### Exercise 2: Detect Services on Specific Ports

```bash
nmap -sV -p 21,22,80,443 <TARGET-IP>
```

Identify which services are running.

### Exercise 3: Perform Detailed Service Detection

```bash
nmap -sV --version-light <TARGET-IP>
```

Compare the results with a normal service detection scan.

### Exercise 4: Service Detection with Default Port Scan

```bash
nmap -sV -sS <TARGET-IP>
```

Observe how Nmap combines TCP SYN scanning and service identification.

### Exercise 5: Save Service Detection Results

```bash
nmap -sV -oN service_results.txt <TARGET-IP>
```

Review the generated output file.

## 6. Banner Grabbing Using Netcat

Connect to an authorized lab service:

```bash
nc -nv <TARGET-IP> 22
```

Observe whether the service provides a banner.

For an HTTP service:

```bash
curl -I http://<TARGET-IP>
```

Compare the manually collected information with Nmap results.

## 7. Wireshark Traffic Analysis

1. Open Wireshark.
2. Start packet capture on the isolated lab interface.
3. Execute an Nmap service detection scan.
4. Apply the following display filter:

```text
tcp
```

5. Observe connection requests and service responses.
6. Analyze how service identification probes interact with target services.

## 8. Understanding Nmap Results

| Result | Meaning |
|---|---|
| Service | Identified application or protocol |
| Version | Detected application version |
| Product | Application or software name |
| Extra Info | Additional fingerprint information |
| CPE | Common Platform Enumeration identifier |

Service fingerprints are estimates. Verify important findings through additional evidence.

## 9. Practical Assignment

Using the isolated vulnerable lab machine:

1. Perform service detection.
2. Identify at least five running services, if available.
3. Record their ports and detected versions.
4. Perform manual banner verification.
5. Compare Nmap and Netcat results.
6. Capture relevant packets using Wireshark.
7. Prepare a service enumeration report.

## 10. Assessment Questions

1. What is service detection?
2. What is the purpose of Nmap `-sV`?
3. What is service fingerprinting?
4. What is banner grabbing?
5. How does Netcat help identify services?
6. Why might service version detection be inaccurate?
7. What is a CPE identifier?
8. Why should service versions be verified before reporting vulnerabilities?

## 11. Expected Learning Outcomes

After completing this lab, students should be able to:

- Identify running network services.
- Perform service and version detection.
- Understand banner grabbing.
- Validate service information using Netcat.
- Analyze scanning traffic using Wireshark.
- Document service enumeration findings.

**Lab Safety:** Perform service identification only against isolated lab systems or explicitly authorized targets.
