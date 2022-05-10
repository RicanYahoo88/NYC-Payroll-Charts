NYC Data DB Python

create directory(VSC)

create environment
python -m venv C:/Users/Cloud/Python/NYCBlog

move to scripts/bin directory
cd C:/Users/Cloud/Python/NYCBlog/Scripts

active environment(space in between)
. activate

Install Flask, and imports*(if not already installed)

pip install flask
pip install flask_bootstrap
pip install sqlite3
pip install pandas


export FLASK_APP=app(app name you used)
export FLASK_ENV=development
flask run

**UPDATE 05/10/2022**
completed payroll charts and added functionality to them as well as limited large calls to the db.Currently working on displaying better looking tables and organizing a more uniform look