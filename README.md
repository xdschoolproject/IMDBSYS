## Setting Up the Virtual Environment (Windows)

### 1. Download python 3.13.9
  Open your browser and download python 3.13.9. Enter this in the URL

   ```bash
  https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe 
````

### 2. Clone the master branch in github
  Open **terminal** in **vscode** and Enter the command:
   ```bash
  git clone -b master https://github.com/xdschoolproject/roboadvisor.git
````
  After cloning you should see roboadvisor folder.

  
### 3. Create a Virtual Environment
   **Note:** This step is needed after cloning the repository because the virtual environment contains all the necessary dependencies that the project requires.
   <br>In the **terminal** in **vscode**, navigate to your cloned roboadvisor folder:
   ```bash
   cd path\to\your\cloned\repo\test
````

Then, create a new virtual environment in your project directory:

```bash
py -3.13 -m venv venv
```
After entering the command a venv folder should be created inside the project folder, like this:

```
project_folder/
│
├── venv/                         # Virtual environment folder Should be Here
│
├── roboadvisor/         
│
├── db.sqlite3                  
│
└── requirements.txt            
│
└── home_page/                     
│
└── stock_analysis_back_end/  
│
└── stock_analysis_front_end/ 
│
└── docs/                   

```
This structure places the `venv` (virtual environment) in the root of the project folder, alongside your application folder (`roboadvisor`), the database file (`db.sqlite3`), and the `requirements.txt` file.

### 4. Activate the Virtual Environment

Activate the environment by running the following command:

```bash
venv\Scripts\Activate.ps1
```

After activation, you should see `(venv)` in the command prompt, indicating that the virtual environment is active.

### 5. Install Dependencies

Install all the required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python packages listed in `requirements.txt` to your virtual environment.

### 6. Verify the Installed Dependencies

To ensure that all dependencies were successfully installed, run the following command:

```bash
pip freeze
```

<br>

## Running the Django Web Application without Streamlit

### 1. Activate the Virtual Environment (If not yet)
   Open **terminal** in **vscode**, and navigate to your project folder:
   ```bash
   cd path\to\your\cloned\repo\
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
### 2. Apply Database Migrations 

Run the following command to apply database migrations:

```bash
python manage.py migrate
```
Note: You don't need to run migrate every time you start the server—just when there are changes to your models or new migrations.

### 3. Run the Django Development Server

Start the server with:

```bash
python manage.py runserver
```

By default, it will be accessible at `http://127.0.0.1:8000/`. Open your browser and enter `http://127.0.0.1:8000/` in the URL

**Note:** This will only run code written in **django** and will not include **streamlit** code. You need to run both servers in order to run both applications together.

<br>

## Running the Streamlit and Django Web Application Together
**Note:** We need to run both **django** and **streamlit** server in the terminal. You need to run both servers in order to run both web applications together.

### 1. Activate the Virtual Environment (If not yet)
   Open **terminal** in **vscode**, and navigate to your project folder:
   ```bash
   cd path\to\your\cloned\repo\test
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
### 2. Apply Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 3. First Run the Streamlit Server

Navigate to the stock_analysis_front_end folder:
```bash
cd path\to\your\cloned\repo\roboadvisor\stock_analysis_front_end\ 
```
Start the server with: 
```bash
streamlit run stock_analysis_app.py 
```
This will open the stock analysis page in your browser. You can close the browser after openning but don't exit the server in the terminal.

### 4. Open a new tab in the terminal in vscode and activate the Virtual Environment in the new tab
   Open a new tab in the **terminal** in **vscode**, and navigate to your project folder (in vscode terminal click the "+" button):
   ```bash
   cd path\to\your\cloned\repo\test
````
   Then activate the venv:
   ```bash
   venv\Scripts\Activate.ps1
````
After activation, you should have two terminal tabs in vscode with `(venv)` in the command prompt, indicating that both virtual environments are active.

### 5. Run the Django Development Server Second
Navigate to the main roboadvisor folder (make sure you are in the folder that has manage.py file):
```bash
cd path\to\your\cloned\repo\
```
Start the server with:
```bash
python manage.py runserver
```
By default, it will be accessible at `http://127.0.0.1:8000/`. Open the browser and enter `http://127.0.0.1:8000/` in the URL.
