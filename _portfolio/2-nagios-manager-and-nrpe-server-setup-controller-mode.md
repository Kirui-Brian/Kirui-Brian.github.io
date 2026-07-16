---
title: "2 Nagios Manager and NRPE Server Setup Controller Mode"
collection: portfolio
permalink: /portfolio/2-nagios-manager-and-nrpe-server-setup-controller-mode/
excerpt: "Lab 2 - Nagios Manager and NRPE Server Setup - Controller Mode"
tags:
  - project
  - cybersecurity
---

**Lab 2 - Nagios Manager and NRPE Server Setup - Controller Mode**

The 4 Debian VMs.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_1.png)

Managed Node 2 IP Address:

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_2.png)

Managed Node 3 IP Address.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_3.png)

Using winscp to copy networkAutomation to the controller.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_4.png)

Debian Controller IP Address:

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_5.png)

Switching to root user, and verifying the networkAutomation folder was copied.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_6.png)

Generating SSH Key Pair.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_7.png)

Copying SSH Public Key to Managed Nodes

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_8.png)

Already setup on Managed Node 1

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_9.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_10.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_11.png)

Installing ansible.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_12.png)

Checking it’s version.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_13.png)

Confirming configuration folder

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_14.png)

Testing ansible connectivity to all managed nodes.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_15.png)

Running the Playbook to configure bind DNS on the managed nodes.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_16.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_17.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_18.png)

Hosts

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_19.png)

Services

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_20.png)

Playbook preparation

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_21.png)

Cleaning up bash script

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_22.png)

Testing ansible connectivity to all managed nodes

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_23.png)

Running the playbook to configure bind DNS on the managed nodes.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_24.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_25.png)

Verifying nagios manager server configuration

Hosts tab.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_26.png)

Services tab

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_27.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_28.png)

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_29.png)

All services are now running OK.

![Screenshot](/images/projects/2-nagios-manager-and-nrpe-server-setup-controller-mode/image_30.png)

Based on the services screenshot, my observation is that “All services are running OK.” This means Nagios Manager successfully communicated with the NRPE servers, and the monitoring checks are returning healthy results. The automated setup and configuration via the playbook worked correctly, enabling proper monitoring of the managed nodes. The system is functioning as intended, with all services operational and reporting accurate status.
