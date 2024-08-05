# Kanban Backend

A powerful backend for the Kanban project management tool, built with Django.

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Kanban Backend is a robust and flexible backend for a Kanban project management tool. It provides an API for managing tasks, categories, and users.

## Installation

### Prerequisites

- Python 3.12
- Django 4.x
- pip (Python Package Installer)

### Installation Steps

1. Clone the repository:

    ```sh
    git clone git@github.com:konradthiemann/Kanban-Backend.git
    cd Kanban-Backend
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the database migrations:

    ```sh
    python manage.py migrate
    ```

5. Start the development server:

    ```sh
    python manage.py runserver
    ```

## Configuration

Ensure you configure your Django settings in `kanbanBackend/settings.py`. Pay particular attention to the database settings and other environment variables.

## Usage

### API Endpoints

Here are some of the key endpoints of the Kanban Backend:

- `/todos/` - CRUD operations for tasks
- `/categories/` - CRUD operations for categories
- `/users/` - User management
- `/register/` - User registration
- `/api/token/` - Get Auth Token
- `/api/token/refresh/` - Refresh Auth Token

### Example API Requests

#### Get new Auth Token

Make a POST request to `/api/token/` with username and password in the body like this:
```
{
    "username":"username",
    "password":"password"
}
```
Your response will look like this:
```
{
    "refresh": "refresh token",
    "access": "access token"
}
```

#### Refresh Auth Token
To refresh the current Auth token make a POST request to `/api/token/refresh/` like down below:
```
{
    "refresh":"refresh token"
}
```
Your response will look like this:
```
{
    "access": "access token"
}
```
#### How to handle Todos

- To get all todos you need to make a GET request to `/todos/`
    - You can add filters to the URL like this:
    ```
    /todos/?title=test
    ```
- To create a todo you need to make a POST request to `/todos/`
```sh
curl -X POST http://localhost:8000/api/todos/ -d '{"title": "New Task", "description": "Task description"}' -H "Content-Type: application/json"
```


#### Create a category
To create a new category make a POST request to `/categories/` like down below:
```
{
    "name":"categoryName"
}
```
Your response will look like this:
```
{
    "id": 1,
    "name": "categoryName"
}
``` 
#### Create/register a new User
- To register a new User you need to make a POST request to `/register/`
```
{
    {
      username: testuser,
      email: random@email.com,
      first_name: john,
      last_name: doe,
      password: topSecret,
      confirm_password: topSecret,
    }
}
```
- If your registration fails you get a response with matching error messages for the field that fails.

#### Get list of Users
- To get a JSON of all users make a GET request to `/users/`. 
- You can add filters to the URL.
    - You can filter by `username`, `first_name`, `last_name`, `email`. 
    ```
    /users/?username=admin
    ```

### API Documentation
The full API documentation can be found in the generated HTML files. To generate the documentation, run the following commands:

```sh
    cd docs
    make html
```
Open the generated index.html file in the build/html folder in your browser to view the documentation.

### Testing
To run the tests for the project, use the following command:

```sh
    python manage.py test
```
### Contributing
Contributions are welcome! Please open an issue to report bugs or request features. Pull requests are also welcome.

### Setting Up a Development Environment

1. Fork the repository and clone your fork:
    ```sh
    git clone git@github.com:konradthiemann/Kanban-Backend.git
    cd Kanban-Backend
    ```
2. Create a new branch for your changes:
    ```sh
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m "Description of changes"
    ```
4. Push the branch to your fork:
    ```sh
    git push origin feature-name
    ```
### License
This project is licensed under the MIT License. See the LICENSE file for more details.