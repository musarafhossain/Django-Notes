# Static Files (CSS, JS, Images etc.)

Follow these steps to add static files in your Django application.

## Step 1: Create static Folder
Create a folder named `static` inside your project directory.

## Step 2: Create file types directory
Inside the `templates` folder, create files directories (css, js, images).

## Step 3: Create Static Files (.css, .js, .jpg)
Inside the `files directories (css, js, images)` folder, create static files.

## Step 3: Add Static Directory Inside settings.py
Go to `[projectname/projectname/settings.py]` and add the static directory.

### Example of settings.py
```python
settings.py 

...                                                                   
STATIC_DIR = f'{BASE_DIR}/static'                                     
...                                                                   
                                                                      
...
STATIC_URL = 'static/'                                                                   
STATICFILES_DIRS = [ STATIC_DIR ]
...                                                                           
```

## Step 4: Write Static Files Inside Directory
Create a template file named `style.css` inside the `static/css` directory.

### Example of static/css/style.css
```css
style.css
h1{
    background-color: red;
}
```

### Example of static/js/script.js
```js
script.js
function sayHello(params) {
    alert(params);
}
```

## Step 5: Now load the static files in template and set the path
```html
home.html
<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>This is home page.</h1>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <button type="button" onclick="sayHello('Hello World!')">SayHello</button>
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```