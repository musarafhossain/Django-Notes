## **Django Authentication and Authorization**

Django's **authentication and authorization framework** provides robust tools for managing users, groups, permissions, and access control.

---

### **1. User Object**

The `User` model represents users and provides fields and methods for user management.

#### **User Fields**
| Field                | Description                                          |
|----------------------|------------------------------------------------------|
| `username`           | The unique identifier for the user.                 |
| `first_name`         | The user’s first name.                              |
| `last_name`          | The user’s last name.                               |
| `email`              | The user’s email address.                           |
| `password`           | Encrypted password.                                 |
| `groups`             | Related groups of the user.                         |
| `user_permissions`   | Specific permissions assigned to the user.          |
| `is_staff`           | Indicates if the user can access the admin site.    |
| `is_active`          | Indicates if the user account is active.            |
| `is_superuser`       | Indicates if the user has all permissions.          |
| `last_login`         | The last login date and time.                       |
| `date_joined`        | The date and time the user joined.                  |
| `is_authenticated`   | Always `True` for authenticated users.              |
| `is_anonymous`       | Always `True` for anonymous users.                  |

---

#### **User Methods**

| **Method**                             | **Description**                                                                                                                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `get_username()`                       | Returns the username.                                                                                                                                                             |
| `get_full_name()`                      | Returns the full name (`first_name` + `last_name`).                                                                                                                                |
| `get_short_name()`                     | Returns the `first_name`.                                                                                                                                                         |
| `set_password(raw_password)`           | Encrypts and sets the user’s password.                                                                                                                                            |
| `set_unusable_password()`              | Marks the user as having no usable password.                                                                                                                                      |
| `has_usable_password()`                | Returns `True` if the user has a usable password.                                                                                                                                 |
| `check_password(raw_password)`         | Checks if a raw password matches the user’s encrypted password.                                                                                                                   |
| `get_user_permissions(obj=None)`       | Returns a set of permissions granted directly to the user, optionally for a specific object.                                                                                      |
| `get_group_permissions(obj=None)`      | Returns a set of permissions granted to the user via groups, optionally for a specific object.                                                                                    |
| `get_all_permissions(obj=None)`        | Returns all permissions (user-specific and group-based) granted to the user, optionally for a specific object.                                                                    |
| `has_perm(perm, obj=None)`             | Checks if the user has a specific permission.                                                                                                                                     |
| `has_perms(perm_list, obj=None)`       | Checks if the user has all permissions in a list.                                                                                                                                 |
| `has_module_perms(package_name)`       | Checks if the user has permissions for a specific app/module.                                                                                                                     |
| `email_user(subject, message, ...)`    | Sends an email to the user.                                                                                                                                                       |

---

#### **Example: User Methods**

```python
from django.contrib.auth.models import User

def user_methods_example(request):
    user = User.objects.create_user(username='john', password='password123', email='john@example.com')

    # Set and check password
    user.set_password('new_password123')
    password_valid = user.check_password('new_password123')

    # Set unusable password
    user.set_unusable_password()
    has_password = user.has_usable_password()

    # Get permissions
    user_permissions = user.get_user_permissions()
    group_permissions = user.get_group_permissions()
    all_permissions = user.get_all_permissions()
    has_add_user_permission = user.has_perm('auth.add_user')

    # Email user
    user.email_user(
        subject='Welcome!',
        message='Thanks for signing up!',
        from_email='admin@example.com'
    )

    return HttpResponse(f"""
        Username: {user.username}<br>
        Email: {user.email}<br>
        Password Valid: {password_valid}<br>
        Has Usable Password: {has_password}<br>
        User Permissions: {user_permissions}<br>
        Group Permissions: {group_permissions}<br>
        All Permissions: {all_permissions}<br>
        Has 'add_user' Permission: {has_add_user_permission}
    """)
```

---

### **2. UserManager Methods**

| **Method**                                                                                         | **Description**                                                                                                           |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `create_user(username, email=None, password=None, **extra_fields)`                                 | Creates and saves a regular user.                                                                                         |
| `create_superuser(username, email=None, password=None, **extra_fields)`                            | Creates and saves a superuser (with `is_staff` and `is_superuser` set to `True`).                                         |
| `with_perm(perm, is_active=True, include_superusers=True, backend=None, obj=None)`                 | Returns all users with a specific permission.                                                                             |
| `make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789")` | Generates a random password.                                                                                              |
| `get_by_natural_key(username)`                                                                    | Retrieves a user by their natural key (usually `username`).                                                               |

---

### **3. Permissions**

Permissions allow fine-grained access control for users and groups.

#### **Group Management**
| **Method**                                   | **Description**                          |
|---------------------------------------------|------------------------------------------|
| `myuser.groups.set([group_list])`           | Sets the user’s groups.                  |
| `myuser.groups.add(group, ...)`             | Adds one or more groups to the user.     |
| `myuser.groups.remove(group, ...)`          | Removes one or more groups from the user.|
| `myuser.groups.clear()`                     | Removes all groups from the user.        |

#### **User Permissions**
| **Method**                                   | **Description**                          |
|---------------------------------------------|------------------------------------------|
| `myuser.user_permissions.set([permission_list])` | Sets the user’s specific permissions. |
| `myuser.user_permissions.add(permission, ...)`  | Adds specific permissions to the user. |
| `myuser.user_permissions.remove(permission, ...)` | Removes specific permissions.        |
| `myuser.user_permissions.clear()`           | Clears all user-specific permissions.   |

---

#### **Example: Permissions Management**

```python
from django.contrib.auth.models import User, Group, Permission

def permissions_example(request):
    # Create user
    user = User.objects.create_user(username='jane', password='password123')

    # Create group and add user
    group = Group.objects.create(name='Editors')
    user.groups.add(group)

    # Add permissions
    permission = Permission.objects.get(codename='add_user')
    user.user_permissions.add(permission)

    # Modify groups and permissions
    user.groups.set([group])  # Set specific groups
    user.groups.remove(group)  # Remove specific group
    user.groups.clear()  # Clear all groups
    user.user_permissions.clear()  # Clear all permissions

    return HttpResponse(f"User '{user.username}' updated successfully.")
```

---

### **4. Authentication**

| **Method**                 | **Description**                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| `authenticate()`           | Verifies the user’s credentials. Returns `User` if valid or `None` if invalid.                  |
| `login()`                  | Logs a user into the session.                                                                   |
| `logout()`                 | Logs a user out of the session.                                                                 |
| `update_session_auth_hash()` | Updates session authentication hash after password change.                                     |

#### **Example: Authentication**
```python
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def auth_example(request):
    user = authenticate(username='jane', password='password123')
    if user is not None:
        login(request, user)
        update_session_auth_hash(request, user)  # After password change
        return HttpResponse(f"Welcome, {user.username}!")
    else:
        return HttpResponse("Invalid credentials")
```

---

### **5. Template Examples**

#### **Display Permissions**
```html
<h1>User Details</h1>
<p>Username: {{ user.username }}</p>
<p>Groups: 
    {% for group in user.groups.all %}
        {{ group.name }}
    {% endfor %}
</p>
<p>Permissions: 
    {% for perm in user.get_all_permissions %}
        {{ perm }}
    {% endfor %}
</p>
```

#### **Conditional Permissions**
```html
{% if user.has_perm('auth.add_user') %}
    <p>You can add users.</p>
{% else %}
    <p>You do not have permission to add users.</p>
{% endif %}
```

---

This guide covers **user fields, methods, user manager methods, permissions management, and authentication workflows** with specific examples for **views** and **templates**.