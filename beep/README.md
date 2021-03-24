# beep

- ip: `10.10.10.7`
- name: `beep.localdomain`
- os:
- ports:
  - 80/tcp: Elastix
    - FreePBX 2.8.1.4
    - creds: admin/jEhdIekWmdjE => also is SSH root password
  - 110/tcp: pop3
    - Cyrus pop3d (`2.3.7-Invoca-RPM-2.3.7-7.el5_6.4`)
  - 10000/tcp: http
    - MiniServ 1.570 (Webmin httpd)
    - http-server-header: MiniServ/1.570

## hydra brute force

```
[22][ssh] host: 10.10.10.7   login: root   password: jEhdIekWmdjE
```

## weaknesses
- local file inclusions
- php filters and LFI
- hydra brute force
- pbx and wardialling
- smtp

