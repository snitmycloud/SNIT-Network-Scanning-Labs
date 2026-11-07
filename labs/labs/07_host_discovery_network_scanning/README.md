# Lab 07: Host Discovery & Network Scanning

## 1. Objective

Learn how to discover active hosts on a network, identify reachable systems, and perform basic network-wide scanning using Nmap.

## 2. Topics Covered

- Host discovery concepts
- Live host identification
- ICMP-based discovery
- TCP-based host discovery
- ARP discovery on local networks
- Network range scanning
- Identifying active and inactive hosts
- Understanding host discovery limitations

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Two or more authorized lab VMs
- Isolated virtual network

## 4. Understanding Host Discovery

Host discovery identifies which systems are reachable within a specified network.

Before scanning ports, security professionals often perform host discovery to understand which devices are active.

Common discovery techniques include:

- ICMP Echo Requests
- TCP SYN probes
- TCP ACK probes
- ARP requests on local Ethernet networks

A host may be active even when it does not respond to a particular discovery probe. Firewalls and network configurations can block discovery traffic.

## 5. Practical Exercises

### Exercise 1: Discover a Single Host

```bash
nmap -sn <TARGET-IP>
```

Observe whether Nmap reports the target as up or down.

### Exercise 2: Discover Hosts in an Authorized Lab Network

```bash
nmap -sn <LAB-NETWORK-RANGE>
```

Example format:

```bash
nmap -sn 192.168.56.0/24
```

Replace the example range with your actual isolated lab network.

Record the IP addresses of discovered hosts.

### Exercise 3: ICMP Echo Discovery

```bash
nmap -sn -PE <TARGET-IP>
```

This requests ICMP Echo responses as part of host discovery.

### Exercise 4: TCP SYN-Based Discovery

```bash
sudo nmap -sn -PS80,443 <TARGET-IP>
```

Observe how Nmap uses TCP SYN probes to check whether the target is reachable.

### Exercise 5: TCP ACK-Based Discovery

```bash
sudo nmap -sn -PA80,443 <TARGET-IP>
```

Compare the results with the TCP SYN-based discovery exercise.

### Exercise 6: Local Network ARP Discovery

For a target on the same local Ethernet network:

```bash
sudo nmap -sn -PR <LAB-NETWORK-RANGE>
```

Observe the ARP requests and replies in Wireshark.

## 6. Wireshark Traffic Analysis

Start Wireshark before running the discovery commands.

Useful display filters:

**ICMP traffic**

```text
icmp
```

**ARP traffic**

```text
arp
```

**TCP SYN packets**

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

**Traffic involving the target**

```text
ip.addr == <TARGET-IP>
```

Observe the request and response patterns for each discovery method.

## 7. Result Documentation

| Observation | Your Result |
|---|---|
| Lab network range | |
| Total hosts discovered | |
| Active host IP addresses | |
| ICMP response observed | |
| TCP response observed | |
| ARP response observed | |
| Discovery method with best results | |

## 8. Lab Assignment

1. Identify your isolated lab network range.
2. Discover active hosts using `-sn`.
3. Compare ICMP, TCP SYN, TCP ACK, and ARP discovery.
4. Capture the traffic using Wireshark.
5. Prepare a host discovery report containing discovered IP addresses and observations.

## 9. Assessment Questions

1. What is host discovery?
2. Why is host discovery performed before port scanning?
3. What is the purpose of Nmap's `-sn` option?
4. How does ICMP-based discovery work?
5. What is the difference between TCP SYN and TCP ACK discovery?
6. Why is ARP discovery useful on a local network?
7. Can a firewall cause an active host to appear down?

## 10. Learning Outcomes

After completing this lab, students will be able to:

- Explain host discovery techniques.
- Identify active hosts in an authorized lab network.
- Use Nmap discovery options.
- Compare ICMP, TCP, and ARP discovery.
- Analyze network discovery traffic using Wireshark.
- Document host discovery results.

## 11. Safety Guidelines

- Scan only isolated lab networks or networks for which explicit authorization has been granted.
- Never scan third-party networks without permission.
- Use private lab IP ranges and intentionally configured virtual machines for practical exercises.
