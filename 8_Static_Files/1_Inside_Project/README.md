# Adding Static Files Inside the Project in Django

Follow these steps to add static files at the **project level** in Django.

---

## Step 1: Create `static` Folder Inside Your Project
- Navigate to your project directory (the one containing `settings.py`) and create a folder named `static`.

### Example Structure
```
myproject/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── myapp/
├── manage.py
└── settings.py
```

---

## Step 2: Add Static Directory Inside `settings.py`
Modify your `settings.py` file to configure static file settings.

```python
# settings.py

# URL to serve static files
STATIC_URL = 'static/'

# Directory for global static files
STATICFILES_DIRS = [BASE_DIR / 'static']

# Directory to collect static files for deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

## Step 3: Create Static Files (CSS, JS, Images)
Add your static files inside the appropriate directories under the `static` folder.

- CSS: `static/css/style.css`
- JS: `static/js/script.js`
- Images: `static/images/logo.png`

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

This setup ensures your static files are accessible globally across your project during development and production.
```