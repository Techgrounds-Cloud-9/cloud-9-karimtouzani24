# Subject
Well Architected Framework  

Introduction  
The way you set up your IT or your application, the architecture, is a big part of how your application runs, how secure it is, and how much it costs. To help design architectures, AWS has the Well Architected Framework (WAF, not to be confused with the Web Application Firewall).  

WAF consists of six pillars, all with their own key concepts, design principles, and best practices. You should be able to name these pillars, as well as understand what they mean. You should also be able to think about architectures in the context of the Well Architected Framework.  

The mnemonic device for the six pillars is CROPSS (the first letter of each pillar). The pillars are:  
- Cost optimization
- Reliability
- Operational Excellence
- Performance efficiency
- Security
- Sustainability

AWS has them ordered as OSRPCS, but that’s a little harder to remember.

## Key terminology
Operational excellence pillar:  

The first pillar is the Operational Excellence pillar. This pillar focuses on running and monitoring systems to deliver business value, and continually improving supporting processes and procedures.
Key topics include:  
- managing and automating changes, responding to events, and defining standards to successfully manage daily operations.  

• Support development and run workloads effectively  
• Gain insight into workload operations  
• Continuously improve processes and procedures to deliver business value  
 
• Best practices for operational excellence:  
    - Perform operations as code  
    - Make frequent, small, reversible changes  
    - Refine operations procedures frequently  
    - Anticipate failure  
    - Learn from all operational failures  

Security Pillar:  

The Security pillar involves the ability to monitor and protect systems while delivering business value through risk assessments and mitigation strategies.
Key topics include  
- protecting the confidentiality and integrity of data, identifying and managing who can do what (or privilege management), protecting systems, and establishing controls to detect security events.  

• Protect data, systems, and assets to take advantage
of cloud technologies to improve your security  

• Best practices for security:
    - Implement a strong identity foundation
    - Enable traceability
    - Apply security at all layers
    - Automate security best practices
    - Protect data in transit and at rest
    - Keep people away from data
    - Prepare for security events  

Reliability Pillar:  

The Reliability pillar is concerned with the ability of a system to recover from infrastructure or service failures, and to dynamically acquire computing resources to meet demand and mitigate disruptions. Reliability can help you recover from failures and meet demand.  

Reliability in the cloud comprises three areas: Foundations, change management, and failure management.

• Ensuring a workload can perform its intended function correctly and consistently when it’s expected to
• This includes the ability to operate and test the workload through its total lifecycle  

• Best practices for reliability:
    - Automatically recover from failure
    - Test recovery procedures
    - Scale horizontally to increase aggregate workload availability  
    - Stop guessing capacity
    - Manage change in automation  

Performance Efficiency Pillar  

The Performance Efficiency pillar refers to using computing resources efficiently while meeting system requirements. At the same time, it is important to maintain that efficiency as demand fluctuates and technologies evolve  

Factors that influence performance efficiency in the cloud include: selection, review, monitoring, tradeoffs.  

• The ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve  

• Best practices for performance efficiency:
    - Democratize advanced technologies
    - Go global in minutes
    - Use serverless architectures
    - Experiment more often
    - Consider mechanical sympathy  

Cost Optimization Pillar  

Cost optimization refers to the ability to avoid or eliminate unneeded expenses and resources. Use coste-effective resources, match supply with demand, increase expenditure awareness, optimize over time.  

• The ability to run systems to deliver business value at the lowest price point  

• Best practices for cost optimization:
    - Implement Cloud Financial Management
    - Adopt a consumption model
    - Measure overall efficiency
    - Stop spending money on undifferentiated heavy lifting
    - Analyze and attribute expenditure


### Sources
https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc  

https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html  

