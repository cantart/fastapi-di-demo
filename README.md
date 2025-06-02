# FastAPI Dependency Injection Demo

This is a demo FastAPI application showcasing dependency injection using [dependency-injector](https://python-dependency-injector.ets-labs.org/).

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (for environment and dependency management)

### Installation

```sh
uv pip install -e ".[dev]"
```

### Environment Variables
Copy `.env.example` to `.env`:
```sh
cp .env.example .env
```

### Running the Application
```sh
fastapi dev app/main.py
```

### References
- [dependency-injector FastAPI example](https://python-dependency-injector.ets-labs.org/examples/fastapi.html)