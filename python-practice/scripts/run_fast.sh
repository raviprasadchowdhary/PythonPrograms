#!/bin/bash
# Run fast tests only (excludes slow/performance tests)

echo "Running fast tests only..."
pytest -m "not slow and not performance" -v

