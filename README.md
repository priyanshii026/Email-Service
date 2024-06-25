# Email Creation Service

This is a Flask-based web application that allows you to create and send emails using HTML templates and inline CSS.

## Features

- Generate emails using Jinja2 templates
- Send emails using SMTP
- Supports multiple email templates
- Customizable email details

## Prerequisites

- Python 3.x
- Flask
- Jinja2
- smtplib

## Installation

1. Clone the repository:

```bash
git clone https://github.com/priyanshii026/Email-Service.git
```

2. Navigate to the project directory:

```bash
cd email-service
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Update the `email_details` dictionary in `app.py` with your desired email details.

2. Modify the email templates (`*.html` files in the `templates` directory) to match your design and content requirements.

3. Update the `send_email` function in `app.py` with your SMTP server settings and email addresses.

4. Run the Flask application:

```bash
python app.py
```

5. Access the application in your web browser at `http://localhost:5000/`.

6. To send an email, make a GET request to `/email?email_key=<email_key>` or a POST request to `/email` with the `email_key` and `email_details` in the request body.

## Configuration

- `templates_dir`: The directory where the email templates are stored.
- `email_details`: A dictionary containing the email details for each template.