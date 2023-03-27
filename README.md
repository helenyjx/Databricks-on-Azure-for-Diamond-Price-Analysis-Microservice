[![Python application test with Github Actions](https://github.com/nogibjj/Project-1-Jiaxin-Ying-/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Project-1-Jiaxin-Ying-/actions/workflows/main.yml)

# Project-4-Cloud-based Big Data Systems

## Demo Video Link

## Structure Diagram

## Key Objectives of Project
The goal of this project is to showcase the use of a large data platform, specifically Databricks on Azure, for data engineering tasks. The dataset used is from Kaggle (https://www.kaggle.com/datasets/shivam2503/diamonds) and contains information about diamonds, including price, carat weight, cut quality, color, clarity, and physical dimensions.

The specific objective of the project is to use SQL to extract information from the dataset and find the average price of diamonds for each different color. This information will then be used to build a functional web microservice using Python and FastAPI, which will allow users to easily view the average prices for different diamond colors.

The significance of this project lies in its demonstration of how a large data platform like Databricks on Azure can be used to efficiently process and analyze large datasets. The use of SQL to extract data from the dataset and Python to build a web microservice highlights the versatility and power of these tools in data engineering. Additionally, the insights gained from this project can be useful for those in the diamond industry, such as diamond sellers or buyers, as they can use the information to make informed decisions about pricing and purchasing.

## Connect Codespace and Databricks
1. Create an account on the Azure portal (https://portal.azure.com/)
2. Go to the Azure Databricks Marketplace page (https://azuremarketplace.microsoft.com/en-us/marketplace/apps/databricks.databricks) to create an Azure Databricks workspace
<img width="726" alt="Screen Shot 2023-03-27 at 6 42 22 PM" src="https://user-images.githubusercontent.com/112274822/228088935-b64bb6ee-8dd7-4512-956c-60f14ffe325a.png">

3. Configure the workspace settings, such as subscription, resource group, workspace name, and pricing tier. Once the workspace is created, go to the Azure Databricks portal (https://<your-workspace-url>.azuredatabricks.net/) and sign in using your Azure credentials, or you can click the "Launch Workspace" directly to login.
<img width="1172" alt="Screen Shot 2023-03-27 at 6 48 32 PM" src="https://user-images.githubusercontent.com/112274822/228089126-ad697ded-7009-4c6b-8178-790f63af9417.png">

4. In the Azure Databricks portal, click on "Compute" in the left-hand menu
<img width="263" alt="Screen Shot 2023-03-27 at 6 59 17 PM" src="https://user-images.githubusercontent.com/112274822/228089236-298b9e4c-e3b2-4bfa-a164-883104749afa.png">

5. Click on "Create compute" to create a new cluster
<img width="496" alt="Screen Shot 2023-03-27 at 6 59 27 PM" src="https://user-images.githubusercontent.com/112274822/228089307-8cdf7e36-dae1-470a-b5d3-bc11d4912ff2.png">

6. Configure the cluster settings, such as cluster name, cluster mode, and node type, make sure you choose "Single node"
<img width="891" alt="Screen Shot 2023-03-27 at 6 59 45 PM" src="https://user-images.githubusercontent.com/112274822/228089359-42f888e4-b49c-4fed-9fd9-a848ba3f3b5d.png">

7. In the Azure Databricks portal, click on "Admin Setting" in the right-hand menu, go to "Workspace Setting", then choose "enable" the DBFS File Broswer
<img width="422" alt="Screen Shot 2023-03-27 at 7 00 55 PM" src="https://user-images.githubusercontent.com/112274822/228089952-153059c8-831d-48f2-86bb-2a7fcf57d8e8.png">
<img width="896" alt="Screen Shot 2023-03-27 at 7 01 22 PM" src="https://user-images.githubusercontent.com/112274822/228090087-033063a7-5cc0-4a7f-b3e3-0a7fe75243d9.png">
<img width="811" alt="Screen Shot 2023-03-27 at 7 01 42 PM" src="https://user-images.githubusercontent.com/112274822/228090133-5c0fbddf-542c-413e-ad70-9a867fff5ed5.png">
Enabling the DBFS File Browser in the Azure Databricks Workspace Settings allows users to easily navigate and access files stored in the Databricks File System (DBFS) using a graphical interface. The DBFS File Browser provides a familiar directory tree structure and allows users to upload, download, and manage files and folders within the DBFS directly from the workspace.

8. In the Azure Databricks portal, click on "User Setting" in the right-hand menu, then click "Genereate new token", wou can then use this access token to authenticate our Codespace when connecting to our Databricks workspace using Databricks Connect.
<img width="1451" alt="Screen Shot 2023-03-27 at 7 03 05 PM" src="https://user-images.githubusercontent.com/112274822/228089886-f4963629-577f-4d3f-b969-c4445620f7e7.png">
<img width="503" alt="Screen Shot 2023-03-27 at 7 04 12 PM" src="https://user-images.githubusercontent.com/112274822/228090382-4022cbc4-7478-435a-b582-cae64f34738c.png">

9. Go back to "compute", then find the JDBC and ODBC information after clicking on the "Advanced Options" tab, scroll down to the "JDBC/ODBC" section of our created cluster
<img width="882" alt="Screen Shot 2023-03-27 at 7 00 16 PM" src="https://user-images.githubusercontent.com/112274822/228091003-300af159-1eea-4087-867f-ba25ddf63079.png">

9. Go to Github Seetings, then find the button in "security", choose "secrets and variables", create 4 token: DATABRICKS_HOST, DATABRICKS_HTTP_PATH, DATABRICKS_SERVER_HOSTNAME and DATABRICKS_TOKEN by copy link from databricks.
<img width="1193" alt="Screen Shot 2023-03-27 at 7 04 01 PM" src="https://user-images.githubusercontent.com/112274822/228090837-33d85dd9-3cce-4e5f-b7d1-2176ece7c7e8.png">

Note that our link should follow below information when create the token at Github:
<img width="842" alt="Screen Shot 2023-03-24 at 6 57 09 PM" src="https://user-images.githubusercontent.com/112274822/228091391-b804391d-e4fc-4d2a-903b-20178fcbf3ab.png">

