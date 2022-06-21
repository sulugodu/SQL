Description
 
The project is developed for solving SQL task. 


**INSTALLATION**

1. Python version: 3.7 
1. Please install Docker.

The required packages are listed in the requirements.txt. Install the
packages as below.
 
`pip install -r requirements.txt`


**Project description:**

**Setup a pod or isolated container comprising a SQL Database**

I am using docker containers as a micro service for hosting mysql server.\
Setting up an isolated mysql server and all required environment variables
are defined in `docker-compose.yml`. 

Start sql server by the command \
`docker compose up` 

Mysql server will be running at `@localhost:33060`. \

**Main_module:**  `main.py` 

The main script starts connection with mysql server, imports data to
database, reads data from database and generates KPI values into csv file. Please refer to function `task_run()` in the `main.py`.

The order of execution is as below.

*task 1 Import testset_B.tsv into the SQL DB* \
*task 2 Reads data from SQL DB* \
*a. Ranks based on column “Price”, grouped by column “brand”* \
*b. Minimum and maximum of column “HDD_GB”* \
*c. Median of column “GHz”, grouped by column “RAM_GB”* 

Run the main script.\
`python main.py` 

Three csv file will be generated.

1. Ranks based on column “Price”, grouped by column “brand”(rank based on
 max price of each brand): `rank.csv`. 
2. Minimum and maximum of column “HDD_GB”: `min_max.csv`.
3. Median of column “GHz”, grouped by column “RAM_GB”: `median.csv`.


**Python module description**

`database.py` : Contains functions for inserting data to sql database.\
`database_parameters.py` : Database parameters needed for sql connection.\
`db_utils.py` : Scripts for importing and reading data from sql database.\
`main.py` : Main script for generating the KPI results
 







      
      