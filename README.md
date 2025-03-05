# Marvel Data Pipeline

[![Character Count Image](architecture/count.png)](architecture/count.png)

This project is a data pipeline crafted to extract, transform, and load Marvel comic book data, then analyze and visualize it. We use Python, SQLite3, and a few other tools to make this happen.

## Project Structure
Here's how the project files and folders are organized:

    MarvelDataPipeline/
    ├── Comic_Character_Analysis.ipynb     # Jupyter Notebook for data analysis
    ├── DataLayer/
    │   ├── DataService.py                  # Handles SQLite database interactions
    │   └── pycache/                  # Compiled Python files
    ├── ETLApp.py                         # Executes the ETL pipeline
    ├── LICENSE                           # Project license
    ├── Models/
    │   └── Comic.py                      # Data model for comic book info
    ├── README.md                          # This file
    ├── ResultSQL/
    │   └── ResultSQL.sql                 # SQL result data
    ├── SSLcheck.py                       # Checks SSL certificates
    ├── Services/
    │   ├── ComicService.py                 # Interacts with comic data
    │   └── pycache/                  # Compiled Python files
    ├── Utils/
    │   ├── Config.py                     # Manages configuration settings
    │   └── pycache/                  # Compiled Python files
    ├── architecture/
    │   ├── DataPipeline.png              # Data Pipeline Diagram
    │   ├── DataPipline.png               # (Typo) Data Pipeline Diagram
    │   ├── count.png                     # Character count result
    │   ├── drawing.png                   # Data Flow Diagram
    │   └── eclidrawpipeline0.png         # Project Data Pipeline Diagram
    ├── character_comic.sql.sqbpro       # SQLiteStudio project file
    ├── cronjob.sh                        # Shell script to run ETL (with venv)
    ├── data_service.log                  # Log file for data service operations
    ├── logs/
    │   └── dbt.log                       # dbt log file
    ├── marvel_dbt/
    │   ├── README.md                     # dbt project README
    │   ├── analyses/                     # dbt analysis files
    │   ├── dbt_project.yml                # dbt project configuration
    │   ├── macros/                       # dbt macro files
    │   ├── models/
    │   │   └── example/
    │   │       ├── my_first_dbt_model.sql
    │   │       ├── my_second_dbt_model.sql
    │   │       └── schema.yml
    │   ├── seeds/                        # dbt seed files
    │   ├── snapshots/                    # dbt snapshot files
    │   └── tests/                        # dbt test files
    ├── my_marvel.db                      # SQLite database file
    ├── raw/                              # Directory for raw data
    ├── sql/
    │   ├── backup_001.db                 # Database backup
    │   └── sql.sql                       # General SQL scripts
    └── sqls/                             # Additional SQL scripts

## Key Components

* **ETL Pipeline (`ETLApp.py`):** Handles the extraction, transformation, and loading of data into `my_marvel.db` using `sqlite3`.
* **Data Modeling (`Models/Comic.py`):** Defines the structure of our comic data.
* **Data Access (`DataLayer/DataService.py`):** Manages interactions with the SQLite database.
* **Data Transformation (`marvel_dbt/`):** Uses dbt for data transformations.
* **Data Analysis (`Comic_Character_Analysis.ipynb`):** Analyzes and visualizes data using Jupyter Notebook, including character and comic plots and character counts (see `count.png`).
* **Configuration (`Utils/Config.py`):** Manages settings for the pipeline.
* **Services (`Services/ComicService.py`):** Provides the business logic for interacting with comic data.
* **Database (`my_marvel.db`):** Stores the comic data.
* **Logging:** Logs operations for both the data service and dbt.
* **Cron Job (`cronjob.sh`):** Automates the ETL process on a schedule.

## DBT Notes (In Progress)

The dbt models in `marvel_dbt/models/` are still being developed. We're aiming to:

* Check for null values in the data.
* Identify and handle empty records.
* Create a materialized view to join character and comic data.

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/dadenewyyt/MarvelDataPipeline.git](https://github.com/dadenewyyt/MarvelDataPipeline.git)
    cd MarvelDataPipeline
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt  # If you have one
    pip install pandas requests dbt-core dbt-sqlite  # Example dependencies
    ```
4.  **Database Setup:**
    * Make sure SQLite is installed.
    * Run `ETLApp.py` to create or update `my_marvel.db`.
5.  **dbt Setup:**
    * Navigate to `marvel_dbt/`.
    * Run `dbt deps`.
    * Configure `profiles.yml` for SQLite.
    * Run `dbt run`.
6.  **Cron Setup (Linux/macOS):**
    * Make `cronjob.sh` executable: `chmod +x cronjob.sh`
    * Open crontab: `crontab -e`
    * Add cron entry (e.g., daily at midnight): `0 0 * * * /path/to/MarvelDataPipeline/cronjob.sh` (adjust the path).

## Usage

1.  **Run ETL:**
    ```bash
    ./cronjob.sh  # Run the shell script to execute the ETL.
    ```
2.  **Run dbt:**
    ```bash
    cd marvel_dbt
    dbt run
    ```
3.  **Analyze Data:**
    * Open `Comic_Character_Analysis.ipynb`.
    * Run the notebook cells.
4.  **Use Services:**
    * Use `ComicService.py` for data interactions.

## Key Notes

* We're using `sqlite3` directly for database operations.
* dbt is used for data transformations (still in progress).
* Jupyter Notebook is used for data analysis and visualization.
* Logging is in place for service and dbt operations.

[![Data Pipeline Diagram](architecture/eclidrawpipeline0.png)](architecture/eclidrawpipeline0.png)
[![Data Flow Drawing](architecture/drawing.png)](architecture/drawing.png)

This document gives you an overview of the project. Check out the code and individual files for more details.
**Developed by: Daniel Wondyifraw**
