# Google Authoenticator demo
- Django 3.x
- Python 3.8

# How to run on Heroku
- assuming appname is `gauth-demo`
```
git clone git@github.com:shinsaka/googleauthenticator_demo.git
cd googleauthenticator_demo

heroku apps:create gauth-demo

heroku git:remote --app gauth-demo

git push heroku master

heroku run --app gauth-demo python manage.py migrate
```

## Show logs on Heroku
```
heroku logs --app gauth-demo -t
```

## Destroy app
```
heroku apps:destroy --app gauth-demo
```

# How to run on local(Ubuntu)

- require pipenv

```
sudo apt install libpq-dev
pipenv install
python manage.py migrate
heroku local
```

