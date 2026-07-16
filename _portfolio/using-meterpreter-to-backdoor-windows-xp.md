---
title: "Using Meterpreter to Backdoor Windows XP"
collection: portfolio
permalink: /portfolio/using-meterpreter-to-backdoor-windows-xp/
excerpt: "Lab - Using Meterpreter to backdoor Windows XP"
tags:
  - project
  - cybersecurity
---

**Lab - Using Meterpreter to backdoor Windows XP**

Windows XP IP address:

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_1.png)

Confirming network range in Kali is same as that in Windows XP.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_2.png)

Pinging the Windows XP from Kali:

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_3.png)

Allowing RDP access.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_4.png)

Nmap result.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_5.png)

Launching meterpreter:

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_6.png)

Setting IP address for RHOST.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_7.png)

Launching payload using execute command.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_8.png)

Checking to see if the machine has a firewall and if it is enabled.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_9.png)

Checking the status of Windows firewall.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_10.png)

The command ***run getgui -h*** failed due to deprecation of getgui.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_11.png)

So instead, I did used this replacement.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_12.png)

Using ***rdesktop***

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_13.png)

Logon message.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_14.png)

**LOGGED IN!**

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_15.png)

The command did not work.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_16.png)

But the sessions are closed.

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_17.png)

![Screenshot](/images/projects/using-meterpreter-to-backdoor-windows-xp/image_18.png)
