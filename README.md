# Marvel Data Pipeline

[![Project Architecture Image](architecture/image1.png)](architecture/image1.png)

This project implements a data pipeline for Marvel comic book data. It includes data extraction, transformation, loading (ETL), and analysis using various tools and technologies, specifically using the `sqlite3` API directly.

## Project Structure

* **`Comic_Character_Analysis.ipynb`**: Jupyter Notebook containing data analysis and visualization.
* **`architecture/`**: Contains architectural images.
* **`DataLayer/`**: Contains data access logic.
    * **`DataService.py`**: Manages SQLite database interactions using the `sqlite3` API.
* **`ETLApp.py`**: Python script for executing the ETL pipeline.
* **`LICENSE`**: Project license.
* **`Models/`**: Defines data models.
    * **`Comic.py`**: Data model for comic book information.
* **`SSLcheck.py`**: Script for SSL certificate checks.
* **`Services/`**: Contains business logic services.
    * **`ComicService.py`**: Service for interacting with comic data.
* **`Utils/`**: Utility modules.
    * **`Config.py`**: Handles configuration settings.
* **`character_comic.sql.sqbpro`**: SQLiteStudio project file.
* **`data_service.log`**: Log file for data service operations.
* **`logs/`**: Directory for log files.
    * **`dbt.log`**: Log file for dbt (data build tool).
* **`marvel_dbt/`**: dbt project for data transformations.
    * **`README.md`**: dbt project README.
    * **`dbt_project.yml`**: dbt project configuration.
    * **`models/`**: dbt models for data transformations.
        * **`example/`**: Example dbt models.
    * Other dbt related directories.
* **`my_marvel.db`**: SQLite database file.
* **`my_marvel.db-journal`**: SQLite journal file.
* **`raw/`**: Directory for storing raw data.
* **`sql/`**: Directory for SQL scripts.
    * **`backup_001.db`**: Database backup.
    * **`sql.sql`**: General SQL scripts.
* **`sqls/`**: Additional directory for SQL scripts.

## Key Components

* **ETL Pipeline (`ETLApp.py`)**:
    * Extracts data from a source (likely an API or file).
    * Transforms the data into a usable format.
    * Loads the transformed data into a SQLite database (`my_marvel.db`) using the `sqlite3` API.
* **Data Modeling (`Models/Comic.py`)**: Defines the structure of the comic book data.
* **Data Access (`DataLayer/DataService.py`)**: Provides an interface for interacting with the database using `sqlite3`.
* **Data Transformation (`marvel_dbt/`)**: Uses dbt to perform data transformations.
* **Data Analysis (`Comic_Character_Analysis.ipynb`)**: Performs analysis and visualization of the comic book data.
* **Configuration (`Utils/Config.py`)**: Manages configuration settings.
* **Services (`Services/ComicService.py`)**: Provides business logic for interacting with comic data.
* **Database (`my_marvel.db`)**: Stores the comic book data.
* **Logging**: Logs are generated for data service operations and dbt transformations.

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/dadenewyyt/MarvelDataPipeline.git](https://www.google.com/search?q=https://github.com/dadenewyyt/MarvelDataPipeline.git)
    cd MarvelDataPipeline
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate #On linux or mac
    venv\Scripts\activate #On windows
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt #If a requirements.txt file exists, if not install needed packages.
    pip install pandas requests dbt-core dbt-sqlite #Example of needed packages.
    ```
4.  **Database Setup:**
    * The project uses SQLite. Ensure SQLite is installed.
    * Run `ETLApp.py` to create or update the database.
5.  **dbt Setup:**
    * Navigate to the `marvel_dbt` directory.
    * Run `dbt deps` to install dbt dependencies.
    * Configure your `profiles.yml` file for your sqlite connection.
    * Run `dbt run` to execute dbt models.

## Usage

1.  **Run ETL:**
    ```bash
    python ETLApp.py
    ```
2.  **Run dbt Transformations:**
    ```bash
    cd marvel_dbt
    dbt run
    ```
3.  **Analyze Data:**
    * Open `Comic_Character_Analysis.ipynb` in Jupyter Notebook.
    * Run the notebook cells.
4.  **Interact with Services:**
    * Use `ComicService.py` for data interactions.

## Key Notes

* This project utilizes SQLite for data storage via the `sqlite3` API directly.
* dbt is used for data transformations.
* Jupyter notebooks are used for data analysis.
* Logging is implemented for data service and dbt operations.
* Architectural diagrams can be found in the `architecture` folder.

[![Data Flow Image](architecture/image3.png)](architecture/image3.png)

This report is based on the file structure and content of the repository. For a more in-depth understanding, explore the code and documentation within the repository.
