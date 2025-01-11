# Set URL Pattern

Follow these steps to set the URL pattern for your Django application.

## Step 1: Set URL Pattern
1. Go to `[projectname/projectname/urls.py]`

### Example of urls.py
```python
urls.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| from django.contrib import admin                                      |
| from django.urls import path                                          |
| from application1 import views as app1_views                          |
| from application2 import views as app2_views                          |
|                                                                       |
| urlpatterns = [                                                       |
|   path('admin/', admin.site.urls),                                    |
|   path('path1/', app1_views.function1),                               |
|   path('path2/', app2_views.function2),                               |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```