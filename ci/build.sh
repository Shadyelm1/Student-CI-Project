#!/bin/sh
# Equivalent build step for macOS/Linux Jenkins agents ("Execute shell")
set -e
echo "=== CI Build Started ==="
echo "Build number: ${BUILD_NUMBER:-local}"
echo "=== Checking source files ==="
ls -R app tests
echo "=== Python version ==="
python3 --version
echo "=== Compiling sources (syntax check) ==="
python3 -m compileall -q app tests
echo "=== Running application ==="
python3 -m app.calculator
echo "=== Running Application Tests ==="
python3 -m unittest discover -s tests -t . -v || { echo "TESTS FAILED"; exit 1; }
echo "=== CI Build Completed Successfully ==="
