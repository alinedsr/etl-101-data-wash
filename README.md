# ETL 101: Data Wash 🧼🚀  

## Project Description  
This project is a **basic ETL (Extract, Transform, Load) pipeline** focused on **data cleaning** using Python and Pandas. The goal is to take a messy dataset, apply **data transformation steps**, and prepare it for analysis or storage in a database.  

## Features  
✅ Handle missing values (fill or remove)  
✅ Remove duplicate records  
✅ Standardize column names  
✅ Normalize text formats (uppercase/lowercase)  
✅ Save cleaned data as CSV  

## Tech Stack  
- 🐼 **Pandas** – Data manipulation  
- 🐍 **Python** – Core scripting  
- 🗄 **CSV** – Input & output format  

## How to Use  
1. Clone the repository:  
   ```bash
   git clone https://github.com/alinedsr/etl-101-data-wash
   cd etl-101-data-wash

2. Install dependencies using Poetry:
   ```bash
   poetry install

3. Run the script:
   ```bash
   poetry run python clean_data.py

4. Check the output in the output/ folder.


## Next Steps
🔹 Automate the process with Apache Airflow
🔹 Store cleaned data in a database (MySQL, Snowflake)
🔹 Add unit tests for data validation