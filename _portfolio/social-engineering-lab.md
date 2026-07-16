---
title: "Social Engineering Lab"
collection: portfolio
permalink: /portfolio/social-engineering-lab/
excerpt: "Social-Engineer Toolkit (SET) main interface in Kali Linux."
tags:
  - project
  - cybersecurity
---

![Screenshot](/images/projects/social-engineering-lab/image_1.png)

Social-Engineer Toolkit (SET) main interface in Kali Linux.

![Screenshot](/images/projects/social-engineering-lab/image_2.png)

Selecting Website Attack Vectors.

![Screenshot](/images/projects/social-engineering-lab/image_3.png)

Selecting the "Credential Harvester" module in SET.

![Screenshot](/images/projects/social-engineering-lab/image_4.png)

![Screenshot](/images/projects/social-engineering-lab/image_5.png)

![Screenshot](/images/projects/social-engineering-lab/image_6.png)

Capturing the username and password. The URL used is Strathmore eLearning.

Issues:
**Issue 1 (IP Address)**:

**Problem**: An IP in the URL is suspicious and not internet-accessible.

**Solution**: Use a domain name and port forwarding.

**Issue 2 (HTTP)**:

**Problem**: HTTP is unencrypted.

**Solution**: Use Let’s Encrypt for free HTTPS certificates.

**Issue 3 (Ugly URL)**:

**Problem**: IP-based URL looks fake.

**Solution**: Use a URL shortener (e.g., Bitly) or a convincing domain.

Email Blast

**SPF** – Specifies which servers can send emails for a domain to prevent spoofing.

Example SPF rule for *company.com*:

***v=spf1 ip4:123.45.67.89*** ***include:gmail.com*** ***~all***

**DKIM** – Adds a digital signature to verify email authenticity.

**DMARC** – Tells receivers how to handle emails failing SPF/DKIM checks.

Attached.

![Screenshot](/images/projects/social-engineering-lab/image_7.png)

Launching msfvenom on Kali terminal.

![Screenshot](/images/projects/social-engineering-lab/image_8.png)

In /tmp directory, we can see our generated LegitProgram. And running Python script.

IP 192.168.100.71 is Metasploitable’s.

![Screenshot](/images/projects/social-engineering-lab/image_9.png)

Metasploitable2 VM downloading Legit Program.

![Screenshot](/images/projects/social-engineering-lab/image_10.png)

Starting msfconsole.

![Screenshot](/images/projects/social-engineering-lab/image_11.png)

Setting up Metasploit and seeing opened sessions.

![Screenshot](/images/projects/social-engineering-lab/image_12.png)

Changing permissions and executing LegitProgram in Metasploitable2.
