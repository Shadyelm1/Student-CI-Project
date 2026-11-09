# Student-CI-Project

A small Python calculator used to demonstrate Continuous Integration (CI)
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

- Python 3.8 or newer (standard library only; no packages to install)

## Run the application

```
python -m app.calculator
```

## Run the tests

From the repository root:

```
python -m unittest discover -s tests -t . -v
```

All 6 tests should pass. The command exits with a non-zero code if any
test fails, which is what makes the Jenkins build fail.

## Continuous Integration

The Jenkins Freestyle job **Student-CI-Project**:

1. Pulls this repository from GitHub (branch `main`).
2. Is triggered by a GitHub webhook on every push
   (`GitHub hook trigger for GITScm polling`).
3. Runs `ci\build.bat` (Windows) or `ci/build.sh` (macOS/Linux), which
   syntax-checks the code, runs the app, and runs the unit tests.
4. Marks the build **FAILED** if any test fails.
