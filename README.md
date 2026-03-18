# databasePipelineETL
A lean and simple ETL pipeline for extracting from different database environments, transforming them, and loading them in a centralized database.

## INTRODUCTION
>This is a project done by a solo developer, expect unoptimized code, and messy spaghetti code, and TONS of it.

This project is created to migrate and integrate all production servers in the company, as of writing the company currently makes use of 4 production line servers with 1 central server.

The main goal is to have all 4 sub servers feed data into the central server for future projects.

![diagram](docs/images/diagram.svg)

The concept of the project is shown above, 4 different database environment to be compiled and stored in a central database for more streamlined flow if information.

## TOOLS
As the project touches on database manipulation, python is mainly used for this project as it offers the best libraries and dependencies on interacting with multiple different database environments, mainly MySQL, PostgreSQL, and MSSQL.

### INSTALLATION
>You need to have pip installed in order to have dependencies work

> make sure you are in the project folder root

Verify that Python is installed:
`pip --version`

Verify that pip is installed:
`pip --version`

#### It is recommended that you use a virtual environment to avoid dependency issues

Install required dependencies:
`pip install -r requirements.txt`

> more installation instructions to come.

