# ETL-101-Data-Wash 🧼🚀  

## 📌 Project Description  
This project is a **modular ETL pipeline** designed to extract, clean, and save a dataset from Kaggle. The dataset used is from **Spotify**, and the goal is to process raw data into a structured format ready for analysis.  

The pipeline follows a standard ETL process:  
✅ **Extract** – Download data from Kaggle  
✅ **Transform** – Clean and preprocess the dataset  
✅ **Load** – Save the cleaned dataset for further analysis  

---

## 📂 Project Structure  
```
etl-101-data-wash/
│── app/
│   ├── extract.py   # Downloads dataset from Kaggle
│   ├── transform.py # Cleans and preprocesses data
│   ├── load.py      # Saves the cleaned dataset
│── data/
│   ├── processed/   # Folder for cleaned data
│   ├── raw/         # Folder for raw data
│── main.py          # Orchestrates the entire ETL process
│── poetry.lock
│── pyproject.toml
│── README.md
```

---

## 🛠️ Tech Stack  
- 🐍 **Python** – Core programming language  
- 📦 **Poetry** – Dependency management  
- 📊 **Pandas** – Data manipulation  
- 💾 **Kaggle API** – Dataset extraction  

---

## 🚀 How to Run  

### **1️⃣ Install Dependencies**  
Ensure you have **Poetry** installed, then run:  
```bash
poetry install
```

### **2️⃣ Configure Kaggle API**  
If you haven't set up the Kaggle API yet, follow these steps:  
1️⃣ Go to [Kaggle Account](https://www.kaggle.com/settings)  
2️⃣ Scroll to the **API** section and click **Create New Token**  
3️⃣ Move the downloaded `kaggle.json` file to:  
   - **Linux/Mac**: `~/.kaggle/kaggle.json`  
   - **Windows**: `C:\Users\YOUR_USER\.kaggle\kaggle.json`  
4️⃣ Set permissions (Linux/Mac only):  
```bash
chmod 600 ~/.kaggle/kaggle.json
```

### **3️⃣ Run the ETL Pipeline**  
To execute the complete ETL process, run:  
```bash
poetry run python main.py
```

This will:  
✔️ Download the dataset  
✔️ Clean and preprocess the data  
✔️ Save the cleaned dataset in `data/processed/spotify_cleaned.csv`

---

## 📊 Output Data  
The cleaned dataset is saved in:  
```
data/processed/spotify_cleaned.csv
```
This file is ready for analysis and further processing.  

---

## 🌟 Next Steps  
🔹 Automate execution with Apache Airflow  
🔹 Store cleaned data in a cloud database (Snowflake, BigQuery)  
🔹 Add data validation checks  

---

## 📜 License  
This project is open-source and available under the **MIT License**. Feel free to use and contribute!  

---

🚀 **Happy Data Cleaning!** 🧼📊