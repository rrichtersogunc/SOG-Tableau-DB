# Tableau Usage Statistics Data Pipeline Technical Specifications

## Author(s)
- [Mustafa Aljumayli](https://github.com/id-mustafa)

## Description
This document contains the technical specifications for the data pipeline addition to the UNC School of Government's data warehouse. This feature adds _3_ new database tables, _5_ new API routes, and _1_ new task-scheduled script to the data warehouse.

The Tableau Usage Statistics Data Pipeline provides a new way to funnel usage statistics for our Tableau site to SQL; this addition to the data warehouse will boost efficiency and cut down on the cost of hosting data that isn't being utilized by the school.

All analysts and data engineers will now have a new dataset to build future systems with.

### Project Requirements:
* Workbook usage in last 15 months
* Datasource usage in last 15 months
* For each datasource, find the connected workbooks. 

## Table of Contents

- [Design Choices](#Design)
  - [Technical Choices](#TechnicalDesign)
  - [Personas](#Personas)
  - [User Stories](#UserStories)
- [Development Concerns](#DevelopmentConcerns)
- [For Future Developers](#FutureDevs)
- [Backend Design and Implementation](#BackendDesign)
  - [Database/Entity-Level Representation Decisions](#EntityDesign)
  - [API Routes](#API)
  - [Backend Service Methods](#BackendService)
  - [Testing](#Testing)

## Design Choices <a name='Design'></a>

### Technical Choices <a name='TechnicalDesign'></a>

The ultimate decision for the project's structure was to create one Jupyter Notebook that can be run daily on a schedule with CRON. Another design choice was to implement the `connections_list` table. This option was weighed against the possibility of a hits table, but the first option made more sense as it revealed more insights about our site. The chosen system design consisted of three SQL tables: `connections_list`, `workbook_list`, `datasource_list`.

### Personas <a name='Personas'></a>

* Andy Admin - an admin for a data warehouse looking to bring more flexible data into SQL tables from Tableau's APIs

### User Stories <a name='UserStories'></a>

* As Andy Admin, I would like to track Tableau usage statistics for workbooks and datasources within the last 15 months.

* As Andy Admin, I would like to keep track of the number of connected workbooks per datasource.

* As Andy Admin, I would like to have an ETL data pipeline script that can be scheduled to run daily with CRON.

## Development Concerns <a name='DevelopmentConcerns'></a>

In future development, consider these possible improvements to this data pipeline feature:

- Implementing a more detailed logging system for tracking data extraction and transformation processes.
- Adding automated testing for the data pipeline to ensure data integrity and pipeline reliability.
- Exploring optimization techniques to enhance the performance of data extraction and loading processes.
- Addition of more tables into the script such as a database table, owner table, and project table for more flexibility.

## For Future Developers <a name='FutureDevs'></a>

Convert the parsed data within this script to a dataframe with a data pipelining framework such as Pandas or Polars. Research was conducted and for the application of this script Polars should be the best option due to its performance boost over Pandas. Consider collecting more data as time goes on with this script. Adding more tables would be much easier to do as the ETL process is already nicely laid out for you. Consider using a combination of both, the REST and Metadata API offered by Tableau. As long as the data is able to be parsed, you can maximize the amount of data you get from Tableau. Consider finding the load times for the Tableau API. 

## Backend Design and Implementation <a name='BackendDesign'></a>

We implemented new table entries to hold Tableau usage statistics. Each record is mapped to relevant entities to denote the relationships and usage statistics.

### Database/Entity-Level Representation Decisions <a name='EntityDesign'></a>

```sql
CREATE TABLE connections_list (
    connection_id VARCHAR(255) PRIMARY KEY,
    is_certified TINYINT(1),
    certifier_id VARCHAR(255),
    certifier_name VARCHAR(255),
    certified_display_name VARCHAR(255),
    database_id VARCHAR(255),
    database_name VARCHAR(255),
    extract_last_refresh_time DATETIME,
    datasource_id VARCHAR(255),
    datasource_name VARCHAR(255),
    workbook_id VARCHAR(255),
    workbook_name VARCHAR(255),
    date_extracted DATETIME,
    last_updated DATETIME
);

CREATE TABLE workbook_list (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    content_url TEXT,
    webpage_url TEXT,
    show_tabs BOOLEAN,
    size INT,
    created_at DATETIME,
    updated_at DATETIME,
    encrypt_extracts BOOLEAN,
    default_view_id VARCHAR(255),
    project_id VARCHAR(255),
    project_name VARCHAR(255),
    owner_id VARCHAR(255),
    owner_name VARCHAR(255),
    hits_total INT,
    hits_last_two_weeks_total INT,
    hits_last_one_month_total INT,
    hits_last_three_months_total INT,
    hits_last_twelve_months_total INT,
    date_extracted DATETIME,
    last_updated DATETIME
);

CREATE TABLE datasource_list (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    content_url TEXT,
    webpage_url TEXT,
    size INT,
    created_at DATETIME,
    updated_at DATETIME,
    encrypt_extracts BOOLEAN,
    project_id VARCHAR(255),
    project_name VARCHAR(255),
    owner_id VARCHAR(255),
    owner_name VARCHAR(255),
    has_extracts BOOLEAN,
    is_certified BOOLEAN,
    use_remote_query_agent BOOLEAN,
    hits_total INT,
    hits_last_two_weeks_total INT,
    hits_last_one_month_total INT,
    hits_last_three_months_total INT,
    hits_last_twelve_months_total INT,
    connected_workbooks INT,
    date_extracted DATETIME,
    last_updated DATETIME
);
```
### API Routes <a name='API'></a>
The data pipeline feature adds 5 new API routes for extracting and updating data.

### Backend Service Methods <a name='BackendService'></a>
We implemented the following service methods to facilitate interactions between API calls and the database. For full implementation, reference the backend service code.

```python

def get_tableau_token(username, password, content_url):
    """Fetches the authentication token and returns it."""
    
def get_workbooks(token):
    """Fetches all workbooks from Tableau API, parses, and returns them."""

def get_wb_usage_statistics(token, workbook_id):
    """Fetches workbook hits from Tableau API, parses, and adds it to the list of workbooks."""

def get_datasources(token):
    """Fetches all data sources from Tableau API and returns them."""

def get_ds_usage_statistics(token, datasource_id):
    """Fetches datasource hits from Tableau API, parses, and adds it to the list of datasources."""

def get_connections(token):
    """Fetches connections using Tableau Metadata API and returns them."""

def parse_connections_data(response):
    """Parses connections data from API response."""

def insert_datasources(sqlconnection, datasources):
    """Inserts parsed datasource data into the MySQL database."""

def insert_workbooks(sqlconnection, workbooks):
    """Inserts parsed workbook data into the MySQL database."""

def insert_connections(sqlconnection, connections):
    """Inserts parsed connections data into the MySQL database."""
```

### Testing <a name='Testing'></a>
All of the service methods have thorough testing and ensure data integrity and reliability. Each service method is directly tested to cover various scenarios and edge cases. The testing ensures that the data pipeline works as expected and handles errors gracefully.