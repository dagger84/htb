# grandpa

- ip: 10.10.10.14
- Windows Server 2003 or Windows XP Professional

- Computer        : GRANPA
- OS              : Windows .NET Server (5.2 Build 3790, Service Pack 2). = Windows Server 2003
- Architecture    : x86
- System Language : `en_US`
- Domain          : HTB
- Logged On Users : 2
- Meterpreter     : x86/windows

## lessons
- have to migrate to a different process (`wmiprvsc.exe`)
  - otherwise can't use simple commands like `getuid`
- `ms10_015_kitrap0d` kernel exploit works for privilege escalation
