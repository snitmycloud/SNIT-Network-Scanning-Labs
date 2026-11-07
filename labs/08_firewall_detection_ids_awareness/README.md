# Lab 08: Firewall Detection & IDS Awareness

## 1. Objective

Understand how firewalls and Intrusion Detection Systems (IDS) affect network scanning, and learn to interpret filtered ports and network responses using Nmap and Wireshark.

## 2. Topics Covered

- Firewall fundamentals
- Packet filtering concepts
- Stateful and stateless firewalls
- Intrusion Detection Systems (IDS)
- Intrusion Prevention Systems (IPS)
- Open, closed, and filtered port states
- Nmap firewall detection
- Network traffic analysis

## 3. Tools Required

- Kali Linux
- Nmap
- Wireshark
- Linux firewall (UFW or iptables)
- Isolated lab target VM

## 4. Understanding Firewalls and IDS

**Firewall:** A security control that monitors and filters network traffic based on configured rules.

**IDS:** Monitors network activity and generates alerts when suspicious behavior is detected.

**IPS:** Monitors network activity and can actively block suspicious traffic.

Common firewall behaviors include:

- Allowing traffic
- Rejecting traffic
- Silently dropping packets
- Allowing traffic only from specific sources

## 5. Practical Exercises

### Exercise 1: Perform a Baseline Scan

Scan your authorized lab target before changing firewall rules.

```bash
nmap -sS -p 22,80,443 <TARGET-IP>
```

Record the port states.

### Exercise 2: Inspect Firewall Rules

On your own Linux lab target:

```bash
sudo ufw status verbose
```

If UFW is installed, inspect its configured rules.

For systems using iptables:

```bash
sudo iptables -L -n -v
```

### Exercise 3: Configure a Lab Firewall Rule

On your own Ubuntu lab target, block incoming connections to a test port.

```bash
sudo ufw deny 8080/tcp
```

Check the updated rules:

```bash
sudo ufw status numbered
```

Scan the test port from your Kali VM:

```bash
nmap -sS -p 8080 <TARGET-IP>
```

Compare the result with the baseline scan.

### Exercise 4: Remove the Test Rule

After completing the exercise, remove the rule you created.

```bash
sudo ufw status numbered
```

Identify the exact rule number, then remove it:

```bash
sudo ufw delete <RULE-NUMBER>
```

Verify the updated firewall status.

### Exercise 5: Compare Port States

Run a scan against your lab target:

```bash
nmap -sS -p 22,80,443,8080 <TARGET-IP>
```

Understand these possible results:

| Port State | Meaning |
|---|---|
| Open | A service is accepting connections |
| Closed | The host is reachable, but no service is listening |
| Filtered | Nmap cannot determine whether the port is open because traffic is filtered or responses are unavailable |
| Open\|Filtered | Nmap cannot distinguish between an open port and packet filtering |

## 6. Wireshark Traffic Analysis

Capture traffic while performing the scans.

Useful display filters:

**TCP traffic**

```text
tcp
```

**TCP reset packets**

```text
tcp.flags.reset == 1
```

**TCP SYN packets**

```text
tcp.flags.syn == 1
```

**ICMP traffic**

```text
icmp
```

Observe whether packets receive responses, are rejected, or appear to be silently dropped.

## 7. IDS Awareness

In this exercise, discuss how an IDS may detect scanning activity.

Common indicators include:

- Repeated connection attempts
- Connections to multiple ports
- Unusual connection patterns
- Repeated failed connection attempts
- High-volume probing

If an IDS is available in your lab, review its alerts while performing the authorized scans.

## 8. Result Documentation

| Observation | Your Result |
|---|---|
| Target IP | |
| Firewall enabled | |
| Ports tested | |
| Baseline port states | |
| Port states after firewall rule | |
| Packets observed in Wireshark | |
| IDS alerts generated | |
| Key findings | |

## 9. Lab Assignment

1. Perform a baseline scan against your lab VM.
2. Inspect the target's firewall rules.
3. Create a temporary firewall rule.
4. Compare port states before and after the rule.
5. Capture the traffic using Wireshark.
6. Review IDS alerts if an IDS is available.
7. Remove the temporary rule and document the results.

## 10. Assessment Questions

1. What is the purpose of a firewall?
2. What is the difference between IDS and IPS?
3. What does the filtered port state indicate?
4. What is the difference between dropping and rejecting packets?
5. How can firewall rules affect Nmap scan results?
6. What network activities may trigger IDS alerts?
7. Why should baseline scan results be recorded?

## 11. Learning Outcomes

After completing this lab, students will be able to:

- Explain firewall, IDS, and IPS concepts.
- Understand how firewall rules affect scanning.
- Interpret Nmap port states.
- Analyze packet behavior using Wireshark.
- Identify basic indicators of network scanning.
- Document firewall-related scanning observations.

## 12. Safety Guidelines

- Perform all configuration changes on your own isolated lab VM.
- Do not modify production firewall rules.
- Do not attempt to bypass third-party security controls.
- Restore firewall settings after completing the exercise.
