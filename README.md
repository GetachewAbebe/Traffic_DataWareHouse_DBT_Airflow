Data Engineering Challenge: Scalable Data Warehouse for City Traffic Analysis
Introduction
You have been tasked with creating a scalable data warehouse to host vehicle trajectory data collected by swarm drones and static roadside cameras in a city. The data warehouse should be designed to support efficient querying by downstream projects and take into account future needs. You will be using the Extract, Load, Transform (ELT) framework with dbt to set up the data transformation workflows.

Tasks
1. Set up the Data Warehouse Infrastructure
Choose a suitable database management system (e.g., PostgreSQL) to serve as the data warehouse.
Set up the database and create the necessary tables to store the vehicle trajectory data.
Dockerize the entire data warehouse infrastructure, including the database, to ensure consistent and scalable deployment.
2. Create an Airflow DAG for Data Ingestion
Use the Airflow framework to create a DAG (Directed Acyclic Graph) that handles the data ingestion process.
Implement the DAG to extract the data files from the provided source (pNEUMA dataset), load them into the data warehouse, and handle any necessary data transformations.
Separate the DAG into distinct environments (Prod, Dev, Staging) to ensure proper data management and versioning.
Implement automated alerting mechanisms, such as Slack or email notifications, to notify you of any DAG failures.
3. Set up dbt for Data Transformation
Connect dbt to your data warehouse and write transformation code for the vehicle trajectory data.
Ensure that the transformations are well-documented and easily accessible through the dbt docs UI.
Explore additional dbt modules, such as great_expectations or re-data, to implement data quality monitoring and testing.
4. Integrate Redash for Reporting
Set up Redash, a open-source business intelligence and visualization tool, to connect to your data warehouse.
Create a dashboard that displays relevant insights and visualizations based on the vehicle trajectory data.
Automate the process of generating and storing the Redash queries using version control (e.g., Git) to ensure reproducibility and maintainability.
5. Document and Showcase Your Approach
Write a short article (around 500-800 words) that discusses your approach, the key decisions you made, and the challenges you faced during the implementation.
Highlight the benefits of the chosen architecture, the advantages of the ELT framework, and the importance of integrating various data engineering tools (Airflow, dbt, Redash) to create a robust and scalable data platform.
Deliverables
A fully dockerized data warehouse infrastructure, including the database, Airflow, dbt, and Redash.
The Airflow DAG(s) responsible for data ingestion, with proper separation of environments and automated alerting mechanisms.
The dbt transformation code, with comprehensive documentation and access to the dbt docs UI.
The Redash dashboard and the automated process for storing and versioning the Redash queries.
A short article (500-800 words) that showcases your approach and the key decisions made throughout the implementation.
Resources
pNEUMA dataset: https://zenodo.org/records/7426506
References for understanding the data generation:
PIA15_poster.pdf (datafromsky.com)
(PDF) Automatic vehicle trajectory extraction for traffic analysis from aerial video data (researchgate.net)
GitHub packages for data visualization and interaction:
tud-hri/travia: a Traffic data Visualization and Annotation tool (github.com)
JoachimLandtmeters/pNEUMA_mastersproject (github.com)