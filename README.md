# to-do-django

A simple To-Do web application built with the Django framework.

## Features

- View all tasks in a clean list
- Add new tasks with a title and optional description
- Edit existing tasks
- Mark tasks as done / undo completion
- Delete tasks
- Django admin interface for task management

## Requirements

- Python 3.10+
- Django 6.0+

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hawen74/to-do-django.git
   cd to-do-django
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. Open your browser at **http://127.0.0.1:8000/**

## Running Tests

```bash
python manage.py test tasks
```

## Project Structure

```
to-do-django/
├── manage.py
├── requirements.txt
├── todoproject/          # Django project settings & root URLs
│   ├── settings.py
│   └── urls.py
└── tasks/                # To-Do app
    ├── models.py         # Task model
    ├── views.py          # CRUD views
    ├── forms.py          # TaskForm
    ├── urls.py           # App URL patterns
    ├── admin.py          # Admin registration
    ├── tests.py          # Unit & integration tests
    └── templates/tasks/  # HTML templates
        ├── base.html
        ├── task_list.html
        ├── task_form.html
        └── task_confirm_delete.html
```
