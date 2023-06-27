/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
pip install -r requirements.txt


python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
