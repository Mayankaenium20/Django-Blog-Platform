# Django-Blog-Platform

iCoder is a Django-based blogging platform that features user authentication, blog post creation, and dynamic content display. Users can read, search, and update blog posts. The project integrates Bootstrap for a responsive design and includes PATCH functionality for updating user details via a REST API.

## Features

- User authentication (signup, login, logout)
- Create, read, and update blog posts
- Search functionality
- Dynamic content display
- Responsive design with Bootstrap
- PATCH functionality for updating user details

## Requirements

- Python 3.x
- Django 3.x or higher
- Bootstrap 5.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/icoder.git
   cd icoder
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application.

## Directory Structure

```plaintext
icoder/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── blogHome.html
│   │       ├── blogPost.html
│   ├── urls.py
│   ├── views.py
├── home/
│   ├── templates/
│   │   └── home/
│   │       ├── user_update.html
│   │       ├── home.html
│   ├── urls.py
│   ├── views.py
├── icoder/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── templates/
│   └── base.html
└── manage.py
```

## Usage

### User Authentication

- **Sign Up**: Create a new account.
- **Log In**: Access your account.
- **Log Out**: Sign out from your account.

### Blog Posts

- **Create**: Add new blog posts.
- **Read**: View blog post content.
- **Update**: Modify existing blog posts.

### Updating User Details

To update user details, navigate to the user update page and modify the required fields. Changes will be saved using the PATCH method.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)

---
