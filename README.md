# Student-CI-Project

In-Class assignment
with Jenkins and GitHub webhooks (CMSC 426, In-Class Activity 3).

## Repository layout

```
Student-CI-Project/
├── app/
│   ├── __init__.py
│   └── calculator.py        # application code
├── tests/
│   ├── __init__.py
│   └── test_calculator.py   # unittest test cases
├── ci/
│   ├── build.bat            # Jenkins build step (Windows agent)
│   └── build.sh             # Jenkins build step (macOS/Linux agent)
├── .gitignore
└── README.md
```

## Requirements

- Python 3.8 or newer

## Run the application

```
python -m app.calculator
```
```
python3 -m app.calculator
```

## Run the tests

From the repository root:

```
python -m unittest discover -s tests -t . -v
```
```
python3 -m unittest discover -s tests -t . -v
```

All 6 tests should pass. if any
test fails, which is what makes the Jenkins build fail.

## Continuous Integration


1. Pulls this repo from GitHub.
2. Is triggered by a GitHub webhook on every push
3. Runs  `ci/build.sh`, which syntax-checks the code, runs the app, and runs the unit tests.
4. Marks the build **FAILED** if any test fails.
