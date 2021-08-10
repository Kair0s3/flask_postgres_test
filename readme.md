Step 1 - Set Up Virtual Environment (Optional)
  - python -m venv .
  - cd Scripts
  - activate
  - cd ..
    - To return back to base directory path

Step 2 - Install Necessary Packages
  - pip install -r requirements.txt

Step 3 - Run Program
  - python app.py

Step 4 - Create Database and table
  - Enter psql commandline first
  - create database test;
  - \c test
    - Syntax - \c <DB> <DBUSER - optional unless you want to use another user>
  - create table users(
    uid serial PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL
  );
