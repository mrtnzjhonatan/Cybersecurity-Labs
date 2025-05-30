# TryHackMe: Blue (EternalBlue Exploit) Write-Up

## Introduction  
The **Blue** room on TryHackMe focuses on exploiting the **MS17-010** vulnerability, also known as **EternalBlue**. This critical security flaw affects Microsoft’s SMBv1 protocol, allowing remote attackers to execute arbitrary code and gain full control over vulnerable Windows systems.

This write-up details the process of scanning, exploiting, and post-exploitation steps performed to compromise the target machine, as well as lessons learned throughout the exercise.

---

## Tools Used  
- `nmap`: Network scanner for port and vulnerability detection.  
- `msfconsole`: Metasploit Framework for exploit execution.  
- `searchsploit`: Local database search for exploits.  
- `smbclient`: SMB share enumeration and access tool.

---

## Step 1: Reconnaissance and Vulnerability Scanning  
Begin by scanning the target machine to identify open SMB ports and verify if the EternalBlue vulnerability exists:

```bash
nmap -p 445 --script smb-vuln-ms17-010 <target-ip>

