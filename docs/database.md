# Database Connection and System Design Information

## Author(s)
- [Mustafa Aljumayli](https://github.com/id-mustafa)

## Database Connection
To establish a connection to your MySQL Database, we use the pymysql framework. In main.ipynb, you'll see a cell that will allow you to establish this connection. Below is the code segment you can expect to see. Each field of the connection is encompassed in the .env file.

sqlconnection = pymysql.connect(
    host=getenv('MYSQL_HOST'),
    user=getenv('MYSQL_USER'),
    password=getenv('MYSQL_PASSWORD'),
    port=int(getenv('MYSQL_PORT')),
    database=getenv('MYSQL_DATABASE')
)

## [System Design](../public/Tableau%20Data%20Pipeline%20Project.mwb)
The system design was heavily influenced by the project's requirements. So to fully understand the schema, we should understand the project requirements below:

* Workbook usage in last 15 months
* Datasource usage in last 15 months
* For each datasource, find the connected workbooks. 

Workbook and datasource usage was captured using the [Tableau REST API](./tableau_api.md), more specifically, the [Get Usage Statistics for Content Item](https://help.tableau.com/current/api/rest_api/en-us/REST/TAG/index.html#tag/Content-Exploration-Methods/operation/UsageStatsService_GetUsageStats) API request. 

There are 3 tables that have been designed to tackle each requirement:

* workbook_list 
* datasource_list
* connections_list

There also exists Entity relationships between each table. 

* There is a one-to-many relationship between the workbook_list and the connections_list tables as a workbook may have many connections.

* There is a one-to-many relationship between the datasource_list and connections_list tables as a data source may have many connections.

* By definition, there is a many-to-many relationship between workbooks and datasources as a workbook may be connected to many datasources and a datasource may be connected to many workbooks.

![Database E-R Diagram](../public/Pipeline%20Project%20Schema.png)

## Database Schema
### Fields Description for the workbook_list SQL Table
* id: Same as the workbook luid in Tableau's schema (Primary Key)

* name: Same as the workbook name in Tableau's schema

* description: Same as the workbook description in Tableau's schema

* content_url: Same as the workbook contentUrl in Tableau's schema, the content_url for a workbook is a string that represents the URL path for accessing the workbook within Tableau Server. This URL is often used to directly navigate to the workbook in a web browser.

* webpage_url: Same as the workbook webpageUrl in Tableau's schema, the webpage_url for a workbook is a complete URL that can be used to directly navigate to the workbook in a web browser. 

* show_tabs: Same as the workbook showTabs field in Tableau's schema, the showTabs attribute for a workbook indicates whether the workbook displays sheet tabs at the bottom. When showTabs is set to true, Tableau Server or Tableau Online will display tabs for each sheet (worksheet, dashboard, or story) in the workbook, allowing users to navigate between them easily. When showTabs is set to false, the tabs are hidden, and users typically navigate between sheets using other navigation elements, such as links or buttons embedded in dashboards or stories.

* size: Same as the workbook size in Tableau's schema, the size attribute for a workbook typically represents the size of the workbook in megabytes (MB).

* created_at: Same as the workbook's createdAt date in Tableau's schema, the createdAt attribute under workbooks represents the timestamp when the workbook was initially created.

* updated_at: Same as the workbook's updatedAt date in Tableau's schema, the updatedAt attribute under workbooks represents the timestamp when the workbook was last updated.

* encrypt_extracts: Same as the workbook's encryptExtracts in Tableau's schema, the encryptExtracts attribute under workbooks refers to whether the data extracts associated with the workbook are encrypted.

* default_view_id: Same as the workbook's defaultViewId in Tableau's schema, the defaultViewId attribute under workbooks refers to the identifier of the default view (worksheet, dashboard, or story) that is opened when the workbook is accessed.

* project_id: Same as the workbook's projectId in Tableau's schema, the projectId in Tableau's API refers to the unique identifier of the project that contains the workbook or datasource.

* project_name: Same as the workbook's projectName in Tableau's schema, the projectName in Tableau's API refers to the name of the project that contains the workbook or datasource.

* owner_id: Same as the workbook's ownerId in Tableau's schema, the ownerId refers to the unique identifier of the user who owns the workbook or datasource.

* owner_name: Same as the workbook's ownerName in Tableau's schema,  the ownerName refers to the name of the user who owns the workbook.

* hits_total: Same as the workbook's hitsTotal in Tableau's schema, hitsTotal typically refers to the total number of times a datasource, workbook, or view has been accessed.

* hits_last_two_weeks_total: Same as the workbook's hitsLastTwoWeeksTotal in Tableau's schema, hitsLastTwoWeeksTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last two weeks.

* hits_last_one_month_total: Same as the workbook's hitsLastOneMonthTotal in Tableau's schema, hitsLastOneMonthTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* hits_last_three_months_total: Same as the workbook's hitsLastThreeMonthsTotal in Tableau's schema, hitsLastThreeMonthsTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* hits_last_twelve_months_total: Same as the workbook's hitsLastTwelveMonthsTotal in Tableau's schema, hitsLastTwelveMonthsTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* date_extracted: Field that was created to keep track of when the record was established in the database.

* last_updated: Field that was created to keep track of when the record was last updated in the database. 

### Fields Description for the datasource_list SQL Table
* id: Same as the datasource luid in Tableau's schema (Primary Key).

* name: Same as the datasource name in Tableau's schema.

* description: Same as the datasource description in Tableau's schema.

* content_url: Same as the datasource contentUrl in Tableau's schema, the content_url for a datasource is a string that represents the URL path for accessing the datasource within Tableau Server. This URL is often used to directly navigate to the datasource in a web browser.

* webpage_url: Same as the datasource webpageUrl in Tableau's schema, the webpageUrl for a datasource is a complete URL that can be used to directly navigate to the datasource in a web browser. 

* size: Same as the datasource size in Tableau's schema, the size attribute for a datasource typically represents the size of the datasource in megabytes (MB).

* created_at: Same as the datasource's createdAt date in Tableau's schema, the createdAt attribute under datasources represents the timestamp when the datasource was initially created.

* updated_at: Same as the datasources's updatedAt date in Tableau's schema, the updatedAt attribute under datasources represents the timestamp when the datasources was last updated.

* encrypt_extracts: Same as the datasource's encryptExtracts in Tableau's schema, the encryptExtracts attribute under datasources refers to whether the data extracts associated with the datasources are encrypted.

* project_id: Same as the datasource's projectId in Tableau's schema, the projectId in Tableau's API refers to the unique identifier of the project that contains the datasource.

* project_name: Same as the datasource's projectName in Tableau's schema, the projectName in Tableau's API refers to the name of the project that contains the datasource.

* owner_id: Same as the datasource's ownerId in Tableau's schema, the ownerId refers to the unique identifier of the user who owns the datasource.

* owner_name: Same as the datasource's ownerName in Tableau's schema,  the ownerName refers to the name of the user who owns the datasource.

* has_extracts: Same as the datasource's hasExtracts in Tableau's schema, the hasExtracts under datasources indicates whether a datasource contains extracts.

* is_certified: Same as the datasource's isCertified in Tableau's schema, the isCertified is a boolean field that indicates whether a datasource has been certified by site admins.

* use_remote_query_agent: Same as the datasource's useRemoteQueryAgent in Tableau's schema, the useRemoteQueryAgent is a boolean field associated with datasources. This field indicates whether the datasource is configured to use Tableau's Remote Query Agent (RQA). 

* hits_total: Same as the datasource's hitsTotal in Tableau's schema, hitsTotal typically refers to the total number of times a datasource, workbook, or view has been accessed.

* hits_last_two_weeks_total: Same as the workbook's hitsLastTwoWeeksTotal in Tableau's schema, hitsLastTwoWeeksTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last two weeks.

* hits_last_one_month_total: Same as the workbook's hitsLastOneMonthTotal in Tableau's schema, hitsLastOneMonthTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* hits_last_three_months_total: Same as the workbook's hitsLastThreeMonthsTotal in Tableau's schema, hitsLastThreeMonthsTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* hits_last_twelve_months_total: Same as the workbook's hitsLastTwelveMonthsTotal in Tableau's schema, hitsLastTwelveMonthsTotal refers to the total number of times a datasource, workbook, or view has been accessed in the last month (approximately the last 30 days).

* connected_workbooks: Field that was created to keep track of how many workbooks are connected per datasource.

* date_extracted: Field that was created to keep track of when the record was established in the database.

* last_updated: Field that was created to keep track of when the record was last updated in the database. 

### Fields Description for the connections_list SQL Table

* connection_id: A unique identifier for the connection, combining datasource ID and workbook ID. It is formed by concatenating the datasource ID and workbook ID, ensuring uniqueness for each connection. (<datasource_id>_<workbook_id>)

* is_certified: This boolean field indicates whether the datasource has been certified by site admins. In Tableau's schema, the isCertified field under datasources represents this value.

* certifier_id: The unique identifier of the user who certified the datasource, if available. This corresponds to the certifier.luid in Tableau's schema under datasources.

* certifier_name: The name of the user who certified the datasource, if available. This corresponds to the certifier.name in Tableau's schema under datasources.

* certified_display_name: The display name of the certifier, which might be used for easier recognition in the user interface. This corresponds to the certifierDisplayName in Tableau's schema under datasources.

* database_id: The unique identifier of the database associated with the datasource, if available. This corresponds to the upstreamDatabases.luid in Tableau's schema under datasources.

* database_name: The name of the database associated with the datasource, if available. This corresponds to the upstreamDatabases.name in Tableau's schema under datasources.

* extract_last_refresh_time: The timestamp when the extract associated with the datasource was last refreshed. This corresponds to the extractLastRefreshTime in Tableau's schema under datasources.

* datasource_id: The unique identifier of the datasource. This corresponds to the luid in Tableau's schema under datasources. (foreign key)

* datasource_name: The name of the datasource. This corresponds to the name in Tableau's schema under datasources.

* workbook_id: The unique identifier of the workbook that uses the datasource. This corresponds to the downstreamWorkbooks.luid in Tableau's schema under datasources. (foreign key)

* workbook_name: The name of the workbook that uses the datasource. This corresponds to the downstreamWorkbooks.name in Tableau's schema under datasources.

* date_extracted: A custom field created to keep track of when the record was established in the database. This is typically set to the current date and time when the data is inserted into the database.

* last_updated: A custom field created to keep track of when the record was last updated in the database. This is typically set to the current date and time when the data is updated in the database.

__authors__ = [
    "Mustafa Aljumayli"
]