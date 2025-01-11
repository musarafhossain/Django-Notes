# Creating and Including HTML Components in Django

This guide explains how to create reusable HTML components and include them in your Django templates.

## Step 1: Create HTML Components Inside Templates Folder

Create a file named `component.html` inside the components directory of your templates folder:  
`[projectname]/templates/components/component.html`

### component.html Content
```html
<header>
    This is header part
</header>
```
---

## Step 2: Include the Component Where You Want

Now, include the component in your base template located at `[projectname]/templates/base.html`.

### base.html Content
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} Default Title {% endblock %}</title>
</head>
<body>
    {% include 'components/component.html' %}
    {% block content %} Default Content {% endblock content %}
</body>
</html>
```

### Explanation:
- The `{% include 'components/component.html' %}` tag allows you to insert the content of `component.html` directly into `base.html`. This promotes reusability and keeps your templates organized.

---

By following these steps, you can create modular components that can be reused across different templates in your Django project, enhancing maintainability and consistency.