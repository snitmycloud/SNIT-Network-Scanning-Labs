# Lab 02: Nmap Fundamentals & Target Specification

## 1. Lab Objective

Understand Nmap architecture, scanning methodology, target specification and commonly used scan options for authorized network assessments.

## 2. Topics Covered

- Introduction to Nmap
- How Nmap Performs Scanning
- Nmap Scan Workflow
- Target Specification
- Single Host and Multiple Host Scanning
- Network Range Specification
- Common Nmap Scan Options
- Nmap Output Formats
- Understanding Scan Results

## 3. Tools Required

- Kali Linux
- Nmap
- Zenmap (optional)
- Metasploitable 2
- Wireshark

## 4. Nmap Installation and Verification

Check Nmap version:

```bash
nmap --version
```

Display help:

```bash
nmap --help
```

Display detailed manual:

```bash
man nmap
```

## 5. Target Specification

### Exercise 1: Scan a Single Host

```bash
nmap <TARGET-IP>
```

### Exercise 2: Scan Multiple Hosts

```bash
nmap <TARGET-IP-1> <TARGET-IP-2>
```

### Exercise 3: Scan an IP Range

```bash
nmap <START-IP>-<END-IP>
```

### Exercise 4: Scan a Subnet

```bash
nmap <LAB-NETWORK-RANGE>
```

### Exercise 5: Exclude a Specific Host

```bash
nmap <LAB-NETWORK-RANGE> --exclude <EXCLUDED-IP>
```

## 6. Common Nmap Scan Options

| Option | Description |
|---|---|
| `-sn` | Host discovery without port scanning |
| `-sS` | TCP SYN scan |
| `-sT` | TCP Connect scan |
| `-sU` | UDP scan |
| `-sV` | Service and version detection |
| `-O` | Operating system detection |
| `-p` | Specify ports |
| `-F` | Fast scan of common ports |
| `-Pn` | Skip host discovery |
| `-n` | Disable DNS resolution |
| `-v` | Increase output verbosity |
| `-oN` | Save normal output |
| `-oX` | Save XML output |

## 7. Practical Exercises

### Exercise 1: Basic Nmap Scan

```bash
nmap <TARGET-IP>
```

Observe the discovered ports and services.

### Exercise 2: Fast Port Scan

```bash
nmap -F <TARGET-IP>
```

Compare the results with the default scan.

### Exercise 3: Scan Specific Ports

```bash
nmap -p 22,80,443 <TARGET-IP>
```

Identify the status of each selected port.

### Exercise 4: Disable DNS Resolution

```bash
nmap -n <TARGET-IP>
```

Observe the difference in output.

### Exercise 5: Save Scan Results

```bash
nmap -oN scan_results.txt <TARGET-IP>
```

Open the generated text file and review the results.

### Exercise 6: Generate XML Output

```bash
nmap -oX scan_results.xml <TARGET-IP>
```

Understand how XML output can support automated reporting.

## 8. Understanding Nmap Output

Students should identify:

- Target IP address
- Host status
- Port number
- Protocol
- Port state
- Service name
- Scan duration

## 9. Practical Assignment

Perform the following activities against the assigned vulnerable lab machine:

1. Perform a default Nmap scan.
2. Perform a fast scan.
3. Scan selected ports.
4. Compare scan results.
5. Save normal and XML outputs.
6. Document the differences.

## 10. Assessment Questions

1. What is Nmap?
2. How does Nmap identify open ports?
3. What is target specification?
4. What is the difference between `-sn` and `-Pn`?
5. What is the purpose of `-sV`?
6. What is the difference between `-oN` and `-oX`?
7. Why would a security professional disable DNS resolution during a scan?

## 11. Expected Learning Outcomes

After completing this lab, students should be able to:

- Explain Nmap scanning methodology.
- Specify individual hosts and network ranges.
- Select appropriate Nmap scan options.
- Interpret basic scan results.
- Save and analyze Nmap output files.

**Lab Safety:** Perform scanning exercises only against authorized targets and isolated lab systems.
