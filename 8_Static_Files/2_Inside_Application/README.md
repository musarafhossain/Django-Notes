# Adding Static Files Inside Application in Django

Follow these steps to add static files in your Django application.

## Step 1: Create `static` Folder Inside Your Application
Navigate to your Django application folder (e.g., `home`) and create a folder named `static`.

### Example Structure
```
home/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
└── views.py
```

---

## Step 2: Add Static Directory Inside `settings.py`
Modify your `settings.py` file to configure static files. 

```python
# settings.py

# Path for global static files (optional)
STATICFILES_DIRS = [BASE_DIR / 'static']

# URL to serve static files
STATIC_URL = 'static/'

# Directory to collect all static files during deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

> **Note:** Django automatically looks for static files in `static` folders inside each app, so you don’t need to add app-level static directories to `STATICFILES_DIRS`.

---

## Step 3: Create Static Files (CSS, JS, Images)
Add your static files inside the appropriate directories under the `static` folder in your app.

- CSS: `home/static/css/style.css`
- JS: `home/static/js/script.js`
- Images: `home/static/images/logo.png`

---

## Step 4: Use Static Files in Templates
1. Load the `static` template tag at the beginning of your template.
2. Reference the static files using the `{% static %}` tag.

### Example `home.html` Template
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>This is the home page.</h1>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <button onclick="sayHello('Hello World!')">Say Hello</button>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

---

## Step 5: Verify Static Files
Run the development server and check the browser console to ensure the static files are loaded correctly.

### Example URLs
- CSS: `http://127.0.0.1:8000/static/css/style.css`
- JS: `http://127.0.0.1:8000/static/js/script.js`
- Image: `http://127.0.0.1:8000/static/images/logo.png`

---

## Step 6: Collect Static Files (Deployment)
Run the following command to collect all static files into the `STATIC_ROOT` directory for production:

```bash
python manage.py collectstatic
```

### Example Structure After Collection
```
staticfiles/
├── css/
│   └── style.css
├── js/
│   └── script.js
└── images/
    └── logo.png
```

---

This setup ensures that your static files are correctly organized and accessible both during development and in production.
```