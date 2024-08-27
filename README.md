# FastAPI Application with Jinja2 Templates

## Overview
This project is a web application built using FastAPI for the backend and Jinja2 for templating. The application is designed to be a simple and efficient starting point for building web applications with these technologies.

## Features
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.8+.
- **Jinja2**: A full-featured template engine for Python, used for rendering HTML templates.
- **BulmaCSS**: A modern CSS framework based on Flexbox (via CDN).
- **jQuery**: A fast, small, and feature-rich JavaScript library (via CDN).
- **Dependency Management**: Managed using Poetry, a tool for dependency management and packaging in Python.

## Project Structure
```
.
├── app.py                  # The main FastAPI application
├── templates/              # Directory for Jinja2 templates
│   ├── base.html.jinja2    # Base template
│   └── index.html.jinja2   # Index template
├── pyproject.toml          # Poetry configuration file
├── poetry.lock             # Poetry lock file
└── README.md               # Project README file
```

## Getting Started

### Prerequisites
- Python 3.8+
- Poetry (for dependency management)

### Installation
1. Clone the repository:
```bash
$ git clone https://github.com/PR-Pilot-AI/rapid-prototyper.git
$ cd rapid-prototyper
```
2. Install dependencies using Poetry:
```bash
$ poetry install
```

### Running the Application
You can run the application using Uvicorn, an ASGI server for Python:
```bash
$ uvicorn app:app --reload
```
This will start the FastAPI application, and you can access it at `http://127.0.0.1:8000/`.

## Usage
- The root path (`/`) serves the `index.html.jinja2` template, which inherits from `base.html.jinja2`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
