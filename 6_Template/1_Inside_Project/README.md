# Creating and Using Templates in Django

Follow these steps to create and use templates in your Django application.

## Step 1: Create Templates Folder
Create a folder named `templates` inside your project directory.

## Step 2: Create Template Files (.html)
Inside the `templates` folder, create your HTML template files.

## Step 3: Add Templates Directory Inside settings.py
Go to `[projectname/projectname/settings.py]` and add the templates directory.

### Example of settings.py
```python
settings.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| ...                                                                   |
| TEMPLATES_DIR = BASE_DIR / 'templates'                                |
| ...                                                                   |
|                                                                       |
| ...                                                                   |
| TEMPLATES = [                                                         |
|   {                                                                   |
|       ...,                                                            |
|       'DIRS': [TEMPLATES_DIR],                                        |
|       ...,                                                            |
|   },                                                                  |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```

## Step 4: Write Template Files Inside Templates Directory
Create a template file named `temp1.html` inside the `templates` directory.

### Example of templates/temp1.html
```html
temp1.html
-----------------------------------------------------------------------------------
| <!DOCTYPE html>                                                                 |
| <html lang="en">                                                                |
| <head>                                                                          |
|     <meta charset="UTF-8">                                                      |
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">      |
|     <title>Say Hello</title>                                                    |
| </head>                                                                         |
| <body>                                                                          |
|     <h1>Hello... How are you?</h1>                                              |
| </body>                                                                         |              
| </html>                                                                         |
-----------------------------------------------------------------------------------
```

## Step 5: Rendering Template Files Inside views.py
Go to `[projectname/applicationname/views.py]` and render the template.

### Example of views.py
```python
views.py
--------------------------------------------------------------
| from django.shortcuts import render                        |
|                                                            |
| # Create your views here.                                  |
| def sayBye(request):                                       | 
|     return render(request, 'temp1.html')                   |
--------------------------------------------------------------
```