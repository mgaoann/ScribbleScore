# handwriting-thing

to run the flask: 
create a new virtual environment (optional)
python3 -m venv .venv (on mac / linux)
. .venv/bin/activate
or on windows
py -3 -m venv .venv
.venv\Scripts\activate
then install flask
pip install Flask
then in the handwriting-thing directory, run 
python -m flask --app board run --port 8000 --debug
