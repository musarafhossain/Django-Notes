# Template Inheritance in Django

Template inheritance in Django allows you to create a base "skeleton" template that contains all the common elements of your site, which can then be extended by child templates. This approach promotes code reuse and simplifies maintenance.

## Step 1: Create a Base Template (base.html)

1. Inside your project’s main templates directory, typically located at `[projectname]/templates/`, create a file named `base.html`. This will serve as the foundational template that other templates will extend.
2. The `base.html` template includes the common structure of your site, such as the DOCTYPE, `<html>`, `<head>`, and `<body>` tags, along with blocks that allow child templates to customize specific sections of the layout.

### File Structure
```
[projectname]
└── templates
    └── base.html
```

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
    <header>
        <h1>Welcome to My Site</h1>
    </header>
    <nav>
        <!-- Navigation links could go here -->
    </nav>
    <main>
        {% block content %} Default Content {% endblock content %}
    </main>
    <footer>
        <p>&copy; 2024 My Site</p>
    </footer>
</body>
</html>
```

### Blocks Explained
- **`{% block title %}`**: This block allows child templates to customize the title of the page.
- **`{% block content %}`**: This is the main content block where child templates can insert custom content.
- Additional sections like header, nav, and footer are part of the common layout, ensuring consistency across pages.

---

## Step 2: Create a Child Template (temp.html) that Extends base.html

1. Inside your project’s main templates directory (`[projectname]/templates/applicationname/`), create a new template file called `temp.html`.
2. In this file, use `{% extends 'base.html' %}` at the top to indicate that this template extends from `base.html`.
3. Override the blocks (like `{% block title %}` and `{% block content %}`) to provide custom content for this specific page.

### File Structure
```
[projectname]
└── templates
    ├── base.html
    └── applicationname
        └── temp.html
```

### temp.html Content
```html
{% extends 'base.html' %}

{% block title %}
    Say Hello
{% endblock %}

{% block content %}
    {{ block.super }}  <!-- Optional: Includes content from the parent block -->
    <h1>Hi... How are you?</h1>
{% endblock content %}
```

### Using `block.super`
- **`{{ block.super }}`**: This allows you to include the content from the parent block (i.e., the `base.html` content) along with any additional content you want to add in the child template.
- You can omit `{{ block.super }}` if you only want to display content unique to the child template.

---

## Summary

- **base.html**: Acts as a skeleton template containing reusable layout code (e.g., header, footer, navigation).
- **Child Templates (e.g., temp.html)**: Extend `base.html` and override specific blocks to customize the title, content, or other sections of the page.

### Benefits of Template Inheritance:
- **Consistent Layout**: Template inheritance ensures a consistent layout across your project.
- **Easy Maintenance**: Changes in `base.html` (e.g., modifying the header or footer) automatically apply to all templates that extend it.
- **Reusable Code**: Avoids redundancy by centralizing common layout code in `base.html`.

This approach makes managing large Django projects easier, allowing for consistent and reusable page layouts while still permitting flexibility in customizing each page.