
# Subject
Detection, Response and analysis

## Key terminology
social engineering:  
Social engineering is a manipulation technique that exploits human error to gain private information, access, or valuables. In cybercrime, these “human hacking” scams tend to lure unsuspecting users into exposing data, spreading malware infections, or giving access to restricted systems. Attacks can happen online, in-person, and via other interactions.  

examples: phishing, spear phishing, baiting, malware, pretexting, tailgating, vishing.

3 steps to follow when getting hit with an attack: Detection, response and analysis.  

detection:  
- is the first step to stop an attack and preventing future attempts.  
- wireshark can help to detect anomalies on the network.  
- IDS and IPS are also used.  

IDS:  
An Intrustion Detection System (IDS) is a system that surveys a network for malicious activities and issues alert when it uncovers any such activity. Any threat is usually reported to the administrator.  

2 types of IDS:  
- NIDS, Network intrusion detection system. Placed at a strategic point within the network to examine traffic from all devices on the network. Primarily, it performs an analysis of passing traffic on the entire subnet and matches the traffic passed on the subnet to the collection of known attacks. Once it identifies an attack or senses abnormal behavior, it sends an alert to the administrator.  

- HIPS, Host intrusion detection systems run on self-standing hosts or devices on the network. In short, it takes a snapshot of existing system files and matches it with the previous snapshots. Likewise, if the analytical system files were altered or deleted, it sends an alert to the administrator to investigate.  

Detection Methods of IDS:  
1. Signature-Based Method
Signature-based IDS refers to the detection of attacks based on predefined criteria such as network traffic or identified malicious instruction sequences common to malware.  
The detected patterns are known as signatures. Signature-based IDS can easily detect already existent or known attack patterns while it’s difficult to detect new attacks with no existing patterns.  

2. Anomaly-Based Method
Anomaly-based IDS were primarily introduced to detect unknown malware attacks which were, in part, due to rapid development of new malware.  
The whole idea is the use of machine learning to create a trustworthy activity model and compare new behavior against the model.  
It is then declared suspicious or potentially malicious if it is not found in the model.  
Although the approach enables the detection of previously unknown attacks, it is susceptible to false positives that are previously unknown. Harmless and legitimate activity may also be classified as malicious.


IPS:  
- Intrusion Prevention Systems are considered as supplements to Intrusion Detection System because both IPS and IDS monitor network traffic and system activities for malicious activity. IPS can take proactive actions such as sending an alarm, resetting a connection or blocking traffic from the hostile IP address. There are four types of intrusion prevention system namely:  
network-based IPS, Wireless IPS, Network behavior analysis and the Host-based IPS.  

Detection methods of IPS:  
1. Signature-Based Detection
Firstly, signature-based IDS compares network packets with already-known attack patterns called signatures.

2. Statically Anomaly-Based Detection
Secondly, anomaly-based IDS operates network traffic and compares it against an established baseline. This baseline will identify what is normal for that network and what protocols are used. However, it may flag a safe activity as harmful if the baselines are not meticulously configured.

3. Stateful Protocol Analysis Detection
Finally, this IDS method recognizes deviations of protocols stated by comparing observed events with pre-configured profiles of generally accepted definitions of safe activities.

Response:  
- first thing to do after its detected is trying to contain the damage.  
- after its contained, you can try to figure out the root cause, so that you can stop it.  
- finally you enter the recovry phase, when you try to get all systems back online.  

Response and analysis are part of a disaster recovery plan. this plan is an important part of a bigger  
business continuity plan.  

Disaster recovery plan (DRP):  
A documented, structured approach that describes how an organization can quickly resume work after an unplanned incident. A DRP is an essential part of a business continuity plan (BCP).  

A business continuity plan (BCP):  
refers to an organization’s system of procedures to restore critical business functions in the event of an unplanned disaster. These disasters could include natural disasters, cyberattacks, service outages, or other potential threats. Business continuity planning (BCP) enables organizations to resume business operations with minimal downtime.  

BCP: Business Continuity Planning deals with keeping business operations running — perhaps in another location or by using different tools and processes — after a disaster has struck.

DRP: Disaster Recovery Planning deals with restoring normal business operations after the disaster takes place.

mitigating or hack response strategies:  
An incident response plan (IRP) is a set of tools and procedures that your security team can use to identify, eliminate, and recover from cybersecurity threats. It is designed to help your team respond quickly and uniformly against any type of external threat.  

These plans are necessary to minimize damage caused by threats, including data loss, abuse of resources, and the loss of customer trust.  
These are the 6 steps of IRP: 

1. Preparation – Perform a risk assessment and prioritize security issues, identify which are the most sensitive assets, and which critical security incidents the team should focus on. Create a communication plan, document roles, responsibilities, and processes, and recruit members to the Cyber Incident Response Team (CIRT).

2. Identification – The team should be able to effectively detect deviations from normal operations in organizational systems, and when an incident is discovered, collect additional evidence, decide on the severity of the incident, and document the “Who, What, Where, Why, and How”.

3. Containment – Once the team identifies a security incident, the immediate goal is to contain the incident and prevent further damage:
Short-term containment — for example, isolating network segments or taking down infected production servers and handing failover.
Long-term containment — applying temporary fixes to affected systems to allow them to be used in production, while rebuilding clean systems.  

4. Eradication – The team must identify the root cause of the attack, remove malware or threats, and prevent similar attacks in the future. For example, if a vulnerability was exploited, it should be immediately patched.

5. Recovery – The team brings affected production systems back online carefully, to ensure another incident doesn’t take place. Important decisions at this stage are from which time and date to restore operations, how to verify that affected systems are back to normal, and monitoring to ensure activity is back to normal.

6. Lessons Learned – This phase should be performed no later than two weeks from the end of the incident, to ensure the information is fresh in the team’s mind. The purpose of this phase is to complete documentation of the incident, investigate further to identify its full scope, understand where the response team was effective, and areas that require improvement.

Concept of systems hardening:  
Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vector s and condensing the system’s attack surface. By removing superfluous programs, accounts functions, applications, ports, permissions, access, etc. attackers and malware have fewer opportunities to gain a foothold within your IT ecosystem.

Systems hardening demands a methodical approach to audit, identify, close, and control potential security vulnerabilities throughout your organization. There are several types of system hardening activities, including:  

- Application hardening
- Operating system hardening
- Server hardening
- Endpoint hardening
- Database hardening
- Network hardening 

different types of disaster recovery options:  
One of the key elements in any Disaster Recovery plan is the selection of a secondary site for data storage to help prevent data loss in the event of cyber attacks or a natural disaster. DR software will extract critical business data from this secondary site and restore it back to primary servers in the event of a major system failure. There are three major types of disaster recovery sites that can be used: cold, warm, and hot sites.  

Cold Computing Sites - the most simplistic type of disaster recovery site. A cold site consists of elements to provide power and networking capability as well as cooling. It does not include other hardware elements such as servers and storage. The use of a cold site is very limiting to a business since before it can be used, backup data along with some additional hardware must be sent to the site and installed. This will impede workflow.

Warm Computing Sites - contain all the elements of a cold site while adding to them additional elements including storage hardware such as tape or disk drives along with both servers and switches. Warm sites are "ready to go" in one sense, but they still need to have data transported to them for use in recovery should a disaster occur.

Hot Computing Sites - a fully functional backup site that already has important data mirrored to it. This is the ideal disaster recovery site but can be challenging to attain.   

RPO and RTO:  
Recovery point objective (RPO) describes a period of time in which an enterprise’s operations must be restored following a disruptive event, e.g., a cyberattack, natural disaster or communications failure.
It’s an important part of your disaster recovery plan, and is typically paired with recovery time objective (RTO)—the maximum time to restore critical functions following a disruptive event.  

Recovery point objective (RPO)  
is defined as the maximum amount of data – as measured by time – that can be lost after a recovery from a disaster, failure, or comparable event before data loss will exceed what is acceptable to an organization. So it describes the amount of time that can pass during an event before data loss exceeds that tolerance.

This also dictates procedures for disaster recovery planning, including the acceptable backup interval, because it refers to the last point when the organization’s data was preserved in a usable format. For example, an RPO of 60 minutes requires a system backup every 60 minutes.  

RPOs can determine:
How much data will be lost after a disaster or event
How frequently you need to backup your data for disaster recovery purposes—in other words, RPO does not concern other IT needs.  

The recovery time objective (RTO)  
is the amount of real time a business has to restore its processes at an acceptable service level after a disaster to avoid intolerable consequences associated with the disruption. The RTO answers the question: “How much time after notification about the business process disruption should it take to resume normal operations?”  

RTO represents how much real time that can pass before the interruption impedes the flow of normal business operations unacceptably.  




## Exercise  
- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?  

answer: To know the RPO, you need to know the interval of the backups. The company makes daily backups, so the rpo is 24h. 

- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?  

anser: To know the RTO, you need to know how fast it can operate after an event. It takes 8 minutes to backup the server. This is the RTO.


### Sources
https://www.kaspersky.com/resource-center/definitions/what-is-social-engineering  

https://terranovasecurity.com/examples-of-social-engineering-attacks/  

https://www.uscybersecurity.net/network-intrusion/  

https://www.techtarget.com/searchdisasterrecovery/definition/disaster-recovery-plan  

https://www.citrix.com/nl-nl/solutions/vdi-and-daas/what-is-a-business-continuity-plan.html  

https://www.oreilly.com/library/view/cissp-for-dummies/9781118417102/a6_16_9781118362396-ch11.html#:~:text=BCP%3A%20Business%20Continuity%20Planning%20deals,after%20the%20disaster%20takes%20place.  

https://www.exabeam.com/incident-response/incident-response-plan/  

https://www.beyondtrust.com/resources/glossary/systems-hardening#:~:text=Systems%20hardening%20is%20a%20collection,condensing%20the%20system's%20attack%20surface.  

https://blog.icorps.com/bid/101789/types-of-disaster-recovery-sites  

https://www.imperva.com/learn/availability/recovery-point-objective-rpo/  

https://www.druva.com/glossary/what-is-a-recovery-point-objective-definition-and-related-faqs/#:~:text=Recovery%20point%20objective%20(RPO)%20is,is%20acceptable%20to%20an%20organization.

### Overcome challenges


### Results