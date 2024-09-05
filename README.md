# BUY4ME E-Commerce Website

## Overview

This is an E-Commerce Website called BUY4ME.

## Features

- [User Authentication]
- [RestFul API]
- [Database Integration]

## Requirements

- **Python 3.x**: Ensure that Python 3.x is installed on your machine.
- **pip**: Python package installer (usually comes with Python).

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/sundaymba/buy4me.git

2. **Navigate to the project directory**

    Move into the project durectory

    ```bash
    cd buy4me

3. **Create an Activate Virtual Environment**

    It’s recommended to use a virtual environment to manage dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


4. **Install the required dependencies**

    Install the required packages using pip

    ```bash
    pip install -r requirements.txt

5. **Configuration**
    
    copy .flaskenv to .env
    run the following command below
    ```bash
    cp .flaskenv .env

    define your database credentials in the .env file
    
6. **migration commands**
    
    initialize migration
    ```bash
    flask db init

    generate a migration version
    ```bash
    flask db migrate -m 'any message'

    upgrade to database
    ```bash
    flask db upgrade

7. **Runing The Application**

    To run the application, use the following command:

    ```bash
    flask run

8. **swagger API docs**
    to access the swagger API doc
    navigate to the following URL
    server_url/apidocs

    localhost example: http://127.0.0.1:5000/apidocs/

9. **Contributing**

    If you would like to contribute to this project, please follow these steps:

    1. Fork the repository.
    2. Create a new branch (git checkout -b feature-branch).
    3. Make your changes and commit them (git commit -m 'Add some feature').
    4. Push to the branch (git push origin feature-branch).
    5. Create a new Pull Request.
    6. remember to always sync your forked repo with the dev branch.