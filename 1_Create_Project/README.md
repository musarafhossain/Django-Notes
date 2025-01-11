# Setting Up a Django Project

Follow these steps to set up a Django project using Python and a virtual environment.

## Step 1: Download and Install Python
- Visit the [official Python website](https://www.python.org/downloads/) to download the latest version of Python.
- Follow the installation instructions for your operating system.

## Step 2: Install Virtual Environment
Run the following command in your command prompt or terminal:
```
pip install virtualenvwrapper-win
```

## Step 3: Create Virtual Environment (VE)
Use the following command to create a new virtual environment:
```
mkvirtualenv envname
```
Replace `envname` with your desired name for the virtual environment.

## Step 4: Activate VE
To activate your virtual environment, use the command:
```
workon envname
```
Make sure to replace `envname` with the name you used in Step 3.

## Step 5: Install Django in Created VE
Once your virtual environment is activated, install Django by running:
```
pip install django
```

## Step 6: Create Django Project
Finally, create a new Django project with the following command:
```
django-admin startproject main
```
---