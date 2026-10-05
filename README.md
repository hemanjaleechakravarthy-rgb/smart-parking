# Smart Parking Space Management System



A Python-based Smart Parking Space Management System developed for the Computational Thinking and Programming project.



The system demonstrates computational thinking, algorithm design, data structures, object-oriented programming, functional programming, concurrency, software testing, performance evaluation, CI/CD, Docker, and AI-assisted software engineering.



## Project Objective



The system manages parking-slot allocation for vehicles by selecting suitable available parking spaces based on distance and allocation requirements.



It demonstrates multiple algorithmic approaches to the same parking allocation problem and compares their performance.



## Key Features



- Smart parking slot allocation

- Greedy algorithm

- Dynamic Programming

- Divide and Conquer

- Backtracking

- Branch and Bound

- Priority Queue using Min-Heap

- Object-Oriented Programming

- Inheritance and composition

- Strategy Design Pattern

- Factory Design Pattern

- Observer Design Pattern

- Repository Design Pattern

- Functional programming

- Higher-order functions

- List comprehensions

- Generators

- Decorators

- Context managers

- Threading

- Multiprocessing

- Async programming

- Unit testing

- Integration testing

- End-to-End testing

- Property-based testing with Hypothesis

- 94% code coverage

- Static type checking with mypy

- Linting and formatting with Ruff

- Performance benchmarking

- Streamlit user interface

- Docker containerisation

- GitHub Actions CI/CD

- AI-assisted development with human validation



## Technologies Used



- Python 3.12

- Pytest

- Hypothesis

- pytest-cov

- mypy

- Ruff

- Streamlit

- Matplotlib

- Docker

- GitHub Actions

- Git



## Project Structure



```text

smart-parking/

│

├── app/

│   ├── models/

│   │   ├── parking_slot.py

│   │   ├── vehicle.py

│   │   └── parking_lot.py

│   │

│   ├── algorithms/

│   │   ├── greedy.py

│   │   ├── dynamic_programming.py

│   │   ├── divide_conquer.py

│   │   ├── backtracking.py

│   │   └── branch_bound.py

│   │

│   ├── services/

│   │   ├── parking_manager.py

│   │   ├── concurrent_manager.py

│   │   ├── async_manager.py

│   │   ├── process_manager.py

│   │   ├── parking_strategy.py

│   │   ├── parking_strategy_factory.py

│   │   ├── parking_observer.py

│   │   └── parking_repository.py

│   │

│   └── utils/

│       ├── functional.py

│       ├── decorators.py

│       ├── context_manager.py

│       └── priority_queue.py

│

├── tests/

├── benchmarks/

├── docs/

├── streamlit_app.py

├── main.py

├── Dockerfile

├── requirements.txt

├── pytest.ini

└── .github/

&#x20;   └── workflows/

&#x20;       └── ci.yml

