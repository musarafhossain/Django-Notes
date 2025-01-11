# Create Application

Follow these steps to create and install a Django application.

## Step 1: Create Application
Run the following command to create a new application:
```
python manage.py startapp applicationname
```
Replace `applicationname` with your desired name for the application.

## Step 2: Install Application
To install the application, follow these steps:

1. Go to `[projectname/projectname/settings.py]`
2. Add the application name in `INSTALLED_APPS`

### Example of settings.py
```
settings.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| INSTALLED_APPS = [                                                    |
|   'django.contrib.admin',                                             |
|   'django.contrib.auth',                                              |
|   'django.contrib.contenttypes',                                      |
|   'django.contrib.sessions',                                          |
|   'django.contrib.messages',                                          |
|   'django.contrib.staticfiles',                                       |
|   'applicationname',                                                  |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```