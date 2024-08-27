# Rapid Prototyper

This project enables **AI-assisted rapid prototyping** of web applications using FastAPI and Jinja2,
allowing developers to explore and iterate on ideas quickly to get a working prototype.

## Idea / Goal of the Prototype
We website that generates / plays background noise for programmers, customizable with sliders and knobs

## Problem Statement
As a programmer, I don't want to listen to music because it is too distracting

## Scope and Limitations
Noise should be generated in the browser. Parameters should be adjustable with sliders

## Prerequisites
For this project, you need to have the following installed:
- [Docker](https://www.docker.com/)
- [PR Pilot CLI](https://github.com/PR-Pilot-AI/pr-pilot-cli)

## How it Works
AI assistance is provided by the [PR Pilot platform](https://www.pr-pilot.ai). Any changes to this project
can be made using natural language prompts using the [PR Pilot CLI](https://github.com/PR-Pilot-AI/pr-pilot-cli).

### Plan
First, you need to clearly define the idea you'd like to explore, the problem 
you're trying to solve, and the scope of the prototype. For example:

```shell
pilot run initialize
```

This will set up the project with the necessary details and an initial implementation.

### Build
Once your project is initialized, you can use PR Pilot to make changes to the project:

```shell
pilot task ""
```

### Ship
...

### Evaluate
...

## Technologies Used
We chose the following technologies for this project:

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.8+.
- **Jinja2**: A full-featured template engine for Python, used for rendering HTML templates.
- **BulmaCSS**: A modern CSS framework based on Flexbox (via CDN).
- **jQuery**: A fast, small, and feature-rich JavaScript library (via CDN).
- **MongoDB**: A schema-less DB for storing data.

This stack was chosen with the following goals in mind:
- **Speed**: We chose technologies that allow for rapid development and iteration.
- **Flexibility**: All of the above libraries are simple, flexible and easy to use in combination.
- **Simplicity**: You shouldn't have to worry about complex configurations or setups.
- **Popularity**: These technologies are widely used and have a large community, making it easier to find help and resources.

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

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
