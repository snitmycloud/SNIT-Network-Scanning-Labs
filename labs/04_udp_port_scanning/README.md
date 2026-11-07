# Lab 04: UDP Port Scanning

## 1. Lab Objective

Understand UDP scanning techniques and learn how to identify UDP services, interpret ICMP responses and analyze UDP port states using Nmap.

## 2. Topics Covered

- UDP Protocol Fundamentals
- TCP vs UDP
- UDP Header Structure
- Common UDP Services
- UDP Port Scanning (-sU)
- UDP Port States
- ICMP Destination Unreachable Messages
- Open vs Closed vs Open|Filtered
- UDP Scanning Limitations

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Netcat
- Metasploitable 2

## 4. UDP Scanning Concepts

UDP is a connectionless transport protocol. Unlike TCP, it does not establish a three-way handshake before sending data.

### Common UDP Services

| Port | Service |
|---|---|
| 53 | DNS |
| 67/68 | DHCP |
| 69 | TFTP |
| 123 | NTP |
| 161 | SNMP |
| 500 | IKE / IPsec |
| 514 | Syslog |

### UDP Port States

| Port State | Meaning |
|---|---|
| Open | A UDP application responded |
| Closed | An ICMP port unreachable response was received |
| Open|Filtered | No response was received, so Nmap cannot distinguish open from filtered |
| Filtered | Network filtering prevents reliable state determination |

## 5. Practical Exercises

### Exercise 1: Basic UDP Scan

```bash
sudo nmap -sU <TARGET-IP>
```

Observe the UDP port states.

### Exercise 2: Scan Specific UDP Ports

```bash
sudo nmap -sU -p 53,123,161 <TARGET-IP>
```

Identify the status of the selected ports.

### Exercise 3: Scan Common UDP Ports

```bash
sudo nmap -sU --top-ports 20 <TARGET-IP>
```

Observe which commonly used UDP ports respond.

### Exercise 4: UDP Service Detection

```bash
sudo nmap -sU -sV -p 53,123,161 <TARGET-IP>
```

Analyze the service information returned by Nmap.

**Note:** UDP scanning may take longer than TCP scanning because many UDP services do not respond to empty probes.

## 6. UDP Traffic Analysis Using Wireshark

1. Open Wireshark.
2. Select the isolated lab network interface.
3. Start packet capture.
4. Run an authorized UDP scan.
5. Apply this display filter:

```text
udp
```

6. Observe UDP request and response packets.

To inspect ICMP unreachable messages, use:

```text
icmp
```

Observe the relationship between UDP probes and ICMP responses.

## 7. UDP Response Interpretation

| Network Response | Nmap Interpretation |
|---|---|
| UDP application response | Open |
| ICMP Type 3, Code 3 | Closed |
| ICMP Type 3, Code 1, 2, 9, 10 or 13 | Filtered |
| No response | Open|Filtered |

## 8. Practical Assignment

Using the isolated lab environment:

1. Perform a UDP scan.
2. Scan selected UDP ports.
3. Identify UDP services.
4. Compare UDP and TCP scan results.
5. Capture UDP traffic using Wireshark.
6. Identify ICMP unreachable responses.
7. Prepare a UDP scanning report.

## 9. Assessment Questions

1. What is UDP?
2. How is UDP different from TCP?
3. Why is UDP scanning slower in many situations?
4. What does `-sU` do in Nmap?
5. What is the meaning of open|filtered?
6. What is an ICMP Destination Unreachable message?
7. What does ICMP Type 3 Code 3 indicate?
8. Why is Wireshark useful for UDP analysis?

## 10. Expected Learning Outcomes

After completing this lab, students should be able to:

- Explain UDP protocol fundamentals.
- Perform UDP port scanning with Nmap.
- Identify common UDP services.
- Interpret UDP port states.
- Analyze ICMP responses.
- Compare TCP and UDP scanning results.

**Lab Safety:** Perform all exercises only against isolated lab systems or explicitly authorized targets.
