# Lab 01: Scanning Fundamentals & Host Discovery

## 1. Lab Objective

Understand network scanning fundamentals and learn how to identify active hosts in an authorized network using Nmap.

## 2. Topics Covered

- Introduction to Network Scanning
- Objectives of Network Scanning
- Active vs Passive Scanning
- Host Discovery
- IP Address and Network Range Identification
- ICMP and TCP-Based Discovery
- Understanding Nmap Scan Results

## 3. Lab Environment

| Component | Configuration |
|---|---|
| Attacker Machine | Kali Linux |
| Target Machine | Metasploitable 2 |
| Virtualization | VirtualBox / VMware |
| Network Mode | Host-Only / Internal Network |
| Scanning Tool | Nmap |

**Important:** Keep the vulnerable target inside an isolated virtual network.

## 4. Practical Exercises

### Exercise 1: Verify Network Configuration

```bash
ip addr
```

Identify the Kali Linux IP address and network interface.

### Exercise 2: Check Network Connectivity

```bash
ping -c 4 <TARGET-IP>
```

Observe whether the target responds to ICMP requests.

### Exercise 3: Perform Host Discovery

```bash
nmap -sn <TARGET-IP>
```

Identify whether the target host is reachable.

### Exercise 4: Discover Hosts in the Lab Network

```bash
nmap -sn <LAB-NETWORK-RANGE>
```

Use only the IP range assigned to your isolated lab.

### Exercise 5: Analyze Scan Results

Identify:
- Discovered IP addresses
- Number of active hosts
- Host response status
- Network range scanned
- Scan duration

## 5. Understanding the Results

| Result | Meaning |
|---|---|
| Host is up | Nmap considers the host reachable |
| Host is down | No qualifying response was received |
| Latency | Observed response time |
| Hosts scanned | Number of target addresses examined |

A host may be active even when it does not respond to a particular discovery probe. Firewall rules and network configuration can affect results.

## 6. Expected Learning Outcomes

After completing this lab, students should be able to:

- Explain network scanning fundamentals.
- Identify their lab network configuration.
- Use Nmap host discovery.
- Discover active hosts in an authorized network.
- Interpret basic Nmap output.

## 7. Lab Assessment

1. What is network scanning?
2. What is the purpose of host discovery?
3. What does `-sn` do in Nmap?
4. Why might a live host appear down?
5. What is the difference between host discovery and port scanning?

## 8. Practical Submission

Students must submit:

- Screenshot of Kali network configuration.
- Nmap host discovery command.
- Nmap scan output.
- Short explanation of discovered hosts.

**Lab Safety:** Perform all exercises only on your isolated lab network or explicitly authorized targets.
