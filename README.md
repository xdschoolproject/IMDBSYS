## Setting Up the Virtual Environment (Windows)
   **Note:** This step is needed after cloning the repository because the virtual environment contains all the necessary dependencies that the project requires.
   
### 1. Create a Virtual Environment
   Open **Command Prompt** or **PowerShell**, and navigate to your cloned project folder:
   ```bash
   cd path\to\your\cloned\repo\test
````

Then, create a new virtual environment in your project directory:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

Activate the environment by running the following command:

```bash
venv\Scripts\activate
```

After activation, you should see `(venv)` in the command prompt, indicating that the virtual environment is active.

### 3. Install Dependencies

Install all the required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
```

This will install all the necessary Python packages listed in `requirements.txt` to your virtual environment.

<br>

## Running the Django Web Application
   **Note:** This will only run code written in **django** and will not include **streamlit** code. You need to run both servers in order to run both applications together.
   
### 1. Activate the Virtual Environment
   Open **Command Prompt** or **PowerShell**, and navigate to your project directory. Then, activate the virtual environment:
   ```bash
   cd path\to\your\cloned\repo\test
   venv\Scripts\activate
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

By default, it will be accessible at `http://127.0.0.1:8000/`.
