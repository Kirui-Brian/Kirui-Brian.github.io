---
title: "End User Device Information Security Policy"
date: 2025-07-10
permalink: /posts/2025/07/10/end-user-device-information-security-policy/
excerpt: "End User Device Information Security Policy"
tags:
  - writeup
  - reflection
  - cybersecurity
---

**End** **User Device Information Security Policy**

**1. Title of the Policy**

End User Device Information Security Policy

**2. Policy Objectives**

The objectives of this policy will be to:

Protect the confidentiality, integrity, and availability of organisational data accessed, processed, or stored on end-user devices (laptops, desktops, tablets, smartphones, and removable media).

Minimise risks of lost, stolen, compromised, or improperly configured devices.

Make sure there are consistent security standards on company-owned, personally owned (BYOD), and contractor devices used for work purposes.

Achieve and maintain compliance to ISO 27001, GDPR, POPIA, HIPAA, PCI-DSS, and other regulations.

Reduce the rate of malware infection, unauthorised access, and data leakage caused by end-user devices to near zero.

**3. Policy Scope**

This policy applies to:

All end-user computing devices (laptops, desktops, tablets, smartphones, virtual desktops, and thin clients) capable of accessing, storing, transmitting, or processing organisational information regardless of ownership.

All employees (permanent, part-time, temporary), contractors, interns, consultants, and third parties.

All types of data classifications (public, internal, confidential, and restricted).

All locations: on-premises, remote/work-from-home, and while travelling.

All removable media including USB drives, external hard drives or solid-state drives, SD cards, CDs/DVDs.

Those out of scope include industrial control systems (ICS/OT), servers, network appliances, and IoT devices because they are covered under separate policies.

**4. Policy Statements**

Non-compliance will result in disciplinary action up to and including termination and possible legal action.

**5. Policy Coordination and Implementation**

Responsibility matrix:

Implementation roadmap (12 months):

Month 1-3: Procure and deploy Mobile Device Management (MDM/EMM/UEM) solution

Month 4-6: Mandatory enrolment of all company devices; launch BYOD enrolment portal

Month 7-9: Full rollout of encryption, EDR, and patching automation

Month 10-12: Achieve 100 percent compliance; begin continuous monitoring

**6. Policy Monitoring and Evaluation**

Key Performance and Risk Indicators monitored monthly using dashboard:

Data sources: MDM/UEM console, Microsoft Intune/Endpoint Manager, patch management system, SIEM, quarterly internal audits, and annual external penetration test. The EUDSC reviews the dashboard every quarter and initiates corrective actions if targets are missed.

**7. Policy Review**

This policy shall be reviewed at least every two (2) years or earlier if triggered by:

A serious security incident involving end user devices

Major regulatory or technological changes e.g., new OS versions, quantum threats to encryption

Significant organisational changes e.g., mergers, mass remote work

The CISO will lead the review with input from the EUDSC and business units. Updated versions will be approved by the Executive Committee and communicated within 30 days.

Version: 1.0

Effective Date: 15 December 2025

Next Review Date: December 2027 or earlier if required

| Category | Mandatory Requirements |
| --- | --- |
| Device Ownership & Registration | All devices accessing organisational resources must be registered with the IT Service Desk within 7 days of first use. |
| Minimum Security Controls | • Full-disk encryption (BitLocker, FileVault, or equivalent) must be enabled. <br> • Up-to-date endpoint protection (EDR/AV) required. <br> • Automatic OS and application patching. <br> • Screen-lock after 10 minutes of inactivity with strong PIN/password/biometrics. <br> • Multi factor authentication required for all corporate accounts. |
| BYOD Requirements | Personal devices must have a separate work profile/container (Microsoft Intune, VMware Workspace ONE, or equivalent) and allow remote wipe of corporate data only. |
| Removable Media | Use of personal unencrypted USB drives is prohibited. <br> Only organisation issued or approved encrypted USBs allowed. <br> Auto-run disabled by default. |
| Lost or Stolen Devices | Immediate reporting to IT Security within 1 hour. <br> Remote wipe will be initiated for devices containing restricted data. |
| Remote Access | Only approved VPN or Zero-Trust Network Access (ZTNA) solutions allowed. <br> Direct internet exposure of corporate applications forbidden. |
| Prohibited Actions | • Jailbreaking/rooting devices <br> • Installing unapproved software <br> • Disabling security tools <br> • Storing restricted data on personal cloud services not approved by IT |
| Physical Security | Devices must not be left unattended in public places. <br> Cable locks encouraged in shared spaces. |

| Role / Body | Responsibilities |
| --- | --- |
| Chief Information Security Officer (CISO) | Overall policy owner; reports to the board annually |
| End-User Device Security Committee (EUDSC) | Chaired by CISO; members: IT Operations, Human Resource, Legal, Risk, two business unit heads. Meets quarterly |
| IT Operations & Security Team | Device enrolment, MDM/EMM deployment, patch management, incident response, remote wipe capability |
| Heads of Department (HODs) | Ensure 100 % compliance within their units. <br> Monthly attestation of device inventory & security status |
| Human Resources | Include policy acceptance in employment contracts and onboarding; manage offboarding device wipe |

| KPI | Target |
| --- | --- |
| Percentage of registered and compliant devices | 100 % |
| Percentage of devices with full disk encryption | 100 % |
| Average time to patch critical vulnerabilities | ≤ 7 days |
| Percentage of devices with active EDR agent active | 100 % |
| Number of lost/stolen device incidents | ≤ 2 per quarter |
| Number of malware incidents from end-user devices | 0 |
