# FastAPI Dependency Injection Demo

This is a demo FastAPI application showcasing dependency injection using [dependency-injector](https://python-dependency-injector.ets-labs.org/).

In this demo, I will try to illustrate that how we can inject dependencies into FastAPI apps with different dependency injection containers.

## A brief Introduction to Dependency Injection
Let's say we have a component (or class) that depends on another component, such as a database connection.

Normally, we would create a database connection in the component itself, creating the dependency inside the class itself, which decreases testability due to we cannot force the component to use a mock database connection in tests easily or configure it differently in different environments (e.g., development, testing, production).

With dependency injection, we say that the component shouldn't create the database connection itself, but receive it from the outside, which allows us to inject a mock database connection in tests or other situations.

For example, you have a class which uses a timer that sleep for 5 hours, but you want to test it quickly, so you want to inject a mock timer that sleeps for 1 second instead or even use a timer that doesn't sleep at all. 

Some people might think that why not just use if-else statements to switch between different behaviors, for example
```python
class CountdownTimer:
    def __init__(self, sleep_time: int = 5 * 60 * 60, is_test: bool = False):
        if is_test:
            self.sleep_time = 1  # 1 second for testing
        else:
            self.sleep_time = sleep_time
        self.sleep_time = sleep_time

    def start(self):
        time.sleep(self.sleep_time)
        print("Countdown finished!")
```

We will see that there are several concerns on a single class like sleeping and switching between different behaviors. With DI, we can define a Timer interface as dependency and implement it outside the component before injecting it into the component

```python
from abc import ABC, abstractmethod
class Timer(ABC):
    @abstractmethod
    def sleep(self, seconds: int):
        pass

class RealTimer(Timer):
    def sleep(self, seconds: int):
        time.sleep(seconds)

class SpyTimer(Timer):
    def sleep(self, seconds: int):
        print(f"Sleeping for {seconds} seconds (spy mode)")

class CountdownTimer:
    def __init__(self, timer: Timer, sleep_time: int = 5 * 60 * 60):
        self.timer = timer
        self.sleep_time = sleep_time

    def start(self):
        self.timer.sleep(self.sleep_time)
        print("Countdown finished!")
```


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
python -m app2.app.main
```

or 
```sh
python -m app.main
```

### References
- [dependency-injector FastAPI example](https://python-dependency-injector.ets-labs.org/examples/fastapi.html)