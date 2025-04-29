# Enterprises Management API
==========================

This API is designed to manage enterprise data efficiently. It follows a clean architecture using controllers, services, middlewares, and a relational MySQL database with SQLAlchemy.

## Prerequisites
-------------
Make sure you have the following installed on your system:
- Python 3.x
- MySQL
- pip (Python package manager)

## Installation
------------
1. Install dependencies:
   From the root directory of the project, run:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
   Inside the /api folder, create a .env file based on the .env.example.
   It should contain:

   ```ini
   JWT_SECRET_KEY="your-cool-jwt-secret-here-in-string-format"
   JWT_ACCESS_TOKEN_EXPIRES=3600
   DATABASE_URL="your-cool-mysql-database-url-here"
   ```

## Running the Server
------------------
From the root folder (/enterprises-management-api), run:
```bash
python ./api/server.py
```

## server.py
---------
This is the entry point of the application. It creates an instance of the Flask app, enables debug mode, and starts the server using Waitress to serve the app on port 5000.

## app.py
------
This file is responsible for configuring the Flask application. It:
- Loads environment variables
- Connects to the MySQL database using SQLAlchemy
- Enables CORS to allow requests from the frontend
- Sets up migrations using Flask-Migrate
- Initializes JWT authentication
- Registers all application routes
- Enables Swagger API documentation

## About the API
-------------
### The API provides endpoints for:

- client: create, delete, edit, get (filtered and all)
- enterprise: create, delete, edit, get (filtered and all)
- product: create, delete, edit, get (filtered and all)
- representative: login, create, delete, edit, get (filtered and all)

All routes use middleware and controller layers. Database models are managed using SQLAlchemy.

### Database structure
------------------
- A representative is the owner of an enterprise.
- An enterprise is linked to clients and products.
- Clients and products are not directly related to each other.

## How to Use
----------
1. First, log in using the representative login route.
2. Use the returned bearer token to authorize requests.
3. Create an enterprise.
4. Create a representative linked to the created enterprise.
5. With the representative and enterprise in place, you can now create clients and products associated with that enterprise.
