# ntou2.0

This repository serves the website of kobe NTOU. This project is open source and the license can be found in LICENSE.

## Getting Started

### Requirements

- Git 1.8+
- Python 3.7.x

### Set up a Virtual Environment

#### Python - Built-in `venv`

Create your virtual environment:

    python3 -m venv venv

And enable it:

    . venv/bin/activate
    
### Install Dependencies

Use pip to install Python depedencies:

    pip install -r requirements.txt
    
### Get Ready for Development

`cd` into the `ntou` directory:

    cd ntou

And migrate the database:

    python manage.py migrate

Now you’re all set!

## Run the Development Server

    python manage.py runserver

