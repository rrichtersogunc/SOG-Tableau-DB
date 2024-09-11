# UNC SOG Tableau Usage Statistics Project

To maintain a well-functioning Tableau workspace at the School of Government a life-cycle model was developed to provide feedback on which components can be kept and which can be archived. This will keep out workspace easy to navigate and tidy. Workbooks that haven’t been viewed in 15 months would be put on the list to be reviewed by stakeholders for archival. Data sources that haven’t been used in 15 months and have no connected workbooks would similarly be placed on an archive list to be reviewed by stakeholders. Visualizations that take longer than 10 seconds to load would also be put on a list for performance tuning. We also need to know the full path to the workbooks and data sources. 

We want to know if the Tableau REST API can give us the above data. If it can, we like to add it to out data warehouse and update it regularly. A report would then be created to allow the above components to be identified and acting on. 

* [Get started with the Development Environment](docs/get_started.md)

## Requirements

* Workbook usage in last 15 months
* Datasource usage in last 15 months
* For each datasource, find the connected workbooks. 
* Visualization load times (Not Implemented)

## Developer Docs
* [Database concerns and creation](docs/database.md)
* [Tableau API methods and data retrieval](docs/tableau_api.md)

## Feature Docs
* [Technical Specification Document](docs/tech_spec.md)

### Authored and developed by Mustafa Aljumayli - 07/24/2024