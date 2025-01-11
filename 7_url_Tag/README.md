# Adding Named URL Patterns and Using Them in Django Templates

This guide explains how to add named URL parameters in your Django application and use them in your templates.

## Step 1: Add a Name Parameter in the Path Function

In your `urls.py` file, either at `[projectname]/projectname/urls.py` or `[projectname]/applicationname/urls.py`, add a name parameter to your path functions.

### Example of urls.py
```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
```

---

## Step 2: Use the Named URL with the URL Tag Inside href in Templates

In your template file (for example, `home.html` located at `[projectname]/templates/` or `[projectname]/applicationname/templates/applicationname/`), use the `{% url %}` template tag to reference the named URLs.

### Example of home.html
```html
<body>
    <h1>This is About Us page.</h1>
    <div>
        <a href="{% url 'profile' %}">Profile</a>
        <a href="{% url 'contact' %}">Contact Us</a>
        <a href="{% url 'about' %}">About Us</a>
    </div>
</body>
```

### Explanation:
- The `{% url 'profile' %}`, `{% url 'contact' %}`, and `{% url 'about' %}` tags dynamically generate the URLs for the specified views based on their names. This approach makes it easier to manage links throughout your application, as you can change the URL patterns in one place without needing to update every link.

---