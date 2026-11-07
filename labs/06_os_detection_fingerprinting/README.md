# Lab 06: OS Detection & Fingerprinting

## 1. Objective

Learn how to identify a target system's operating system using Nmap OS detection and understand how network responses help estimate the target platform.

## 2. Topics Covered

- What is OS fingerprinting?
- Active OS detection
- TCP/IP stack fingerprinting
- Nmap OS detection
- Operating system accuracy and limitations
- Understanding OS detection results

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Authorized lab target (Metasploitable or another intentionally vulnerable VM)

## 4. Understanding OS Fingerprinting

OS fingerprinting is the process of identifying a system's operating system by examining its network behavior and responses.

Nmap analyzes characteristics such as:

- TCP response behavior
- TCP window sizes
- IP ID patterns
- TCP options
- Network stack responses

Nmap uses these characteristics to compare the target's responses against known OS fingerprints.

## 5. Practical Exercises

### Exercise 1: Basic OS Detection

Run the following command against your authorized lab target:

```bash
sudo nmap -O <TARGET-IP>
```

Observe the output and identify:

- Detected operating system
- OS details
- Detection confidence
- Network distance, if available

### Exercise 2: OS Detection with Service Scanning

```bash
sudo nmap -sV -O <TARGET-IP>
```

Compare the service detection results with the OS detection results.

### Exercise 3: Aggressive Detection

```bash
sudo nmap -A <TARGET-IP>
```

Observe the additional information returned by Nmap, including:

- OS detection
- Service and version detection
- Default script results
- Traceroute information, when available

Use this option only against your isolated lab target. It enables multiple detection techniques, so it generates more network traffic.

## 6. Wireshark Traffic Analysis

Start Wireshark and capture traffic while performing OS detection.

Useful display filters:

```text
tcp
```

```text
icmp
```

```text
ip.addr == <TARGET-IP>
```

Observe TCP flags, packet responses, and other characteristics that help Nmap identify the operating system.

## 7. Result Interpretation

Document the following:

| Observation | Your Result |
|---|---|
| Target IP | |
| Detected OS | |
| OS confidence | |
| Open ports | |
| Detected services | |
| Network distance | |
| Additional observations | |

**Important:** OS detection is an estimate, not a guarantee. Firewalls, NAT, virtualization, missing responses, and unusual network configurations can affect accuracy. Nmap may need at least one open and one closed TCP port to identify an OS reliably.

## 8. Lab Assignment

1. Perform OS detection on your authorized lab VM.
2. Run OS detection with and without service detection.
3. Compare the results of `-O` and `-A`.
4. Capture the scanning traffic using Wireshark.
5. Prepare a short OS fingerprinting report.

## 9. Assessment Questions

1. What is OS fingerprinting?
2. How does Nmap identify an operating system?
3. What is the purpose of the `-O` option?
4. What additional information does `-A` provide?
5. Why can OS detection produce inaccurate results?
6. How can firewalls affect OS fingerprinting?

## 10. Learning Outcomes

After completing this lab, students will be able to:

- Explain OS fingerprinting concepts.
- Perform OS detection using Nmap.
- Interpret operating system detection results.
- Analyze scanning traffic using Wireshark.
- Document OS fingerprinting findings.

## 11. Safety Guidelines

- Perform scanning only in an isolated lab environment or against systems for which explicit authorization has been granted.
- Do not scan public IP addresses or third-party networks without permission.
- Use intentionally vulnerable virtual machines for practical exercises.
