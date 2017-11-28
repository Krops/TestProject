# TestProject

before launch

export MYSITE_CONFIG="/{path to project}/TestProject/config.json"
export DJANGO_SETTINGS_MODULE=TestProject.settings.dev
(dev uses lite, prod uses postgresql)

then

cd /{path to project}/TestProject/
pip install -r requirements.txt
python manage.py loaddata prod/fixtures/initial_data.json
python manage.py migrate
python manage.py runserver