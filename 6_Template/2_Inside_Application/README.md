# Creating and Using Application-Specific Templates in Django

Follow these steps to create and use templates specific to your Django application.

## Step 1: Create Templates Folder Inside Application Directory
Create a folder named `templates` inside your application directory:  
`[projectname/applicationname/templates]`

## Step 2: Create Template Files (.html)
Inside the `templates/applicationname` directory, create your HTML template files. For example:  
`[projectname/applicationname/templates/applicationname/temp1.html]`

## Step 3: Add Templates Directory Inside settings.py
Go to `[projectname/projectname/settings.py]` and ensure your TEMPLATES setting includes `APP_DIRS`.

### Example of settings.py
```python
settings.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| ...                                                                   |
| TEMPLATES = [                                                         |
|   {                                                                   |
|       ...,                                                            |
|       'DIRS': [],                                                     |
|       'APP_DIRS': True,                                               |
|       ...,                                                            |
|   },                                                                  |
| ]                                                                     |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```

## Step 4: Write Template Files Inside Templates Directory
Create a template file named `temp1.html` inside the `templates/applicationname` directory.

### Example of templates/applicationname/temp1.html
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
|     return render(request, 'applicationname/temp1.html')   |
--------------------------------------------------------------
```