# Installation

### Create a VENV,

    `python -m venv venv`

### Activate VENV (Git Base),

    `source venv/Scripts/activate`

### Install Needed Packages For Flask API From `requirements.txt` By PIP, 

    `pip install -r requirements.txt`


### If You Insatll Any Extra Packages From PIP, Run This Command For Add New Packages Name to `requirements.txt`,

    `pip freeze > requirements.txt`

---

# Database Connectivity

 - Create a New Database In XAMPP or WAMP.

 - Update The `.env` File.

---

# Flask Migration

 - Create Models and Refer Route File In `__init__.py`.

 - Run This Commands,

    ```
        flask db init
        flask db migrate -m "Migration Meassage"
        flask db upgrade
    ```

---