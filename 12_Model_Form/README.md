### **Django Model Forms**

Model Forms provide an easy way to create forms based on Django models. They automatically generate form fields that correspond to model fields.

---

### 1. **Creating a ModelForm**

#### **Example: Basic Model**
```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
```

#### **Example: ModelForm**
```python
# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Link the form to the Book model
        fields = '__all__'  # Include all fields
```

---

### 2. **Specifying Fields**

You can specify which fields to include or exclude in the form:

#### **Include Specific Fields**
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
```

#### **Exclude Specific Fields**
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['isbn']
```

---

### 3. **Adding Labels, Help Text, and Error Messages**

#### **Customize Field Properties**
```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
        }
        help_texts = {
            'isbn': 'Enter the 13-character ISBN.',
        }
        error_messages = {
            'isbn': {
                'unique': 'This ISBN already exists.',
                'required': 'ISBN is required.',
            },
        }
```

---

### 4. **Customizing Widgets**

You can customize how fields are rendered using widgets.

```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
```

---

### 5. **The `save()` Method**

The `save()` method is used to save the form data to the database.

```python
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def save(self, commit=True):
        book = super().save(commit=False)  # Save instance but don’t commit to the database
        # Add custom logic here (e.g., modifying a field)
        book.title = book.title.title()  # Capitalize title
        if commit:
            book.save()  # Save to the database
        return book
```

---

### 6. **ModelForm Inheritance**

You can extend an existing `ModelForm` class to add or override functionality.

```python
class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class ExtendedBookForm(BaseBookForm):
    class Meta(BaseBookForm.Meta):  # Inherit Meta properties
        fields = BaseBookForm.Meta.fields + ['published_date']
```

---
### **Django Model Forms with `exclude`**

The `exclude` attribute in a ModelForm’s `Meta` class is used to specify fields that should not be included in the form.

---

### 7. **Example with `exclude`**

```python
# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['isbn']  # Exclude the ISBN field from the form
        labels = {
            'title': 'Book Title',
        }
        help_texts = {
            'description': 'Provide a brief description of the book.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
```

#### **Key Notes**:
1. **Fields Excluded**: In the above example, the `isbn` field will not be displayed in the form.
2. **Why Use `exclude`**: 
   - When a field is sensitive or managed elsewhere (e.g., auto-generated fields like timestamps).
   - To keep the form concise and relevant to the user.

---

### Complete Example: ModelForm

#### **models.py**
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
```

#### **forms.py**
```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
        }
        help_texts = {
            'isbn': 'Enter the 13-character ISBN.',
        }
        error_messages = {
            'isbn': {
                'unique': 'This ISBN already exists.',
                'required': 'ISBN is required.',
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
```

#### **views.py**
```python
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return redirect('success')  # Redirect on success
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
```

#### **add_book.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Book</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Add a New Book</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
```

#### **Output**:
- Fields are styled using Bootstrap classes.
- Field-specific labels, help text, and error messages are displayed.
- Data is saved to the database using the `save()` method.

---

### Key Features Covered:
1. Creating a `ModelForm`.
2. Selecting fields (`__all__`, `exclude`).
3. Customizing labels, help text, and error messages.
4. Using widgets for better UI.
5. Overriding the `save()` method for custom logic.
6. Extending forms via inheritance.