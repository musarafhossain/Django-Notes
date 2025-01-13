# **Django Sessions**

Sessions in Django allow you to store and retrieve arbitrary data on a per-site-visitor basis. The data is stored on the server side, while a session key is stored in the client-side cookies.

---

## **1. Setting Up Django Sessions**

Ensure the `django.contrib.sessions` middleware is enabled in your `MIDDLEWARE` and the `INSTALLED_APPS` includes `django.contrib.sessions`.

---

## **2. Session Methods**

### **Setting a Session Item**

```python
def set_session_item(request):
    request.session['username'] = 'JohnDoe'
    return HttpResponse("Session item set successfully.")
```

### **Getting a Session Item**

```python
def get_session_item(request):
    username = request.session.get('username', 'Guest')
    return HttpResponse(f"Hello, {username}!")
```

### **Deleting a Session Item**

```python
def delete_session_item(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponse("Session item deleted successfully.")
```

### **Checking if a Session Key Exists**

```python
def check_session_item(request):
    if 'username' in request.session:
        return HttpResponse("Username exists in session.")
    return HttpResponse("Username does not exist in session.")
```

---

## **3. Session Methods with Examples**

### **keys()**
Get all keys in the session.

```python
def session_keys(request):
    keys = request.session.keys()
    return HttpResponse(f"Session Keys: {list(keys)}")
```

### **items()**
Get all key-value pairs.

```python
def session_items(request):
    items = request.session.items()
    return HttpResponse(f"Session Items: {dict(items)}")
```

### **clear()**
Clear all session data.

```python
def clear_session(request):
    request.session.clear()
    return HttpResponse("Session cleared.")
```

### **setdefault()**
Set a default value if the key does not exist.

```python
def set_default_session(request):
    username = request.session.setdefault('username', 'DefaultUser')
    return HttpResponse(f"Username is: {username}")
```

### **flush()**
Clear all session data and regenerate the session key.

```python
def flush_session(request):
    request.session.flush()
    return HttpResponse("Session flushed.")
```

### **set_expiry(value)**
Set the session expiry:
- `value=0`: Expires when the browser is closed.
- `value=None`: Uses default expiry age.
- `value=timedelta`: Set expiry as a time delta.
- `value=seconds`: Set expiry in seconds.

```python
from datetime import timedelta

def set_session_expiry(request):
    request.session.set_expiry(timedelta(minutes=5))  # Expires in 5 minutes
    return HttpResponse("Session expiry set to 5 minutes.")
```

### **get_expiry_age()**
Get the expiry age in seconds.

```python
def get_expiry_age(request):
    age = request.session.get_expiry_age()
    return HttpResponse(f"Session expires in {age} seconds.")
```

### **get_expiry_date()**
Get the exact expiry date and time.

```python
def get_expiry_date(request):
    expiry_date = request.session.get_expiry_date()
    return HttpResponse(f"Session expiry date: {expiry_date}")
```

### **cycle_key()**
Generate a new session key while retaining existing data.

```python
def cycle_session_key(request):
    request.session.cycle_key()
    return HttpResponse("Session key cycled.")
```

### **set_test_cookie()**
Set a test cookie.

```python
def set_test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("Test cookie set.")
```

### **test_cookie_worked()**
Check if the test cookie was set correctly.

```python
def test_cookie_worked(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return HttpResponse("Test cookie worked.")
    return HttpResponse("Test cookie did not work.")
```

### **delete_test_cookie()**
Delete the test cookie.

```python
def delete_test_cookie(request):
    request.session.delete_test_cookie()
    return HttpResponse("Test cookie deleted.")
```

---

## **4. Session Settings**

### **Key Settings and Examples**

#### **SESSION_CACHE_ALIAS**
Specifies the cache alias to store session data.

```python
# settings.py
SESSION_CACHE_ALIAS = 'default'
```

#### **SESSION_COOKIE_AGE**
Specifies the session cookie's age in seconds (default is 1209600 seconds or 2 weeks).

```python
# settings.py
SESSION_COOKIE_AGE = 3600  # Expires in 1 hour
```

#### **SESSION_COOKIE_DOMAIN**
Defines the domain for which the session cookie is valid.

```python
# settings.py
SESSION_COOKIE_DOMAIN = '.example.com'  # Valid for all subdomains of example.com
```

#### **SESSION_COOKIE_HTTPONLY**
Prevents JavaScript access to session cookies.

```python
# settings.py
SESSION_COOKIE_HTTPONLY = True
```

#### **SESSION_COOKIE_NAME**
The name of the session cookie (default: `sessionid`).

```python
# settings.py
SESSION_COOKIE_NAME = 'custom_sessionid'
```

#### **SESSION_COOKIE_PATH**
The path for which the session cookie is valid.

```python
# settings.py
SESSION_COOKIE_PATH = '/'
```

#### **SESSION_COOKIE_SAMESITE**
Controls cross-site cookie behavior (`'Lax'`, `'Strict'`, `'None'`).

```python
# settings.py
SESSION_COOKIE_SAMESITE = 'Lax'
```

#### **SESSION_COOKIE_SECURE**
Ensures cookies are sent only over HTTPS.

```python
# settings.py
SESSION_COOKIE_SECURE = True
```

#### **SESSION_ENGINE**
Defines the backend to store session data.

```python
# settings.py
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default backend
```

#### **SESSION_EXPIRE_AT_BROWSER_CLOSE**
Expires session when the browser closes.

```python
# settings.py
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

#### **SESSION_FILE_PATH**
Directory to store file-based sessions.

```python
# settings.py
SESSION_FILE_PATH = '/tmp/django_sessions'
```

#### **SESSION_SAVE_EVERY_REQUEST**
Save session data on every request.

```python
# settings.py
SESSION_SAVE_EVERY_REQUEST = True
```

#### **SESSION_SERIALIZER**
Serializes session data (`JSONSerializer` or `PickleSerializer`).

```python
# settings.py
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
```

---

## **5. Complete Code Example**

#### **Views**

```python
from django.http import HttpResponse
from datetime import timedelta

def set_session_example(request):
    request.session['name'] = 'John Doe'
    request.session.set_expiry(300)  # Expires in 300 seconds
    return HttpResponse("Session data set!")

def get_session_example(request):
    name = request.session.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}!")

def delete_session_example(request):
    request.session.flush()  # Clears all session data
    return HttpResponse("Session data deleted.")
```

#### **URLs**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('set-session/', views.set_session_example, name='set_session'),
    path('get-session/', views.get_session_example, name='get_session'),
    path('delete-session/', views.delete_session_example, name='delete_session'),
]
```

#### **Template**

```html
<h1>Django Session Example</h1>
<a href="{% url 'set_session' %}">Set Session</a><br>
<a href="{% url 'get_session' %}">Get Session</a><br>
<a href="{% url 'delete_session' %}">Delete Session</a><br>
```

---

This guide provides comprehensive details on Django sessions, including examples for session methods and settings.