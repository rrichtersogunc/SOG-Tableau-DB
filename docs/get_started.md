# To get started, lets install all dependencies:
## run 'pip install pymysql requests python-dotenv'

## Author(s)
- [Mustafa Aljumayli](https://github.com/id-mustafa)

## Description of the program
This is an ETL Data pipeline that grabs usage statistics from Tableau's REST and Metadata APIs and loads them into a MySQL database. The process is simply outlined below:

#### Extract: Write the API request or GraphQL query that'll get the information from Tableau
#### Transfrom: Parse the API's response and define each piece of data as a Python variable.
#### Load: Load the Python variables from the dictionary to 3 tables within the MySQL database, workbook_list, datasource_list, and connections_list.

## Description of the File Structure

### [Documentation Folder](../docs/)
The 'docs' folder houses all the information pertaining to the project readily accessible for any developer or analyst to browse. In here, you can find 4 files explaining different parts of the project. Here are the files and a brief description of each:

#### [Getting Started File](./get_started.md)
The get_started.md file is currently your introductory tutorial for all you need to get started.

#### [Database File](./database.md)
The database.md file is where you can find all the information about the database connection, schema, and system design.

#### [Tableau API File](./tableau_api.md)
The tableau_api.md file is where you can find all the information about the APIs used in this program. 

#### [Technical Specification Document](./tech_spec.md)
The tech_spec.md file is where you can find the use cases, user stories, and design choices for the project.

### [Environment Variables File](../.env)
For new users, this is where your attention needs to be. The .env file is where you can place all of your sensitive environment variables. There should also be a .gitignore file that keeps the .env file from being pushed to any github repository so that your information never gets leaked. This file should follow the model below exactly as this is what's used in the main program. Make sure to save the file once all variables are set.

* MODE=development
* MYSQL_USER = YOUR_MASTER_DB_USERNAME
* MYSQL_PASSWORD = YOUR_MASTER_DB_PASSWORD
* MYSQL_HOST = YOUR_DB_HOSTNAME
* MYSQL_PORT = YOUR_DB_PORT
* MYSQL_DATABASE = YOUR_DB_NAME (Do not confuse this with the database identifier. You must create a database in your MySQL Server with this name.)
* TABLEAU_API_URL = https://tableau.example.edu/api/3.21
* TABLEAU_SERVER_URL = https://tableau.example.edu 
* TABLEAU_API_URL = {TABLEAU_DOMAIN_URL}/api/{api_version}
* TABLEAU_USERNAME = YOUR_TABLEAU_USERNAME
* TABLEAU_PASSWORD = YOUR_TABLEAU_PASSWORD
* TABLEAU_CONTENT_URL = YOUR_CONTENT_URL (Obtained from the Tableau server url once signed into Tableau)

### [Environment Variable Getter File](../env.py)
The env.py file contains a getter method that retrieves your environment variables from the .env file and calls it in your main file. There is a terminal command to run the env.py file for you in the first cell but in case this fails, just run the file to load all environment variables.

### [Main Jupyter Notebook File](../env.py)
The main.ipynb file houses the entire program, running this file will allow you to run the ETL data pipeline from start to finish. The first couple cells are about authentication and creating the tables if they don't happen to exist already. Then the transformation process will parse and store the response data into a python dictionary that serves as the model for how the data will be loaded into the SQL table.

### [README File](../README.md)
This file serves as the primary introduction point and hub for the project. It will give you a brief background of the project and outline the project's requirements. It'll also guide you to project documentation.

### [Git Ignore File](../.gitignore)
Due to the project's nature of dealing with potentially sensitive information, any file that you would like to not be uploaded onto GitHub as it contains sensitive data, you can place it in the .gitignore file to keep the machine locally. Keep in mind. You cannot pull any file from an online repository to your local machine if it has been listed in your .gitignore file.

## This is all you need to get started with this data pipeline. Enjoy!

__authors__ = [
    "Mustafa Aljumayli"
]