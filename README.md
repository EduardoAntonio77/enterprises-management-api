# Enterprises Management API

This API is designed to manage enterprise data efficiently. Follow the instructions below to set it up and run the server.

## Prerequisites

Before running the API, ensure that you have the following installed:
- Python 3.x
- MySQL database
- `pip` for managing dependencies

## Installation

1. **Install dependencies**:
   
   In the root directory of the project, run the following command to install the required dependencies:

   ```bash
        pip install -r requirements.txt
   ```

2. **Set up environment variables:**
    Inside the `/api` folder, create a `.env` file based on the format provided in `.env.example.` You need to configure the following variables:
    ```ini
        JWT_SECRET_KEY="your-cool-jwt-secret-here-in-string-format"
        JWT_ACCESS_TOKEN_EXPIRES=3600  # 3600 seconds = 1 hour
        DATABASE_URL="your-cool-mysql-database-url-here"
    ```
    Make sure to replace the placeholder values with your own JWT secret key and MySQL database URL.

## Running the Server
Once you've set up the environment variables, you can run the API server.

To start the server, use the following command from the root project folder (`/enterprises-management-api`):

```bash
python ./api/server.py
```