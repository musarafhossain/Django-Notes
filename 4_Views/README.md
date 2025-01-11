# Create View

Follow these steps to create a view in your Django application.

## Step 1: Create View
1. Go to `[projectname/applicationname/views.py]`

### Example of views.py
```
views.py
-------------------------------------------------------------------------
| ...                                                                   |
|                                                                       |
| from django.shortcuts import render                                   |
| from django.http import HttpResponse                                  |
| # Create your views here.                                             |
| def function_name1(request):                                          |
|   html = "<h1>Hello World!</h1>"                                      |
|   variable = 5 + 2 * 7                                                |
|   text = "Hello World"                                                |
|   return HttpResponse(html + str(variable) + text)                    |
|                                                                       |
| ...                                                                   |
-------------------------------------------------------------------------
```

### Definition
A function-based view is a Python function that takes a web request and returns a web response.
```