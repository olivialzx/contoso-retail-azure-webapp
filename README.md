CONTOSO RETAIL
AZURE CLOUD ENGINEERING PROJECT




PROJECT SUMMARY

The Contoso Retail project is an end-to-end Azure cloud environment built to demonstrate the deployment, security, monitoring, backup, governance, and cost management of a retail web application.

The project combines Azure PaaS and IaaS services.

The customer-facing application is hosted on Azure App Service and deployed from GitHub. A Linux Virtual Machine provides the backend infrastructure workload. Azure SQL Database and Azure Storage provide managed data services. Azure Key Vault and Managed Identity provide secure secret management. Azure RBAC, NSG, Bastion, Defender for Cloud, and Azure Policy provide access and security controls. Azure Monitor, Application Insights, alerts, backup, Cost Management, and Azure Advisor provide operational management.




PROJECT ARCHITECTURE

Users
  |
  | HTTPS
  v
Azure App Service
contoso-retail-web-2026
  |
  | Application Deployment
  ^
  |
GitHub
Application Source Code


AZURE NETWORK

Virtual Network
10.0.0.0/16
  |
  +--------------------------+
  |                          |
  v                          v
Frontend Subnet          Backend Subnet
10.0.0.0/24              10.0.1.0/24
                             |
                             v
                    Linux Backend VM
                    vm-contoso-backend393
                             |
                             v
                            NSG
                             |
                             v
                        Azure Bastion
                     Secure VM Administration


DATA SERVICES

Azure SQL Server
sql-contoso-retail-2026
  |
  v
Azure SQL Database
contoso-retail-db


Azure Storage Account
  |
  +---- Blob Container
  |
  +---- File Share


APPLICATION SECURITY

Azure App Service
  |
  v
System Assigned Managed Identity
  |
  v
Azure Key Vault
  |
  v
Application Secrets


SECURITY AND GOVERNANCE

Azure RBAC
  |
  +---- Controls Azure resource access

Network Security Group
  |
  +---- Controls network traffic

Azure Bastion
  |
  +---- Provides secure VM administration

Microsoft Defender for Cloud
  |
  +---- Security posture and recommendations

Azure Policy
  |
  +---- Governance and tagging requirements


MONITORING AND ALERTING

Application
  |
  v
Application Insights
  |
  v
Azure Monitor
  |
  v
CPU Alert Rule
CPU greater than 80%
  |
  v
Action Group
  |
  v
Email Notification


BACKUP AND OPERATIONS

Backend Linux VM
  |
  v
Recovery Services Vault
  |
  v
VM Backup / Recovery Point


Cost Management
  |
  +---- Monthly Budget: $50
  +---- 80% Alert
  +---- 100% Alert


Azure Advisor
  |
  +---- Cost recommendations
  +---- Security recommendations
  +---- Reliability recommendations
  +---- Performance recommendations




RESOURCE ORGANIZATION

Resource Groups were used to logically organize the Azure environment.
rg-contoso-network

Used for: VNet, subnets, NSGs, route tables, Azure Bastion, public IPs.

rg-contoso-app

Used for: App Service, App Service Plan, VM, Application Gateway / Load Balancer.

rg-contoso-data

Used for: Azure SQL Database, SQL Server, Storage Account, Blob containers.

rg-contoso-security

Used for: Key Vault, Defender for Cloud and security-related resources.

rg-contoso-monitoring

Used for: Log Analytics Workspace, Application Insights, Azure Monitor alerts, Action Groups and dashboards.




NETWORKING

Virtual Network:

10.0.0.0/16

Frontend Subnet:

10.0.0.0/24

Backend Subnet:

10.0.1.0/24

The network was divided into frontend and backend segments to provide logical network separation.




COMPUTE

Azure App Service:

contoso-retail-web-2026

Hosts the Python retail web application using Azure PaaS.

Linux Virtual Machine:

vm-contoso-backend393

Provides the backend IaaS workload.

Azure Bastion provides secure administrative access to the VM.




STORAGE AND DATABASE

Azure Storage was configured with:

Blob Container
File Share

Azure SQL was configured with:

SQL Server:
sql-contoso-retail-2026

Database:
contoso-retail-db

The SQL Database uses the General Purpose Serverless model with 1 vCore.




APPLICATION DEPLOYMENT

The application source code was maintained in GitHub and deployed to Azure App Service.



Deployment flow:

GitHub
  |
  v
Azure App Service
  |
  v
Running Python Web Application




SECURITY

The project uses multiple layers of Azure security.

RBAC controls who can access Azure resources.

NSGs control network traffic.

Azure Bastion provides secure VM administration.

Managed Identity provides an Azure identity for the App Service.

Key Vault provides secure application secret management.

Microsoft Defender for Cloud provides security posture recommendations.

Azure Policy provides governance and resource compliance.



MONITORING

Application Insights was enabled for the App Service to provide application telemetry.

Azure Monitor was used for infrastructure monitoring and VM metrics.

A CPU alert was configured with an 80 percent threshold.

The alert triggers an Action Group that sends an email notification.



BACKUP

A Recovery Services Vault was configured to protect the backend Linux VM.

Backup flow:

Backend VM
  |
  v
Recovery Services Vault
  |
  v
Recovery Point



GOVERNANCE AND COST MANAGEMENT

Azure Policy was configured for governance requirements such as resource tagging.

Cost Management was configured with a $50 monthly demonstration budget.

Alert thresholds were configured at 80 percent and 100 percent.

Azure Advisor was reviewed for recommendations related to cost, security, reliability, and performance.







PROJECT IMPLEMENTATION FLOW

1. Created and organized Azure Resource Groups.

2. Created the Virtual Network with 10.0.0.0/16 address space.

3. Created frontend and backend subnets.

4. Deployed the Linux backend VM.

5. Configured Network Security Group controls.

6. Configured Azure Bastion for secure VM administration.

7. Created the App Service and App Service Plan.

8. Connected GitHub deployment and deployed the Python application.

9. Created and configured Azure Storage.

10. Created the Azure SQL Server and SQL Database.

11. Created Azure Key Vault.

12. Enabled System Assigned Managed Identity for the App Service.

13. Configured Azure RBAC.

14. Reviewed Microsoft Defender for Cloud security recommendations.

15. Enabled Application Insights.

16. Configured Azure Monitor.

17. Created the CPU greater-than-80-percent alert.

18. Configured the Action Group and email notification.

19. Configured Recovery Services Vault for VM backup.

20. Configured Azure Policy for governance.

21. Configured Cost Management and budget alerts.

22. Reviewed Azure Advisor recommendations.

23. Reviewed VM metrics and validated the deployed environment.





AZURE SERVICES USED

Compute:
Azure App Service
Azure App Service Plan
Azure Linux Virtual Machine

Networking:
Azure Virtual Network
Subnets
Network Security Group
Azure Bastion

Storage:
Azure Storage Account
Blob Storage
Azure File Share

Database:
Azure SQL Server
Azure SQL Database

Security:
Azure Key Vault
Managed Identity
Azure RBAC
Microsoft Defender for Cloud

Monitoring:
Azure Monitor
Application Insights
Metric Alerts
Action Groups

Backup:
Recovery Services Vault

Governance and Operations:
Azure Policy
Cost Management
Azure Advisor

Deployment:
GitHub






PROJECT OUTCOME

The completed Contoso Retail environment demonstrates the practical responsibilities of an Azure Cloud Engineer:

Resource organization
Network design
IaaS deployment
PaaS application hosting
Application deployment
Storage management
Database deployment
Identity and access management
Network security
Secret management
Cloud security
Monitoring
Alerting
Backup and recovery
Governance
Cost management
Cloud optimization




The project demonstrates the complete cloud workload lifecycle:

PLAN
  |
DEPLOY
  |
CONFIGURE
  |
SECURE
  |
MONITOR
  |
ALERT
  |
BACK UP
  |
GOVERN
  |
OPTIMIZE
  |
DOCUMENT




PROJECT EVIDENCE

The project documentation includes screenshots covering:

01 Resource Groups
02 VNet and Subnets
03 App Service
04 GitHub Deployment
05 Backend VM
06 Storage
07 SQL Database
08 Key Vault
09 RBAC
10 Application Insights
11 Monitor Alert
12 Backup
13 Azure Policy
14 Cost Management
15 Azure Advisor
16 VM Metrics

The repository also contains the Azure architecture diagram showing the resources, relationships, security controls, monitoring flow, backup flow, and operational components implemented in the project.
