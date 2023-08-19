## Plonktam Insurance

- git clone `https://github.com/Iantechie/Plonktam.git`
- Create virtual environ (linux) `python3 -m venv venv`
- Activate virtual environment (linux) `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run migrations, make sure to configure environment variables accordingly e.g Database credentials `python manage.py migrate`
- Activate server `python manage.py runserver` for default port. `python manage.py runserver 0.0.0.0:{yourport}`
- Visit the url in your browser and access the webpages