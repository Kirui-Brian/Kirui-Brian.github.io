---
title: "3 AWS Infrastructure Provisioning with Terraform"
collection: portfolio
permalink: /portfolio/3-aws-infrastructure-provisioning-with-terraform/
excerpt: "Lab 3 – AWS Infrastructure Provisioning with Terraform"
tags:
  - project
  - cybersecurity
---

**Lab** **3** **– AWS Infrastructure Provisioning with Terraform**

**Signed in** to AWS.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_1.png)

Creating **API keys** for authentication.

Access Key section. 

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_2.png)

**Accepting to create access keys**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_3.png)

Access key created. I copied both **Access key** and **Secret access key**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_4.png)

Displaying my EC2 instances:

I clicked on the **aws** icon to display the Console Home.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_5.png)

I clicked on **All Services** to view all services.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_6.png)

I clicked on **EC2**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_7.png)

I clicked on **Instances**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_8.png)

These are the **instances** displayed.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_9.png)

I clicked on Launch instances to create a new instance.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_10.png)

Test instance in **Name and tags**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_11.png)

Choosing an **A****pplication and OS (Amazon Machine Image)** – Debian It is **Free tier eligible**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_12.png)

I retained the default settings for **Instance type**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_13.png)

I chose **Proceed without a key pair** for the **Key pair (login).**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_14.png)

I retained the default settings for Network settings. With this, a Virtual private cloud (VPC) will be created with a public subnet. I left **Allow SSH traffic** **from** box selected under **Firewall (security groups)** – this is to allow connection to my instance from my machine.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_15.png)

I retained the default settings for **Configure storage**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_16.png)

On the bottom right, I clicked **Launch instance**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_17.png)

I got a success message

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_18.png)

I clicked on **Instances** to see my new instance.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_19.png)

After refreshing the page my instance was as below.

I selected the instance by clicking on the **Instance ID****.**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_20.png)

I then clicked on **Instance State** and chose **Terminate (delete) instance.**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_21.png)

I then clicked **Terminate (delete)**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_22.png)

 

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_23.png)

**Part 1: Terraform installation on MS Windows**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_24.png)

I extracted the downloaded zip file and this is the .exe file.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_25.png)

I created a directory named Terraform in drive C:\Program Files and copied the terraform.exe to the created folder.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_26.png)

I created environment variables.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_27.png)

I clicked on Edit the system environment variables.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_28.png)

Then I clicked on Environment Variables in the System Properties window.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_29.png)

I clicked on Path then clicked on Edit button in the Environment Variables window that opened.

I clicked New and pasted the path to terraform.exe that I had copied. 

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_30.png)

I then clicked on OK till all windows closed.

I checked if Terraform has been installed correctly by typing ***terraform -v*** in the command prompt. 

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_31.png)

I did not continue with the lab on Windows.

**Part 2: Installing Terraform on Linux (Debian 11)**

**Step 1:**

I logged in as a super user.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_32.png)

I ran these commands to download, authenticate and install Terraform from Hashicorp website.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_33.png)

The below command solved that.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_34.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_35.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_36.png)

Finished running the installation commands.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_37.png)

I verified that Terraform is installed using this command **terraform -v**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_38.png)

I created the ‘**.aws’** directory using the following command **mkdir -p/root/.aws**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_39.png)

**Step 2:**

This is the **main.tf** file.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_40.png)

I used nano to create **credentials** file.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_41.png)

I ran this command after step 25.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_42.png)

**Step 3:**

I cleaned up the files with the command.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_43.png)

I navigated to the aws terraform working directory and ran **terraform init.**

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_44.png)

Then I ran **terraform plan**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_45.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_46.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_47.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_48.png)

Then I ran **terraform apply**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_49.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_50.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_51.png)

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_52.png)

Keyed in **yes** to the prompt and pressed **E****nter**.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_53.png)

Finally refreshed at the **EC2->Instance** page.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_54.png)

And completed the lab by deleting the instance as per step 7.

![Screenshot](/images/projects/3-aws-infrastructure-provisioning-with-terraform/image_55.png)
