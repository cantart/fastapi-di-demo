# FastAPI Dependency Injection Demo

This is a demo FastAPI application showcasing dependency injection using [dependency-injector](https://python-dependency-injector.ets-labs.org/).

## Why Dependency Injection?
Let's say we have a component (or class) that depends on another component, such as a database connection.

Traditionally, we would create a database connection in the component itself, creating the dependency inside the class itself, which decreases testability due to we cannot force the component to use a mock database connection in tests easily or configure it differently in different environments (e.g., development, testing, production).

For example, you have a class which uses a timer that sleep for 5 hours, but you want to test it quickly, so you want to inject a mock timer that sleeps for 1 second instead or even use a timer that doesn't sleep at all.

With dependency injection, we say that the component shouldn't create the database connection itself, but receive it from the outside, which allows us to inject a mock database connection in tests or other situations.

Formally, this idea is like the `abstraction` and `polymorphism` principle in OOP, where we define an interface (or abstract class) for the dependency and implement it in a concrete class. The component then depends on the interface, not the concrete implementation.

## Why Python Dependency Injector?
Typically, we can do the dependency injection ourselves by passing the dependencies to the component's constructor or methods directly. However, this can become hard to manage as the number of dependencies grows, especially in larger applications.

This is why we use a dependency injection framework like [dependency-injector](https://python-dependency-injector.ets-labs.org/). It allows us to define dependencies in a declarative way, manage their lifecycle, and inject them into components automatically. So, our main jobs are defining the dependency injection container, telling the framework how to create each dependency and where to inject it.

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