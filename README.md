Here is your updated `README.md`, reflecting the changes made to include the product management features and adjustments:

---

# BUY4ME E-Commerce Website

## Overview

BUY4ME is an E-Commerce website that allows users to browse products, register, and make purchases. It includes RESTful API endpoints for user authentication, product management, and database integration.

## Features

- **User Authentication**: Register and login functionality.
- **RESTful API**: API routes for users and products.
- **Product Management**: Create, retrieve, and view products.
- **Database Integration**: MySQL database for user and product data.
- **Swagger Documentation**: API documentation via Swagger UI.

## Requirements

- **Python 3.x**: Ensure that Python 3.x is installed on your machine.
- **pip**: Python package installer (usually comes with Python).
- **MySQL**: Ensure MySQL is installed for database functionality.

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/sundaymba/buy4me.git
   ```

2. **Navigate to the project directory**

   Move into the project directory:

   ```bash
   cd buy4me
   ```

3. **Create and Activate Virtual Environment**

   It’s recommended to use a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the required dependencies**

   Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configuration**
   
   Copy `.flaskenv` to `.env`:

   ```bash
   cp .flaskenv .env
   ```

   Define your database credentials in the `.env` file, such as `DB_USERNAME`, `DB_PASSWORD`, `DB_NAME`, etc.

6. **Database Migration Commands**
   
   - Initialize migration:

     ```bash
     flask db init
     ```

   - Generate a migration version:

     ```bash
     flask db migrate -m 'Initial migration'
     ```

   - Upgrade to apply the migrations to the database:

     ```bash
     flask db upgrade
     ```

7. **Running The Application**

   To run the application, use the following command:

   ```bash
   flask run
   ```

8. **Swagger API Docs**

   To access the Swagger API documentation, navigate to the following URL:

   - **Localhost example**: `http://127.0.0.1:5000/apidocs/`
   - This will give you access to the documentation for all the API endpoints, including authentication and product management.

9. **Product Management**

   The application includes API routes for managing products. You can use the following endpoints:
   
   - **GET** `/api/v1/products`: Get all products.
   - **POST** `/api/v1/products`: Create a new product.
   - **GET** `/api/v1/products/{product_id}`: Get a product by its ID.
   
   Full API documentation is available in Swagger.

10. **Contributing**

    If you would like to contribute to this project, please follow these steps:

    1. Fork the repository.
    2. Create a new branch (`git checkout -b feature-branch`).
    3. Make your changes and commit them (`git commit -m 'Add some feature'`).
    4. Push to the branch (`git push origin feature-branch`).
    5. Create a new Pull Request.
    6. Remember to always sync your forked repo with the `dev` branch.

---

This update covers the new product management feature and aligns with the changes has been made in the project.