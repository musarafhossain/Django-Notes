### **Django Messages Framework**

Django's messages framework is a built-in system for sending and displaying temporary messages to users. Messages can be used to provide feedback like success notifications, warnings, or error alerts.

---

### **1. Message Levels**

The messages framework provides five default message levels, each with an associated constant:

| **Level**      | **Constant**          | **Description**                         |
|-----------------|-----------------------|-----------------------------------------|
| DEBUG          | `messages.DEBUG`      | Development-level debug information.    |
| INFO           | `messages.INFO`       | General information for the user.       |
| SUCCESS        | `messages.SUCCESS`    | Indicates a successful action.          |
| WARNING        | `messages.WARNING`    | Alerts the user about a potential issue.|
| ERROR          | `messages.ERROR`      | Reports a serious problem.              |

---

### **2. Message Tags**

Message tags are CSS classes associated with the message levels. By default, the tags are:

| **Level**      | **Default Tag**       |
|-----------------|-----------------------|
| DEBUG          | `debug`               |
| INFO           | `info`                |
| SUCCESS        | `success`             |
| WARNING        | `warning`             |
| ERROR          | `error`               |

You can customize the tags in `settings.py`:
```python
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug-custom',
    message_constants.INFO: 'info-custom',
    message_constants.SUCCESS: 'success-custom',
    message_constants.WARNING: 'warning-custom',
    message_constants.ERROR: 'error-custom',
}
```

---

### **3. Adding Messages**

#### Using `messages.add_message()`
The most generic way to add a message:
```python
messages.add_message(request, messages.INFO, 'This is an info message.')
```

#### Shortcut Methods
Shortcut methods make it easier to add messages:
```python
messages.debug(request, 'This is a debug message.')
messages.info(request, 'This is an info message.')
messages.success(request, 'This is a success message.')
messages.warning(request, 'This is a warning message.')
messages.error(request, 'This is an error message.')
```

---

### **4. Displaying Messages**

To display messages in templates, use the `messages` context processor and loop through the messages in your template:

```html
<!-- base.html -->
{% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li class="{{ message.tags }}">{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
```

---

### **5. Methods**

### **`set_level()`**

The `set_level()` function sets the minimum message level that will be recorded in the storage. Messages below the set level will be ignored and not stored.

#### **Syntax**
```python
messages.set_level(request, level)
```

- **`request`**: The current HTTP request object.
- **`level`**: The minimum message level to be stored (e.g., `messages.DEBUG`, `messages.INFO`, etc.).

#### **Example**
```python
from django.contrib import messages

def set_level_example(request):
    # Set the level to WARNING
    messages.set_level(request, messages.WARNING)

    # Add messages of various levels
    messages.debug(request, "This is a DEBUG message.")    # Ignored
    messages.info(request, "This is an INFO message.")    # Ignored
    messages.success(request, "This is a SUCCESS message.")  # Ignored
    messages.warning(request, "This is a WARNING message.")  # Stored
    messages.error(request, "This is an ERROR message.")     # Stored

    return render(request, 'set_level_example.html')
```

In this example:
- Only the **WARNING** and **ERROR** messages are stored and displayed.
- **DEBUG**, **INFO**, and **SUCCESS** messages are ignored because their levels are below `messages.WARNING`.

---

### **`get_level()`**

The `get_level()` function retrieves the current message level for the request. This is useful to check which messages are being stored based on the current level.

#### **Syntax**
```python
current_level = messages.get_level(request)
```

- **`request`**: The current HTTP request object.
- **Returns**: The current message level as an integer (e.g., `10` for `DEBUG`, `20` for `INFO`, etc.).

#### **Example**
```python
from django.contrib import messages

def get_level_example(request):
    # Get the current message level
    current_level = messages.get_level(request)

    # Print or use the current level
    print(f"Current message level: {current_level}")

    # Add a message to display the level
    messages.info(request, f"The current message level is {current_level}.")
    return render(request, 'get_level_example.html')
```

---

### **Message Level Constants and Their Values**

| **Level Name** | **Constant**      | **Value** |
|-----------------|-------------------|-----------|
| DEBUG           | `messages.DEBUG` | `10`      |
| INFO            | `messages.INFO`  | `20`      |
| SUCCESS         | `messages.SUCCESS` | `25`   |
| WARNING         | `messages.WARNING` | `30`   |
| ERROR           | `messages.ERROR` | `40`      |

---

### **Practical Example: Combining `set_level()` and `get_level()`**

#### **views.py**
```python
from django.shortcuts import render
from django.contrib import messages

def set_and_get_level_example(request):
    # Set the message level to WARNING
    messages.set_level(request, messages.WARNING)

    # Get the current level
    current_level = messages.get_level(request)

    # Add messages of different levels
    messages.debug(request, "This is a DEBUG message.")    # Ignored
    messages.info(request, "This is an INFO message.")    # Ignored
    messages.success(request, "This is a SUCCESS message.")  # Ignored
    messages.warning(request, "This is a WARNING message.")  # Stored
    messages.error(request, "This is an ERROR message.")     # Stored

    # Display the current level in a message
    messages.info(request, f"Current message level is {current_level}.")  # Ignored

    return render(request, 'set_and_get_level.html')
```

#### **set_and_get_level.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set and Get Message Level</title>
</head>
<body>
    <h1>Messages:</h1>
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li class="{{ message.tags }}">{{ message }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No messages to display.</p>
    {% endif %}
</body>
</html>
```
---

### **6. Retrieving Messages**

Use `get_messages()` to retrieve and iterate over messages programmatically:
```python
from django.contrib.messages import get_messages

for message in get_messages(request):
    print(message)
```

---

### Full Example: Using Messages Framework

#### **views.py**
```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants as message_constants

def add_message_view(request):
    # Adding messages
    messages.debug(request, 'Debug message.')
    messages.info(request, 'Information message.')
    messages.success(request, 'Success message.')
    messages.warning(request, 'Warning message.')
    messages.error(request, 'Error message.')

    # Setting a custom level
    messages.set_level(request, messages.WARNING)
    
    # Custom tags
    MESSAGE_TAGS = {
        message_constants.DEBUG: 'debug-custom',
        message_constants.INFO: 'info-custom',
    }

    return render(request, 'messages_example.html')

def show_messages_view(request):
    return render(request, 'messages_example.html')
```

#### **urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('add_messages/', views.add_message_view, name='add_messages'),
    path('show_messages/', views.show_messages_view, name='show_messages'),
]
```

#### **messages_example.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Messages Example</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Django Messages Example</h1>
        <a href="{% url 'add_messages' %}" class="btn btn-primary">Add Messages</a>

        <hr>

        <h2>Messages:</h2>
        {% if messages %}
            <ul class="list-group">
                {% for message in messages %}
                    <li class="list-group-item {{ message.tags }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No messages to display.</p>
        {% endif %}
    </div>
</body>
</html>
```

---

### **Key Features Covered**:
1. **Message Levels**: DEBUG, INFO, SUCCESS, WARNING, ERROR.
2. **Adding Messages**: Using `add_message()` and shortcut methods.
3. **Displaying Messages**: Using the `messages` context processor in templates.
4. **Message Tags**: Default and custom.
5. **Methods**: `get_level()`, `set_level()`, `get_messages()`.