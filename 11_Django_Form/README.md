## Django Forms: A Complete Guide

### 1. **Create a Form**
You can create a Django form by subclassing `forms.Form` or `forms.ModelForm` in your app's `forms.py`.

#### Example:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
```

---

### 2. **Display Form**
You can display forms in templates using `{% csrf_token %}` for security and `{{ form.as_p }}`, `{{ form.as_table }}`, or `{{ form.as_ul }}` for rendering.

#### Example:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

---

### 3. **Form Rendering Options**
- `{{ form.as_p }}`: Renders the form fields inside `<p>` tags.
- `{{ form.as_table }}`: Renders the form fields inside a table.
- `{{ form.as_ul }}`: Renders the form fields as a list.

---

### 4. **ID Attribute**
- Each form field is rendered with an `id` attribute for easier styling and accessibility.

#### Example:
```html
<input type="text" name="name" id="id_name">
```

---

### 5. **Label Tag**
Labels can be added automatically or customized via the `label` argument in the field.

#### Example:
```html
<label for="id_name">Your Name</label>
```

---

### 6. **Initial Values**
Set initial values for form fields using the `initial` argument.

#### Example:
```python
class ExampleForm(forms.Form):
    name = forms.CharField(initial="Default Name")
```

---

### 7. **Order Form Fields**
Specify the order of fields by overriding the `Meta` class in a `ModelForm` or reordering manually in a `Form`.

#### Example:
```python
class ExampleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        fields = ['email', 'name']
```

---

### 8. **Rendering Form Fields Manually**
You can access individual field components and render them manually.

#### Example:
```html
<form method="post">
    {% csrf_token %}
    {{ form.name.label_tag }}
    {{ form.name }}
    {{ form.name.help_text }}
</form>
```

---

### 9. **Form Built-in Fields**
Common fields include:
- `CharField`
- `EmailField`
- `IntegerField`
- `BooleanField`
- `DateField`
- `ChoiceField`
- `FileField`

---

### 10. **Field Arguments**
You can customize fields using arguments like `required`, `label`, `initial`, etc.

#### Example:
```python
class ExampleForm(forms.Form):
    name = forms.CharField(required=True, help_text="Enter your full name.")
```

---

### 11. **Widgets**
Customize field rendering with widgets.

#### Example:
```python
class ExampleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-class'}))
```

---

### 12. **Built-in Widgets**
Django provides built-in widgets like:
- `TextInput`
- `Textarea`
- `Select`
- `RadioSelect`
- `CheckboxInput`

---

### 13. **CSRF Protection**
Always use `{% csrf_token %}` in forms to protect against Cross-Site Request Forgery.

---

### 14. **Form Validation**
#### Specific Field Validation:
Override `clean_<fieldname>()`.

#### Example:
```python
def clean_name(self):
    data = self.cleaned_data['name']
    if "invalid" in data:
        raise forms.ValidationError("Invalid name!")
    return data
```

#### All Fields at Once:
Override `clean()`.

---

### 15. **Field Errors**
- `{{ field.errors }}`: Displays field-specific errors.
- `{{ form.non_field_errors }}`: Displays non-field-specific errors.

#### Styling Errors:
Use CSS classes or tags to style errors.

---

### 16. **Form Cleaning and Validation**
#### Built-in Validators:
Django provides validators like `EmailValidator`, `RegexValidator`.

#### Custom Validator:
```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s is not an even number', params={'value': value})
```

---

### 17. **Get Data in Terminal**
Retrieve submitted form data in your views:

```python
def form_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
```

This comprehensive guide covers all essential aspects of Django forms!