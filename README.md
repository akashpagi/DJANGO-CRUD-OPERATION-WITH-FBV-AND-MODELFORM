# Django CRUD Operation with Function-Based Views (FBV) and ModelForm

This project is a simple **CRUD (Create, Read, Update, Delete)** application built with **Django** using **Function-Based Views (FBV)** and **ModelForm**. The project demonstrates how to manage student records, including creating, viewing, updating, and deleting student information.

## Features
- **Add New Student**: Users can add new student details using a form.
- **View Student Information**: All student records are displayed in a table.
- **Edit Student**: Users can edit existing student records.
- **Delete Student**: Users can delete student records.

## Project Structure
```bash
Project structure for directory: CRUD_PROJECT

├── 📄 db.sqlite3
├── 📂 enroll
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 forms.py
│   ├── 📂 migrations
│   │   ├── 📄 0001_initial.py
│   │   ├── 📄 __init__.py
│   │   └── 📂 __pycache__
│   ├── 📄 models.py
│   ├── 📂 static
│   │   └── 📂 enroll
│   │       ├── 📂 css
│   │       │   ├── 📄 all.min.css
│   │       │   └── 📄 bootstrap.css
│   │       └── 📂 js
│   │           ├── 📄 all.min.js
│   │           ├── 📄 bootstrap.js
│   │           ├── 📄 jQuery.js
│   │           └── 📄 popper.js
│   ├── 📂 templates
│   │   └── 📂 enroll
│   │       ├── 📄 add_and_show.html
│   │       ├── 📄 base.html
│   │       └── 📄 update_student.html
│   ├── 📄 tests.py
│   ├── 📄 views.py
│   ├── 📄 __init__.py
│   └── 📂 __pycache__
├── 📄 manage.py
├── 📄 README.md
└── 📂 v59_CRUD_PROJECT
    ├── 📄 asgi.py
    ├── 📄 settings.py
    ├── 📄 urls.py
    ├── 📄 wsgi.py
    ├── 📄 __init__.py
    └── 📂 __pycache__

Total directories 📂: 12
Total files 📄: 39
File extensions count:
.sqlite3 : 1
.py : 15
.pyc : 12
.css : 2
.js : 4
.html : 3
.txt : 1
.md : 1
```

## Technologies Used
- **Django** - Web framework for the backend
- **Django ModelForm** - For handling forms
- **SQLite** - Default Django database for local development
- **Bootstrap** - For responsive front-end design

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/akashpagi/DJANGO-CRUD-OPERATION-WITH-FBV-AND-MODELFORM.git
cd DJANGO-CRUD-OPERATION-WITH-FBV-AND-MODELFORM
```

### 2. Create a Virtual Environment
Create and activate a virtual environment to manage project dependencies:
On Windows
```bash
python -m venv env
env\Scripts\activate
```
On macOS and Linux:
```bash
python -m venv env
source env/bin/activate
```

### 3. Install Dependencies
Install the required Python packages (if required):
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
Apply database migrations to set up the initial database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to view the application.

### Usage
- **Add New Student**
  - Use the provided form to add new student details.

- **Edit or Delete Student**
  - Click the Edit or Delete buttons next to each student's information to perform the respective actions.

### Contributing
Feel free to submit issues or pull requests if you'd like to improve this project. Contributions are welcome!









