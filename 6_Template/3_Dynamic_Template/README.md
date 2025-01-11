# Passing Data from Views to Templates in Django

Follow these steps to pass data as a dictionary from your views to your templates.

## Step 1: Pass the Data as Dictionary from views.py
Go to `[projectname/applicationname/views.py]` and modify your view function as follows:

```python
views.py
----------------------------------------------------------------------------------------
| from django.shortcuts import render                                                  |
|                                                                                      |
| # Create your views here.                                                            |
| def function1(request):                                                              |
|     return render(request, 'applicationname/temp.html', {'name': 'Musaraf Hossain'}) |
----------------------------------------------------------------------------------------
```

### Explanation:
- The `render()` function takes three arguments: the request, the template name (`'applicationname/temp.html'`), and a context dictionary (in this case, `{'name': 'Musaraf Hossain'}`).
- The dictionary will make the variable `name` available in the template for rendering.

---

## Step 2: Add the Variable Inside Template File
Go to `[projectname/applicationname/templates/applicationname/temp.html]` and modify your template file as follows:

```html
temp.html
-----------------------------------------------------------------------------------
| <!DOCTYPE html>                                                                 |
| <html lang="en">                                                                |
| <head>                                                                          |
|     <meta charset="UTF-8">                                                      |
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">      |
|     <title>Say Hello</title>                                                    |
| </head>                                                                         |
| <body>                                                                          |
|     <h1>Hello {{ name }}... How are you?</h1>                                   |
| </body>                                                                         |              
| </html>                                                                         |
-----------------------------------------------------------------------------------
```

### Explanation:
- Inside the template (`temp.html`), you can access the passed variable `name` using the `{{ name }}` syntax.
- When the `function1` view is called, the variable `name` will be replaced by its value (`'Musaraf Hossain'`), and the rendered page will show: **'Hello Musaraf Hossain... How are you?'**

---

This approach allows you to pass dynamic data from your views to your templates, making it possible to display custom content based on user input, database records, or any other dynamic source.
```