# Set URL Pattern

Follow these steps to set the URL pattern for your Django application.

## Step 1: Set URL Pattern in Project
1. Go to `[projectname/projectname/urls.py]`

### Example of urls.py
```python
urls.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| from django.contrib import admin                                      |
| from django.urls import path, include                                 |
|                                                                       |
| urlpatterns = [                                                       |
|   path('admin/', admin.site.urls),                                    |
|   path('', include('application1.urls')),                             |
|   path('', include('application2.urls')),                             |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```

## Step 2: Create a New File (urls.py) Inside Application
Create a new file named `urls.py` inside your application directory.

## Step 3: Set URL Pattern in Application
1. Go to `[projectname/applicationname/urls.py]`

### Example of application urls.py
```python
urls.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| from . import views                                                   |
| from django.urls import path                                          |
|                                                                       |
| urlpatterns = [                                                       |
|   path('', views.function1, name='view1'),                            |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```