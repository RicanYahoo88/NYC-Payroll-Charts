NYC Data DB Python

#must have db from myself or a project member as it is over 100mb so i cant upload it

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
