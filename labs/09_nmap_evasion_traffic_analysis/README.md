# Lab 09: Nmap Evasion Concepts & Traffic Analysis

## 1. Objective

Understand Nmap scan traffic characteristics, packet manipulation concepts, and how network security tools identify unusual scanning patterns.

## 2. Topics Covered

- Network scanning signatures
- Nmap timing and performance options
- Packet fragmentation concepts
- Decoy scanning concepts
- Source address and packet manipulation
- IDS monitoring and detection
- Wireshark packet analysis
- Firewall and IDS logging

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Isolated lab target VM
- IDS tool (optional)

## 4. Understanding Scan Detection

Network security monitoring tools can identify scanning activity through patterns such as:

- Repeated connection attempts
- Sequential port probing
- Connections to many ports in a short period
- Unusual packet patterns
- Repeated unsuccessful connection attempts

Security professionals study these patterns to understand how scanning is detected and how to improve defensive monitoring.

## 5. Practical Exercises

### Exercise 1: Compare Nmap Timing Profiles

Run a normal scan against your authorized lab target:

```bash
nmap -sS -p 1-100 <TARGET-IP>
```

Now compare it with a slower timing profile:

```bash
nmap -sS -T2 -p 1-100 <TARGET-IP>
```

Observe:

- Scan completion time
- Number of packets generated
- Connection patterns
- Differences in traffic volume

Use only your isolated lab target.

### Exercise 2: Understand Packet Fragmentation

Study how IP fragmentation divides a large IP packet into smaller fragments.

In Wireshark, inspect:

- IP identification field
- Fragment offset
- More Fragments flag
- Reassembled packets

Useful Wireshark display filter:

```text
ip.flags.mf == 1 || ip.frag_offset > 0
```

Document the fragmentation behavior observed in your lab traffic.

### Exercise 3: Understand Decoy Scanning

Study the purpose of Nmap's decoy scanning concept.

Discuss:

- Why source attribution can become difficult
- How decoy traffic may appear in network logs
- Why decoys do not guarantee anonymity
- How defenders correlate traffic using timestamps and network telemetry

Do not use decoy scanning against public or third-party systems.

### Exercise 4: Observe IDS Detection

If an IDS is available in your lab, perform a basic authorized scan and review its alerts.

Record:

- Alert name
- Source IP
- Destination IP
- Detection timestamp
- Detected scanning behavior
- Severity level

### Exercise 5: Analyze Scanning Traffic

Capture traffic in Wireshark during your Nmap exercises.

Useful display filters:

**SYN packets**

```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

**TCP reset packets**

```text
tcp.flags.reset == 1
```

**IP fragments**

```text
ip.flags.mf == 1 || ip.frag_offset > 0
```

**Traffic involving the target**

```text
ip.addr == <TARGET-IP>
```

## 6. Result Documentation

| Observation | Your Result |
|---|---|
| Target IP | |
| Timing profile tested | |
| Scan completion time | |
| Packet count | |
| Fragmentation observed | |
| IDS alert generated | |
| Detection behavior | |
| Key findings | |

## 7. Lab Assignment

1. Compare two Nmap timing profiles.
2. Capture both scans using Wireshark.
3. Compare packet patterns and scan duration.
4. Study IP fragmentation fields.
5. Explain decoy scanning and its limitations.
6. Review IDS alerts if an IDS is available.
7. Prepare a short traffic analysis report.

## 8. Assessment Questions

1. What is a network scanning signature?
2. How do Nmap timing profiles affect scan behavior?
3. What is IP fragmentation?
4. What are decoy scans?
5. Why do decoys not guarantee anonymity?
6. How can IDS tools identify port scanning?
7. How can Wireshark help investigate scanning activity?

## 9. Learning Outcomes

After completing this lab, students will be able to:

- Explain common scanning patterns.
- Compare Nmap timing profiles.
- Understand IP fragmentation.
- Explain decoy scanning concepts and limitations.
- Analyze scanning traffic using Wireshark.
- Interpret basic IDS alerts.
- Document network security observations.

## 10. Safety Guidelines

- Perform practical exercises only in an isolated lab environment.
- Do not use evasion techniques against third-party systems.
- Do not attempt to bypass production IDS or firewall controls.
- Use controlled traffic captures for packet analysis.
- Follow written authorization and approved testing scope.
