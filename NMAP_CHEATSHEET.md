# SNIT Network Scanning Labs – Nmap Cheat Sheet

A quick reference guide for commonly used Nmap commands in authorized network scanning labs.

## 1. Nmap Installation and Verification

```bash
sudo apt update
sudo apt install nmap -y
nmap --version
```

## 2. Target Specification

| Command | Description |
|---|---|
| `nmap 192.168.56.20` | Scan a single host |
| `nmap 192.168.56.10 192.168.56.20` | Scan multiple hosts |
| `nmap 192.168.56.0/24` | Scan an authorized network range |
| `nmap -iL targets.txt` | Scan targets listed in a file |

## 3. Host Discovery

| Command | Description |
|---|---|
| `nmap -sn <TARGET-IP>` | Host discovery without port scanning |
| `nmap -sn <LAB-NETWORK-RANGE>` | Discover active hosts in a lab network |
| `nmap -sn -PE <TARGET-IP>` | ICMP Echo discovery |
| `sudo nmap -sn -PR <TARGET-IP>` | ARP discovery on a local network |
| `sudo nmap -sn -PS80,443 <TARGET-IP>` | TCP SYN-based discovery |

## 4. TCP Port Scanning

| Command | Description |
|---|---|
| `sudo nmap -sS <TARGET-IP>` | TCP SYN scan |
| `nmap -sT <TARGET-IP>` | TCP Connect scan |
| `nmap -p 80 <TARGET-IP>` | Scan port 80 |
| `nmap -p 22,80,443 <TARGET-IP>` | Scan selected ports |
| `nmap -p 1-1000 <TARGET-IP>` | Scan ports 1 to 1000 |
| `nmap -p- <TARGET-IP>` | Scan all TCP ports |

## 5. UDP Port Scanning

| Command | Description |
|---|---|
| `sudo nmap -sU <TARGET-IP>` | UDP scan |
| `sudo nmap -sU -p 53 <TARGET-IP>` | Scan UDP port 53 |
| `sudo nmap -sU -p 53,67,123,161 <TARGET-IP>` | Scan selected UDP ports |

**Note:** UDP scans can be slower because many UDP services do not respond to probes. `open|filtered` does not confirm that a port is open.

## 6. Service and Version Detection

| Command | Description |
|---|---|
| `nmap -sV <TARGET-IP>` | Detect service versions |
| `nmap -sV -p 22,80,443 <TARGET-IP>` | Detect versions on selected ports |
| `nmap -sV --version-light <TARGET-IP>` | Use lighter version detection |

## 7. OS Detection

| Command | Description |
|---|---|
| `sudo nmap -O <TARGET-IP>` | OS detection |
| `sudo nmap -sV -O <TARGET-IP>` | Service and OS detection |
| `sudo nmap -A <TARGET-IP>` | Enable aggressive detection features |

Use `-A` only on authorized lab targets. It enables multiple detection techniques and generates additional traffic.

## 8. Scan Timing

| Option | Description |
|---|---|
| `-T0` | Very slow timing |
| `-T1` | Slow timing |
| `-T2` | Reduced timing |
| `-T3` | Normal timing |
| `-T4` | Faster timing |
| `-T5` | Very aggressive timing |

Example:

```bash
nmap -T3 -p 1-100 <TARGET-IP>
```

Timing options affect scan speed and network traffic. Faster is not automatically better.

## 9. Firewall and Port State Analysis

| State | Meaning |
|---|---|
| Open | A service accepts connections |
| Closed | Host responds, but no service listens on the port |
| Filtered | Filtering prevents Nmap from determining the port state |
| Unfiltered | Port is accessible, but Nmap cannot determine whether it is open |
| Open\|Filtered | Nmap cannot distinguish between open and filtered |

## 10. Saving Scan Results

| Command | Description |
|---|---|
| `nmap -oN report.txt <TARGET-IP>` | Normal text output |
| `nmap -oX report.xml <TARGET-IP>` | XML output |
| `nmap -oG report.gnmap <TARGET-IP>` | Grepable output |
| `nmap -oA assessment <TARGET-IP>` | Save multiple output formats |

## 11. Useful Supporting Commands

**Check Kali IP address:**

```bash
ip addr
```

**Check routing table:**

```bash
ip route
```

**Test connectivity:**

```bash
ping <TARGET-IP>
```

**Check listening ports on your own Linux VM:**

```bash
ss -tulnp
```

**Capture packets:**

```bash
sudo wireshark
```

## 12. Important Safety Guidelines

- Scan only systems you own or have explicit authorization to test.
- Use isolated virtual machines for training.
- Never scan third-party networks without permission.
- Document scan scope and results.
- Avoid destructive testing.

---

**SNIT Training Institute | Nmap Command Reference**
