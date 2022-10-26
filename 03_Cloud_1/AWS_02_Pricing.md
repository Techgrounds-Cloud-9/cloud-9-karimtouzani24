# Subject
AWS Pricing

## Key terminology
One of the main reasons for moving to the cloud is cost. If done well, public cloud infrastructures can reduce costs significantly compared to traditional data centers.  
This is done by adopting  
- a pay-as-you-go pricing model  
- and economies of scale.  

You pay only for the compute capacity, storage, and outbound data transfer that you use. You never pay for inbound data transfer and data transfer between services within the same region.  

AWS lists four advantages of their pricing model:  

- Pay-as-you-go  
- Save when you commit  
- Pay less by using more  
- Benefit from massive economies of scale  

When creating a new AWS account, you automatically get a free-tier account for the first 12 months. Some services are free up to a certain limit with a free-tier account.
Other services are always free. However, those services might be integrated with other services for which you have to pay.  

The Total Cost of Ownership (TCO) is used to measure how much an infrastructure would cost if it were hosted the traditional way. This is done by measuring capital expenditures (capex). The cloud pricing model allows you to trade capex for variable expenditure. This can reduce cost by not spending money on capacity you don’t need.


## Exercise  
The four advantages of the AWS pricing model.  
- Pay-as-you-go  
 Only pay for what use, helping your organization remain agile, responsive and always able to meet scale demands. You can adapt your business depending on need and not on forecasts, reducing the risk or overprovisioning or missing capacity.  

- Save when you commit  
Savings Plans offer savings over On-Demand in exchange for a commitment to use a specific amount (measured in $/hour) of an AWS service or a category of services, for a one- or three-year period.  

- Pay less by using more  
With AWS, you can get volume based discounts and realize important savings as your usage increases. For services such as S3 and data transfer OUT from EC2, pricing is tiered, meaning the more you use, the less you pay per GB.  

- Benefit from massive economies of scale  

The AWS Free Tier provides customers the ability to explore and try out AWS services free of charge up to specified limits for each service. The Free Tier is comprised of three different types of offerings, a 12-month Free Tier, an Always Free offer, and short term trials.  

Services with a 12-month Free Tier allow customers to use the product for free up to specified limits for one year from the date the account was created. Services with an Always Free offer allow customers to use the product for free up to specified limits as long as they are an AWS customer. Services with a short term trial are free to use for a specified period of time or up to a one-time limit depending on the service selected. Details on the limits and services provided for free are detailed in each card on the Free Tier page

AWS free tier for:  
- S3, 5GB of standard storage , 20000 get requests, 2000 put requests for 12 months.
- EC2, 750 hours per month for 12 months for windows, linux, RHEL, SLES t2.micro or t3.micro dependent on region.
- Always free services  

12-Months Free: These free tier offers are only available to new AWS customers, and are available for 12 months following your AWS sign-up date. When your 12 month free usage term expires or if your application use exceeds the tiers, you simply pay standard, pay-as-you-go service rates (see each service page for full pricing details). Restrictions apply; see offer terms for more details.

Always Free: These free tier offers do not automatically expire at the end of your 12 month AWS Free Tier term, but are available to both existing and new AWS customers indefinitely.

Trials: These free tier offers are short term trial offers that start from the time of first usage begins. Once the trial period expires you simply pay standard, pay-as-you-go service rates (see each service page for full pricing details).

Understand the differences between capex and opex  

- Capital Expenditure (CapEx): It is the initial spending of money ( whole together ) on physical infrastructure, and then deducting that up-front expense over time. The up-front cost from CapEx has a value that reduces over time. All expenses incurred for long-term benefits in the future lie under CapEx.  

- Operational Expenditure (OpEx): It is like a pay-as-you-go service. You can deduct this expense in the same year you spend it. There is no up-front cost, as you pay for a service or product as you use it. It is as the name suggests, the expense of daily operation.  

Examples of CapEx:   
- Manufacturing plants, equipment, and machinery
- Computers and Hardware
- Building improvements
- Vehicles  

Examples of OpEx:  
- Interest paid on debt
- Property taxes
- Accounting and legal fees
- Wages and salaries
- Business travel
- Rent and utilities  

The AWS Pricing Calculator is an estimation tool that provides an approximate cost of using AWS services based on the usage parameters that you specify. The AWS Pricing Calculator is not a quote tool, and does not guarantee the cost for your actual use of AWS services. The cost estimated by the AWS Pricing Calculator may vary from your actual costs for a number of reasons. Common reasons the estimate may be different from your actual cost include:  
- actual usage  
- region used  
- change in price
- tax not included  
- etc  

With AWS Pricing Calculator, you can do the following tasks:

- View transparent prices – See the calculations behind the estimated prices for your service configurations. You can view price estimates by service or by groups of services to analyze your architecture costs.
- Use groups for hierarchical estimates – Sort your estimates into groups to align with your architecture for clear service cost analysis.
- Share your estimates – Save the link to each estimate to share or revisit at a later time. Estimates are saved to the AWS public servers.
- Export your estimates – Export your estimates in CSV or PDF format to share locally with your stakeholders.

https://docs.aws.amazon.com/pdfs/whitepapers/latest/how-aws-pricing-works/how-aws-pricing-works.pdf  Belangrijk document!

### Sources
https://calculator.aws/#/  

https://docs.aws.amazon.com/pdfs/whitepapers/latest/how-aws-pricing-works/how-aws-pricing-works.pdf  

https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all#  

https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all#Learn_more_about_AWS_Free_Tier_Products  

https://www.geeksforgeeks.org/capex-vs-opex-in-cloud-computing/  

https://aws.amazon.com/calculator/calculator-assumptions/