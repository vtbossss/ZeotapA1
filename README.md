# Rule Engine Project with AST

This is a 3-tier rule engine application to determine user eligibility based on attributes such as age, department, income, and spend. The application leverages an Abstract Syntax Tree (AST) structure for creating, combining, and evaluating rules dynamically.

---

## Table of Contents

1. [Objective](#objective)
2. [Application Architecture](#application-architecture)
3. [Design Choices](#design-choices)
4. [Dependencies](#dependencies)
5. [Build Instructions](#build-instructions)
6. [Usage](#usage)
7. [Available Endpoints](#available-endpoints)
8. [Project Structure](#project-structure)

---

## Objective

The objective of this project is to evaluate user eligibility based on specific rules set with various attributes using a rule engine that dynamically creates, combines, and modifies rules in the form of an AST.

## Application Architecture


- **UI Layer:** The UI layer of this application is powered by the Django REST Framework's built-in HTML interface, which provides a straightforward way for users to interact with the API for testing and development purposes.
- **Documentation:** The documentation is available at /api/ endpoint.
- **API Layer:** Django REST API to handle rule creation, combining, and evaluation.
- **Data Layer:** SQLite database for storing rules and application metadata.

## Design Choices

- **Abstract Syntax Tree (AST):** The project uses ASTs to handle the conditional rules, making them dynamic and modifiable.
- **Database:** SQLite is used for simple storage and retrieval. Other databases can be easily integrated if needed.
- **Dockerization:** Docker and Docker Compose are utilized for an isolated and consistent environment setup.

---

## Dependencies

To set up and run this project, you will need:

- Docker
- Docker Compose
- Git

All application dependencies are listed in `requirements.txt`.

---

## Build Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/vtbossss/ZeotapA1.git

    cd ZeotapA1
    
    cd rule_engine_project
    ```

2. **Set Up Docker**

    Make sure Docker and Docker Compose are installed. You can download Docker [here](https://docs.docker.com/get-docker/).

3. **Build and Run the Docker Containers**

    ```bash
    docker-compose build

    docker-compose up
    ```

   This command will:
   - Build the Docker image for the application.
   - Start up the Django development server and automatically apply migrations.

4. **Access the Application**

   Once running, the application will be accessible at `http://localhost:8000/api/`.

---

## Usage

- **Creating Rules**: Use the UI or the API to create new rules.
- **Combining Rules**: You can combine rules using the API.
- **Evaluating Rules**: Pass user attributes to the API to determine eligibility.

---

## Available Endpoints

### 1. Create Rule

- **Endpoint**: `POST /api/create-rule/`
- **Usage**:
  - URL: `http://localhost:8000/api/create-rule/`
  - Request Body Example 1 (for Rule 1):
    ```json
    {
        "rule_name": "Rule 1",
        "rule_string": "(((age > 30) and (department == 'Sales')) or ((age < 25) and (department == 'Marketing'))) and ((salary > 50000) or (experience > 5))"
    }
    ```
    Note: The rule ID included in the response can be used for future reference or can be accessed through the "get-all-rules" endpoint.
    
  - Request Body Example 2 (for Rule 2):
    ```json
    {
        "rule_name": "Rule 2",
        "rule_string": "((age > 30) and (department == 'Marketing')) and ((salary > 20000) or (experience > 5))"
    }
    ```

    #Note- the rule id displayed in the response to use further or this can be accessed further in get-all-rules endpoint

### 2. Evaluate Rule

- **Endpoint**: `POST /api/evaluate-rule/`
- **Usage**:
  - URL: `http://localhost:8000/api/evaluate-rule/`
  - Request Body Example 1 (for Rule 1):
    ```json
    {
        "rule_id": 1, #use rule id of your rule this id is for example purpose
        "user_data": {
            "age": 32,
            "department": "Sales",
            "salary": 60000,
            "experience": 6
        }
    }
    ```
    Rule 1 Output: True
    
  - Request Body Example 2 (for Rule 2):
    ```json
    {
        "rule_id": 2, #use rule id of your rule this id is for example purpose
        "user_data": {
            "age": 31,
            "department": "Marketing",
            "salary": 25000,
            "experience": 6
        }
    }
    ```
    Rule 2 Output: True

---

### 3. Get All Rules

- **Endpoint**: `GET /api/get-all-rules/`
- **Usage**:
  - URL: `http://localhost:8000/api/get-all-rules/`
  - Method: `GET`
  - No request body needed.

## Project Structure

```plaintext
ZeotapA1/
├── rule_engine_project/
│   ├── rule_engine_project/       # Django project directory
│   │   ├── __pycache__/           # Compiled bytecode files
│   │   ├── __init__.py
│   │   ├── asgi.py                # ASGI configuration for async support
│   │   ├── settings.py            # Django project settings
│   │   ├── urls.py                # URL configuration
│   │   └── wsgi.py                # WSGI configuration for web servers
│   ├── rules/                     # Application for rule engine logic
│   │   ├── __pycache__/           # Compiled bytecode files
│   │   ├── migrations/            # Database migration files
│   │   │   ├── __pycache__/
│   │   │   ├── __init__.py
│   │   │   └── 0001_initial.py    # Initial migration file
│   │   ├── __init__.py
│   │   ├── admin.py               # Admin configuration for rules
│   │   ├── apps.py                # App configuration
│   │   ├── ast_helper.py          # Helper functions for AST manipulations
│   │   ├── models.py              # Database models for rules
│   │   ├── serializers.py         # Serializers for API data formatting
│   │   ├── tests.py               # Test suite for rules
│   │   ├── urls.py                # URL patterns for rules app
│   │   ├── utils.py               # Utility functions
│   │   └── views.py               # Views handling rule-related requests
│   ├── templates/                 # HTML templates for UI
│   │   ├── api.html               # API documentation page
│   │   ├── base.html              # Base template for the application
│   │   └── create_rule.html       # Rule creation page
│   ├── db.sqlite3                 # SQLite database file
│   ├── docker-compose.yml         # Docker Compose configuration file
│   ├── Dockerfile                 # Dockerfile to containerize the application
│   ├── manage.py                  # Django management script
│   └── requirements.txt           # Python dependencies for the project
