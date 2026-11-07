# SNIT Network Scanning Labs – Troubleshooting Guide

This guide covers common issues encountered during Nmap and network scanning practicals.

## 1. Nmap Command Not Found

**Error:**
```text
nmap: command not found
```

**Solution:**

Install Nmap on Kali Linux:

```bash
sudo apt update
sudo apt install nmap -y
```

Verify installation:

```bash
nmap --version
```

## 2. Permission Denied During SYN Scan

**Error:** Insufficient privileges to perform a SYN scan.

**Solution:**

Run Nmap with administrator privileges:

```bash
sudo nmap -sS <TARGET-IP>
```

## 3. Host Appears Down

**Possible reasons:**

- Target VM is powered off.
- Kali and target VMs are on different networks.
- Firewall blocks discovery probes.
- Incorrect target IP address.

**Troubleshooting:**

Check your network configuration:

```bash
ip addr
```

Check connectivity:

```bash
ping <TARGET-IP>
```

Try a TCP-based discovery scan:

```bash
sudo nmap -sn -PS80,443 <TARGET-IP>
```

Note: A failed ping does not necessarily mean the target is offline.

## 4. All Ports Show as Filtered

**Possible reasons:**

- Firewall silently drops packets.
- Network security rules restrict traffic.
- Target is not reachable.

**Troubleshooting:**

Inspect firewall rules on your own lab target:

```bash
sudo ufw status verbose
```

Capture traffic in Wireshark and inspect whether probes receive responses.

## 5. UDP Scan Takes Too Long

**Possible reasons:**

- UDP services may not respond.
- Firewalls may silently drop UDP packets.
- Nmap waits for responses or retries.

**Solution:**

Start with a smaller selection of ports:

```bash
sudo nmap -sU -p 53,67,123,161 <TARGET-IP>
```

Remember that `open|filtered` means Nmap cannot distinguish between an open port and a filtered port.

## 6. OS Detection Fails

**Possible reasons:**

- Insufficient privileges.
- Firewall blocks required probes.
- Not enough information from the target.
- Network address translation or virtualization affects responses.

**Solution:**

Run OS detection with elevated privileges:

```bash
sudo nmap -O <TARGET-IP>
```

Nmap OS detection is an estimate, not a guaranteed identification.

## 7. Service Version Is Not Detected

**Possible reasons:**

- Service does not respond.
- Port is filtered.
- Service uses unusual behavior.
- Version information is hidden.

**Solution:**

Try service detection against selected ports:

```bash
nmap -sV -p 22,80,443 <TARGET-IP>
```

## 8. Wireshark Does Not Capture Traffic

**Possible reasons:**

- Incorrect network interface selected.
- Capture permissions are insufficient.
- Scan traffic uses another interface.
- Capture started after the scan.

**Solution:**

List available interfaces:

```bash
ip link show
```

Select the correct interface in Wireshark and start capturing before running Nmap.

## 9. Virtual Machines Cannot Communicate

**Possible reasons:**

- Incorrect virtual network mode.
- Different network segments.
- IP configuration problems.
- VM network adapter is disconnected.

**Troubleshooting:**

Check IP configuration on both VMs:

```bash
ip addr
```

Check routing:

```bash
ip route
```

Ensure both VMs are connected to the intended isolated virtual network.

## 10. Nmap Output Files Are Missing

**Possible reason:**

The output option was not specified, or the file was saved in another directory.

**Solution:**

Save output explicitly:

```bash
nmap -sV -oN scanning-report.txt <TARGET-IP>
```

Check your current directory:

```bash
pwd
ls -l
```

## 11. General Troubleshooting Checklist

- [ ] Confirm the target VM is running.
- [ ] Verify the target IP address.
- [ ] Check network connectivity.
- [ ] Confirm the correct network interface.
- [ ] Verify firewall configuration.
- [ ] Use appropriate privileges.
- [ ] Start Wireshark before scanning.
- [ ] Check Nmap command syntax.
- [ ] Save and review scan output.

## Important Safety Notice

Troubleshoot only systems within your authorized lab environment. Do not disable security controls on production or third-party systems.

---

**SNIT Training Institute | Network Scanning Practical Support**
