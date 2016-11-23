A url shortener scheme using python, Django and SQLITE3

Install python 3.4 or above in the system - ( https://www.python.org/downloads/)
Install Django 1.9.5 in the system using pip –(https://docs.djangoproject.com/en/1.9/topics/install/)
Note: Install virtual environment before installing Django (optional)

Install sqlite3 – (https://www.sqlite.org/download.html)
Add the above appliations to PATH variable
Place the zipped folder in your machine and extract the content
Navigate to folder, “shorturl “ in command prompt and type
Python manage.py makemigrations
Python manage.py migrate
This will create and initialize the database shorturl_db
Type Python load_db.py to load data into shorturl_db from file words (14).txt located in the same folder
Verify the data by connecting to data base using sqlite3 shorturl_db
Type Python manage.py runserver to start the development server
Copy the http address from command prompt and test using any standard browser
Note: The database is inside the zipped folder. But I have placed it outside as well

       Note : The above instructions are for a windows machine
