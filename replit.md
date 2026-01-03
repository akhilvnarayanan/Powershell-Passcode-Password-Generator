# Password Generator

## Overview
A web-based password generator that creates secure random passwords. This is a web adaptation of the original PowerShell password generator script.

## Features
- Generate passwords with customizable length
- Configure the number of special (non-alphanumeric) characters
- Copy generated passwords to clipboard with one click

## Project Structure
- `app.py` - Flask backend server with password generation logic
- `templates/index.html` - Frontend HTML/CSS/JS interface
- `random_password_generator.ps1` - Original PowerShell script (for reference)

## Running the Application
The application runs on port 5000 using Flask. Start with:
```
python app.py
```

## API Endpoints
- `GET /` - Serves the main password generator interface
- `POST /generate` - Generates a password
  - Request body: `{"length": 12, "nonAlpha": 2}`
  - Response: `{"password": "generated_password"}`

## Technology Stack
- Python 3.11
- Flask (web framework)
- HTML/CSS/JavaScript (frontend)
