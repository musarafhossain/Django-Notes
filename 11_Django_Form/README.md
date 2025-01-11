### Django Forms: Comprehensive Guide with Full Code Examples

---

### 1. **Creating a Form**

You can create a Django form by subclassing `forms.Form` or `forms.ModelForm`. Below is an example using `forms.Form`.

#### **forms.py**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text="Enter your full name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
```

---

### 2. **Displaying a Form**

Forms can be displayed in templates by rendering them using `{% csrf_token %}` and `{{ form.as_p }}`, `{{ form.as_table }}`, or `{{ form.as_ul }}`.

#### **views.py**
```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'contact.html', {'form': form})
```

#### **contact.html**
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

---

### 3. **Form Rendering Options**

- `{{ form.as_p }}`: Renders the form fields wrapped in `<p>` tags.
- `{{ form.as_table }}`: Renders the form fields in table rows.
- `{{ form.as_ul }}`: Renders the form fields as an unordered list.

---

### 4. **ID Attribute and Label Tag**

You can customize the `id` attribute using `widget` and `attrs`. Labels can be customized using the `label` field argument.

#### **forms.py**
```python
class CustomForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={'id': 'custom-id', 'class': 'form-control'}),
    )
```

#### **Generated HTML:**
```html
<label for="custom-id">Full Name</label>
<input type="text" name="name" id="custom-id" class="form-control">
```

---

### 5. **Initial Values**

Set initial field values using the `initial` argument.

#### **forms.py**
```python
class InitialForm(forms.Form):
    name = forms.CharField(initial="John Doe")
```

---

### 6. **Ordering Form Fields in the View**

You can reorder fields dynamically in the view by modifying the form's `fields` attribute.

#### **views.py**
```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    # Reorder fields dynamically
    form.order_fields(['email', 'name', 'message'])
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request, 'contact.html', {'form': form})
```

---

### 7. **Rendering Form Fields Manually Using a `for` Loop**

Instead of rendering fields individually, use a loop in the template to iterate over form fields. This is useful for dynamic forms.

#### **contact.html**
```html
<form method="post">
    {% csrf_token %}
    {% for field in form %}
        <div>
            <label for="{{ field.id_for_label }}">{{ field.label }}</label>
            {{ field }}
            {% if field.help_text %}
                <small>{{ field.help_text }}</small>
            {% endif %}
            {% for error in field.errors %}
                <div class="error">{{ error }}</div>
            {% endfor %}
        </div>
    {% endfor %}
    <button type="submit">Submit</button>
</form>
```

---

### 8. **Built-in Form Fields**

Some common fields include:
- `CharField`
- `EmailField`
- `ChoiceField`
- `IntegerField`
- `BooleanField`
- `DateField`

#### **forms.py**
```python
class BuiltInFieldsForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    agree = forms.BooleanField()
```

---

### 9. **Field Arguments**

Customize fields using arguments like `required`, `label`, `initial`, `help_text`, etc.

#### **forms.py**
```python
class FieldArgumentsForm(forms.Form):
    name = forms.CharField(label="Your Name", required=True, help_text="Full name required")
    email = forms.EmailField(disabled=True, initial="example@example.com")
```

---

### 10. **Widgets**

Django provides built-in widgets like `TextInput`, `Textarea`, `CheckboxInput`. You can also customize widgets using the `attrs` argument.

#### **forms.py**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 5}),
    )
```

---

### 11. **CSRF Protection**

Always include `{% csrf_token %}` in forms to protect against Cross-Site Request Forgery attacks.

---

### 12. **Form Validation**

Django validates forms automatically but also allows custom validation.

#### **forms.py**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    # Field-specific validation
    def clean_name(self):
        data = self.cleaned_data['name']
        if not data.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters.")
        return data

    # Full-form validation
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")

        if email and not email.endswith("@example.com"):
            raise forms.ValidationError("Email must be from the domain '@example.com'.")
        if message and len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
```

---

## 13. **Retrieve All Form Field Data**

You can retrieve all the form field data using the `cleaned_data` attribute after form validation.

#### **views.py**
```python
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get all cleaned data
            form_data = form.cleaned_data
            print("Name:", form_data.get('name'))
            print("Email:", form_data.get('email'))
            print("Message:", form_data.get('message'))
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

---
### 14. **Field Errors**

Field errors in Django forms provide feedback when validation fails. Django distinguishes between **field-specific errors** and **non-field errors**.

---

#### **1. Field-Specific Errors**
Field-specific errors occur when a particular field fails its validation.

- **Accessing field-specific errors**:
  ```html
  {{ field.errors }}
  ```
  Each field in the form can have its own error message displayed next to it.

#### **2. Non-Field Errors**
Non-field errors occur when validation on the entire form fails (e.g., custom `clean` method logic).

- **Accessing non-field errors**:
  ```html
  {{ form.non_field_errors }}
  ```

---

### Styling Errors

To style errors, you can iterate through errors and wrap them in custom HTML.

- **Template example**:
  ```html
  {% for field in form %}
      {% for error in field.errors %}
          <div class="error">{{ error }}</div>
      {% endfor %}
  {% endfor %}

  {% for error in form.non_field_errors %}
      <div class="non-field-error">{{ error }}</div>
  {% endfor %}
  ```

---

### Complete Example

#### **forms.py**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
    )

    # Field-specific validation
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters.")
        return name

    # Form-wide validation
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email and not email.endswith('@example.com'):
            self.add_error('email', "Email must end with @example.com")
        if len(cleaned_data.get('message', '')) < 10:
            self.add_error('message', "Message must be at least 10 characters long.")
```

---

#### **views.py**
```python
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle valid form data
            print(form.cleaned_data)
        else:
            print(form.errors)  # Print all errors in terminal
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

---

#### **contact.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        .error {
            color: red;
            font-size: 0.9em;
        }
        .non-field-error {
            color: orange;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {% for field in form %}
            <div class="form-group">
                <label for="{{ field.id_for_label }}">{{ field.label }}</label>
                {{ field }}
                {% if field.help_text %}
                    <small>{{ field.help_text }}</small>
                {% endif %}
                {% for error in field.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            </div>
        {% endfor %}
        
        {% for error in form.non_field_errors %}
            <div class="non-field-error">{{ error }}</div>
        {% endfor %}
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

---

### Output Details:

1. **Field-Specific Errors**:
   - If the **name** field contains non-alphabetic characters, an error appears below the field: 
     > Name must contain only alphabetic characters.
   - If the **email** field doesn't end with `@example.com`, an error appears below it:
     > Email must end with @example.com.
   - If the **message** field is less than 10 characters long:
     > Message must be at least 10 characters long.

2. **Non-Field Errors**:
   - Custom errors added in the `clean` method that don’t belong to a single field (none in this example).

3. **Styling Errors**:
   - Errors are styled in red for field errors and orange for non-field errors.

---

### Terminal Output:

If the form fails validation, errors will also be printed in the terminal as follows:
```plaintext
{'name': ['Name must contain only alphabetic characters.'],
 'email': ['Email must end with @example.com'],
 'message': ['Message must be at least 10 characters long.']}
```

This complete example ensures:
- Proper error handling and display.
- Styling for better user experience.
- Debugging by printing errors in the terminal.