# delivery

- ip: 10.10.10.222

## port 80

### delivery.htb

### helpdesk.delivery.htb
- powered by **osticket**
- create new ticket
- register account with email to get confirmation
- use that to login to mattermost
- http://helpdesk.delivery.htb/scp/login.php
- abc@delivery.htb
  - 8577242@delivery.htb
- root@delivery.htb
- `maildeliverer:Youve_G0t_Mail!`
- PleaseSubscribe! hashcat rules
- osTicket (v1.15.1)

## port 8065 = mattermost
- create account: `8577242@delivery.htb:Password123!`


## ssh
```
"DataSource": "mmuser:Crack_The_MM_Admin_PW@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s",
"AtRestEncryptKey": "n5uax3d4f919obtsp1pw1k5xetq1enez",
```
- `mysql -h localhost -u mmuser -p Crack_The_MM_Admin_PW mattermost`
- mattermost root: `root:$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO`
- hash type: 3200
- cracked: `$2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO:PleaseSubscribe!21`

