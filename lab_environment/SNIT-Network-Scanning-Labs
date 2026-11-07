# SNIT Network Scanning Lab Environment Setup

## 1. Objective

Build an isolated virtual lab environment for practicing network scanning, Nmap operations, service detection, and network traffic analysis.

## 2. Lab Architecture

The lab consists of two virtual machines connected through an isolated Host-Only Network.

| Virtual Machine | Purpose | Operating System |
|---|---|---|
| VM 1 | Attacker / Scanner | Kali Linux |
| VM 2 | Vulnerable Target | Metasploitable 2 |

## 3. Required Software

- Oracle VirtualBox or VMware Workstation
- Kali Linux ISO
- Metasploitable 2 virtual machine
- Nmap
- Wireshark
- Netcat

## 4. Virtual Machine Configuration

### VM 1: Kali Linux

Recommended lab configuration:

| Component | Recommended Configuration |
|---|---|
| RAM | 4 GB |
| CPU | 2 cores |
| Storage | 40 GB |
| Network Adapter | Host-Only Adapter |

### VM 2: Metasploitable 2

Recommended lab configuration:

| Component | Recommended Configuration |
|---|---|
| RAM | 1 GB |
| CPU | 1 core |
| Storage | 10 GB |
| Network Adapter | Host-Only Adapter |

These are suggested lab settings. Adjust them according to your computer's available resources.

## 5. Configure an Isolated Network

In VirtualBox:

1. Open VirtualBox.
2. Go to Tools → Network.
3. Open the Host-only Networks section.
4. Create a Host-Only Network.
5. Enable its DHCP server if you want automatic IP assignment.
6. Connect both virtual machines to the same Host-Only Network.

For each VM:

1. Open Settings.
2. Select Network.
3. Choose Adapter 1.
4. Enable Network Adapter.
5. Select Host-Only Adapter.
6. Choose the same Host-Only Network for both VMs.

**Important:** Do not connect the vulnerable Metasploitable VM to a Bridged Adapter or expose it to a public network.

## 6. Verify Kali Linux Network Configuration

Start Kali Linux and open a terminal.

Check its IP address:

```bash
ip addr
```

Check its routing table:

```bash
ip route
```

Identify the Host-Only Network interface and record its IP address.

## 7. Verify Metasploitable 2 Network Configuration

Start Metasploitable 2 and log in using its default lab credentials.

Default credentials:

- Username: `msfadmin`
- Password: `msfadmin`

Check its IP address:

```bash
ifconfig
```

Record the IP address assigned to the Host-Only Network.

## 8. Test Connectivity Between VMs

From Kali Linux, ping the Metasploitable 2 IP address:

```bash
ping <TARGET-IP>
```

If connectivity is working, you should receive replies.

Stop the ping using:

```text
Ctrl + C
```

A failed ping does not always indicate that the target is offline. Check the network configuration and firewall behavior.

## 9. Verify the Target Using Nmap

From Kali Linux:

```bash
nmap -sn <TARGET-IP>
```

Perform a basic port scan:

```bash
nmap -sS -p 1-1000 <TARGET-IP>
```

Observe the discovered ports and record the results.

## 10. Install Required Tools in Kali Linux

Update the package list:

```bash
sudo apt update
```

Install Nmap:

```bash
sudo apt install nmap -y
```

Install Wireshark:

```bash
sudo apt install wireshark -y
```

Install Netcat:

```bash
sudo apt install netcat-openbsd -y
```

Verify installations:

```bash
nmap --version
wireshark --version
nc -h
```

## 11. Take Virtual Machine Snapshots

Before beginning practical exercises:

1. Shut down each VM.
2. Open its Snapshots section in VirtualBox.
3. Take a snapshot.
4. Name it `Clean-Lab-Setup`.

Snapshots help restore the lab to its original state after configuration changes.

## 12. Lab Environment Verification Checklist

- [ ] VirtualBox or VMware installed.
- [ ] Kali Linux installed.
- [ ] Metasploitable 2 installed.
- [ ] Both VMs connected to the same Host-Only Network.
- [ ] Kali IP address recorded.
- [ ] Metasploitable IP address recorded.
- [ ] VM connectivity tested.
- [ ] Nmap installed and verified.
- [ ] Wireshark installed and verified.
- [ ] Netcat installed and verified.
- [ ] Initial VM snapshots created.

## 13. Safety Guidelines

- Use Metasploitable 2 only as an isolated vulnerable target.
- Never expose Metasploitable 2 to a public or production network.
- Do not use Bridged Networking for the vulnerable target.
- Perform scanning exercises only within your authorized lab network.
- Keep the vulnerable VM powered off when it is not being used.

---

**SNIT Training Institute | Network Scanning Lab Environment**
