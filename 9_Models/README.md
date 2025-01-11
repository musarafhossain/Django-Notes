# Django Models

Django models are Python classes that define the structure and behavior of your database tables. They provide a way to interact with the database using Python rather than raw SQL.

---

## Step 1: Define a Model
Create a model by defining a class that inherits from `django.db.models.Model`.

### Example: Defining a Model
```python
# projectname/applicationname/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Text field with max length
    description = models.TextField()         # Large text field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)      # Auto timestamp on update

    def __str__(self):
        return self.name
```

---

## Step 2: Field Options in Models

When defining model fields, you can use several options to customize their behavior. These options can be passed as arguments when defining a field in the model.

### Common Field Options

| Option              | Description                                                   | Example                                                    |
|---------------------|---------------------------------------------------------------|------------------------------------------------------------|
| `max_length`        | Specifies the maximum length of a field (usually for `CharField`). | `name = models.CharField(max_length=100)`                  |
| `null`              | If set to `True`, the database column will allow NULL values. | `description = models.TextField(null=True)`                |
| `blank`             | If set to `True`, the field can be left blank in forms.      | `price = models.DecimalField(blank=True)`                  |
| `default`           | Sets the default value for a field.                           | `price = models.DecimalField(default=0.0)`                 |
| `choices`           | Defines a set of valid choices for a field.                   | `category = models.CharField(choices=category_choices)`    |
| `unique`            | Ensures that all values in the field are unique.              | `email = models.EmailField(unique=True)`                   |
| `db_index`          | Adds an index for the field in the database.                  | `username = models.CharField(db_index=True)`               |
| `auto_now_add`      | Automatically sets the field to the current timestamp when a new record is created. | `created_at = models.DateTimeField(auto_now_add=True)`     |
| `auto_now`          | Automatically sets the field to the current timestamp whenever the record is updated. | `updated_at = models.DateTimeField(auto_now=True)`         |
| `verbose_name`      | Provides a human-readable name for the field (used in the admin panel). | `category = models.CharField(verbose_name="Product Category")` |
| `help_text`         | Provides a description for the field, shown in forms.        | `price = models.DecimalField(help_text="Price in USD")`    |

---

## Step 3: Activate the Model
### 1. **Add the App to `INSTALLED_APPS`:**
   In `settings.py`, include your app in the `INSTALLED_APPS` list.

   ```python
   INSTALLED_APPS = [
       ...,
       'myapp',
   ]
   ```

### 2. **Create Migrations:**
Run the following command to create the migration file for your model:

```bash
python manage.py makemigrations
```

### 3. **Apply the Migrations:**
Run the following command to apply the migrations and update the database:

```bash
python manage.py migrate
```

---

## Step 4: Use the Model
You can interact with the database using the model in Python.

### Example: Creating, Retrieving, Updating, and Deleting Records
```python
# Using the Product model
from myapp.models import Product

# Create a new product
product = Product(name="Laptop", description="A powerful laptop", price=999.99)
product.save()

# Retrieve products
products = Product.objects.all()  # Get all products
product = Product.objects.get(id=1)  # Get a specific product by ID

# Update a product
product.price = 899.99
product.save()

# Delete a product
product.delete()
```

---

## Step 5: Model Operations

### 1. **Create a New Record**
You can create a new instance of a model and save it to the database.

```python
product = Product(name="Phone", description="Smartphone", price=499.99)
product.save()
```

Alternatively, you can use the `.create()` method to both instantiate and save the object.

```python
product = Product.objects.create(name="Tablet", description="Touchscreen tablet", price=299.99)
```

### 2. **Retrieve Records**
There are several methods to retrieve records from the database.

- **Get all records:**
  ```python
  products = Product.objects.all()
  ```

- **Get a single record by primary key (ID):**
  ```python
  product = Product.objects.get(id=1)
  ```

- **Filter records by a condition:**
  ```python
  cheap_products = Product.objects.filter(price__lt=100)  # Products under $100
  ```

- **Get the first matching record:**
  ```python
  product = Product.objects.filter(price__gt=100).first()
  ```

- **Get a single record using `filter()` and `first()`:**
  ```python
  product = Product.objects.filter(name="Laptop").first()
  ```

### 3. **Update Records**
To update a record, retrieve it, modify its attributes, and save it.

```python
product = Product.objects.get(id=1)
product.price = 799.99
product.save()  # Save the changes to the database
```

You can also use `.update()` to update multiple records at once:

```python
Product.objects.filter(price__lt=100).update(price=50)
```

### 4. **Delete Records**
To delete a record, retrieve it and call `.delete()`.

```python
product = Product.objects.get(id=1)
product.delete()
```

To delete multiple records based on a condition, you can use `filter()`:

```python
Product.objects.filter(price__lt=50).delete()
```

### 5. **Count Records**
To count the number of records that match a certain condition:

```python
count = Product.objects.filter(price__gt=100).count()  # Count products over $100
```

### 6. **Order Records**
To order the records, use `.order_by()`:

```python
ordered_products = Product.objects.order_by('price')  # Ascending order
```

To order in descending order, use a hyphen (`-`):

```python
ordered_products = Product.objects.order_by('-price')  # Descending order
```

### 7. **Existence Check**
To check if a record exists that matches a condition, use `.exists()`:

```python
exists = Product.objects.filter(name="Laptop").exists()  # Returns True if the record exists
```

### 8. **Aggregate Operations**
Django supports aggregation, such as calculating the sum, average, etc., of fields.

- **Sum of a field:**
  ```python
  from django.db.models import Sum
  total_price = Product.objects.aggregate(Sum('price'))
  ```

- **Average of a field:**
  ```python
  from django.db.models import Avg
  average_price = Product.objects.aggregate(Avg('price'))
  ```

---

## Step 6: Field Types in Models

When defining a model, several field types are available to choose from based on the kind of data you want to store.

### Common Field Types

| Field Type           | Description                                                   | Example                                                  |
|----------------------|---------------------------------------------------------------|----------------------------------------------------------|
| `CharField`           | A string field with a fixed maximum length.                     | `name = models.CharField(max_length=100)`                 |
| `TextField`           | A large text field for storing longer text.                    | `description = models.TextField()`                        |
| `IntegerField`        | A field for storing whole numbers.                            | `age = models.IntegerField()`                             |
| `FloatField`          | A field for storing decimal or floating-point numbers.        | `price = models.FloatField()`                             |
| `DecimalField`        | A field for precise numerical data, with a specified number of decimal places. | `price = models.DecimalField(max_digits=10, decimal_places=2)` |
| `BooleanField`        | A true/false field.                                           | `is_active = models.BooleanField()`                       |
| `DateField`           | A field for date values.                                       | `created_at = models.DateField()`                         |
| `DateTimeField`       | A field for storing both date and time.                       | `updated_at = models.DateTimeField(auto_now=True)`        |
| `TimeField`           | A field for time values.                                       | `start_time = models.TimeField()`                         |
| `ImageField`          | A field for storing image files (usually used with media storage). | `image = models.ImageField(upload_to='uploads/')`      |
| `FileField`           | A field for storing file uploads.                             | `file = models.FileField(upload_to='files/')`              |
| `ForeignKey`          | A many-to-one relationship field (relating to another model). | `author = models.ForeignKey(User, on_delete=models.CASCADE)` |
| `OneToOneField`       | A one-to-one relationship field (relating to another model). | `profile = models.OneToOneField(User, on_delete=models.CASCADE)` |
| `ManyToManyField`     | A many-to-many relationship field (relating to another model). | `tags = models.ManyToManyField(Tag)`                       |

---

This guide now includes a comprehensive overview of Django models, field options, model operations, and field types.
```