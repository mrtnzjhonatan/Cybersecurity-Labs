# TryHackMe: Blue (EternalBlue Exploit)

### Summary
- Vulnerability: MS17-010 (EternalBlue)
- Tools used: `nmap`, `msfconsole`, `searchsploit`, `smbclient`
- Exploitation: Metasploit with exploit/windows/smb/ms17_010_eternalblue
- Post Exploitation: `hashdump`, privilege escalation enumeration

### Lessons Learned
- Always patch critical Windows vulnerabilities
- EternalBlue is still a risk on unmaintained systems
