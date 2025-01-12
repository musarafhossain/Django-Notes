## **Django Cookies**

Cookies are small pieces of data stored on the client's browser. Django provides utilities to create, read, modify, and delete cookies.

---

### **1. Creating Cookies**

Cookies are created using the `set_cookie()` method in the response object. 

#### **Parameters of `set_cookie()`**
| Parameter      | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| `key`          | The name of the cookie.                                                                         |
| `value`        | The value of the cookie.                                                                        |
| `expires`      | Expiration date in the format of a string or `datetime`.                                        |
| `max_age`      | Maximum age of the cookie in seconds.                                                          |
| `path`         | Path for which the cookie is valid (default: `/`).                                              |
| `domain`       | Domain for which the cookie is valid.                                                          |
| `secure`       | Indicates if the cookie should be sent over HTTPS only.                                         |
| `httponly`     | Prevents JavaScript access to the cookie (security measure).                                    |
| `samesite`     | Controls cross-site cookie behavior (`'Lax'`, `'Strict'`, or `'None'`).                         |

---

#### **Example: Setting Cookies**

```python
from django.http import HttpResponse
from datetime import datetime, timedelta

def set_cookie_example(request):
    response = HttpResponse("Cookie Set Successfully")
    # Set a cookie that expires in 1 day
    response.set_cookie(
        key='user_token',
        value='abcd1234',
        expires=datetime.utcnow() + timedelta(days=1),
        path='/',
        secure=True,
        httponly=True,
        samesite='Strict'
    )
    return response
```

---

### **2. Reading/Accessing Cookies**

Cookies can be accessed via the `request.COOKIES` dictionary.

#### **Example: Reading Cookies**

```python
from django.http import HttpResponse

def read_cookie_example(request):
    user_token = request.COOKIES.get('user_token', 'No Cookie Found')
    return HttpResponse(f"User Token: {user_token}")
```

---

### **3. Replace/Append Cookies**

Replacing or appending cookies is as simple as calling `set_cookie()` with the same key. It overwrites the existing cookie value.

#### **Example: Replacing a Cookie**

```python
from django.http import HttpResponse

def replace_cookie_example(request):
    response = HttpResponse("Cookie Replaced Successfully")
    # Replace the existing cookie
    response.set_cookie('user_token', 'new_token_value')
    return response
```

---

### **4. Deleting Cookies**

Cookies can be deleted using the `delete_cookie()` method.

#### **Example: Deleting Cookies**

```python
from django.http import HttpResponse

def delete_cookie_example(request):
    response = HttpResponse("Cookie Deleted Successfully")
    # Delete the cookie
    response.delete_cookie('user_token')
    return response
```

---

### **5. Creating Signed Cookies**

Signed cookies ensure the integrity of data using a secret key. Use `set_signed_cookie()` for signed cookies.

#### **Parameters of `set_signed_cookie()`**
- Same as `set_cookie()`, with an additional `salt` parameter for extra security.

#### **Example: Setting Signed Cookies**

```python
from django.http import HttpResponse

def set_signed_cookie_example(request):
    response = HttpResponse("Signed Cookie Set Successfully")
    response.set_signed_cookie(
        key='user_id',
        value='12345',
        salt='my_salt',
        max_age=3600,  # Expires in 1 hour
        httponly=True,
    )
    return response
```

---

### **6. Getting Signed Cookies**

Signed cookies can be accessed using `get_signed_cookie()`, which validates the cookie's signature.

#### **Example: Reading Signed Cookies**

```python
from django.http import HttpResponse

def get_signed_cookie_example(request):
    try:
        user_id = request.get_signed_cookie('user_id', salt='my_salt')
        return HttpResponse(f"Signed Cookie Value: {user_id}")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
```

---

### **7. Cookies Security Issues**

1. **Cross-Site Scripting (XSS):**
   - Always use the `httponly` attribute to prevent JavaScript access to cookies.

2. **Cross-Site Request Forgery (CSRF):**
   - Use the `csrf_token` provided by Django for form submissions.

3. **Cookie Theft:**
   - Use the `secure` attribute to ensure cookies are sent over HTTPS only.

4. **Cross-Site Cookie Behavior:**
   - Use the `samesite` attribute to restrict cookies to same-site requests (`Lax` or `Strict`).

---

### **8. Cookies Limitations**

1. **Size Limit:**
   - Most browsers restrict the size of cookies to around 4 KB.

2. **Count Limit:**
   - Browsers typically allow around 20–50 cookies per domain.

3. **Data Security:**
   - Cookies are not encrypted. Use signed cookies or session cookies for sensitive data.

4. **User Control:**
   - Users can delete or block cookies at any time.

---

### **Complete Code Example**

#### **Views**
```python
from django.http import HttpResponse
from datetime import datetime, timedelta

def set_cookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('user_token', 'abcd1234', httponly=True, samesite='Strict')
    return response

def read_cookie(request):
    user_token = request.COOKIES.get('user_token', 'No Cookie Found')
    return HttpResponse(f"User Token: {user_token}")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('user_token')
    return response

def set_signed_cookie(request):
    response = HttpResponse("Signed Cookie Set")
    response.set_signed_cookie('user_id', '12345', salt='secure_salt', httponly=True)
    return response

def read_signed_cookie(request):
    try:
        user_id = request.get_signed_cookie('user_id', salt='secure_salt')
        return HttpResponse(f"Signed Cookie: {user_id}")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
```

#### **URLs**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('read-cookie/', views.read_cookie, name='read_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
    path('set-signed-cookie/', views.set_signed_cookie, name='set_signed_cookie'),
    path('read-signed-cookie/', views.read_signed_cookie, name='read_signed_cookie'),
]
```

#### **Template Example**
```html
<h1>Cookie Example</h1>
<a href="{% url 'set_cookie' %}">Set Cookie</a><br>
<a href="{% url 'read_cookie' %}">Read Cookie</a><br>
<a href="{% url 'delete_cookie' %}">Delete Cookie</a><br>
<a href="{% url 'set_signed_cookie' %}">Set Signed Cookie</a><br>
<a href="{% url 'read_signed_cookie' %}">Read Signed Cookie</a><br>
```

---

This guide comprehensively covers **creating, reading, replacing, deleting cookies, signed cookies, their security considerations, and limitations**, complete with **views, URLs, and templates** for clarity.