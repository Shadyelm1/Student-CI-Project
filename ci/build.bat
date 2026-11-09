@echo off
REM Jenkins "Execute Windows batch command" build step for Student-CI-Project
echo === CI Build Started ===
echo Build number: %BUILD_NUMBER%
echo Commit: %GIT_COMMIT%

echo === Checking source files ===
dir /s /b app tests

echo === Python version ===
python --version
if errorlevel 1 (
    echo PYTHON NOT FOUND ON JENKINS AGENT
    exit /b 1
)

echo === Compiling sources (syntax check) ===
python -m compileall -q app tests
if errorlevel 1 (
    echo COMPILATION FAILED
    exit /b 1
)

echo === Running application ===
python -m app.calculator
if errorlevel 1 (
    echo APPLICATION FAILED TO RUN
    exit /b 1
)

echo === Running Application Tests ===
python -m unittest discover -s tests -t . -v
if errorlevel 1 (
    echo TESTS FAILED
    exit /b 1
)

echo === CI Build Completed Successfully ===
exit /b 0
