# SNIT Network Scanning Lab – Network Topology

## 1. Lab Architecture

The lab uses an isolated Host-Only Network to connect Kali Linux and Metasploitable 2.

## 2. Network Diagram

```text
             HOST COMPUTER
          VirtualBox / VMware
                   |
          Host-Only Network
             192.168.56.0/24
                   |
          +--------+--------+
          |                 |
     KALI LINUX        METASPLOITABLE 2
     Attacker VM        Vulnerable Target
     192.168.56.10      192.168.56.20
          |                 |
     Nmap Scanning      Target Services
     Wireshark          Open Ports
     Netcat             Vulnerable Services
          |                 |
          +--------+--------+
                   |
           Isolated Lab
```

**Note:** The IP addresses above are examples. Actual addresses depend on your Host-Only Network configuration.

## 3. Network Configuration

| Component | Configuration |
|---|---|
| Network Type | Host-Only |
| Example Network | 192.168.56.0/24 |
| Kali Linux | 192.168.56.10 |
| Metasploitable 2 | 192.168.56.20 |
| Communication | Internal lab communication |

## 4. Communication Flow

1. Kali Linux sends scanning packets to the target.
2. Metasploitable 2 responds according to its network services and firewall configuration.
3. Nmap analyzes the responses.
4. Wireshark captures and displays network traffic.
5. Students document discovered hosts, ports, and services.

## 5. Important Network Rules

- Both VMs must use the same Host-Only Network.
- Metasploitable 2 must not use Bridged Networking.
- Do not expose vulnerable services to public networks.
- Use actual VM IP addresses instead of the example addresses above.

---

**SNIT Training Institute | Network Scanning Lab Architecture**
