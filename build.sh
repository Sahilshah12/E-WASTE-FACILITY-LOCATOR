#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=========================================="
echo "Starting Render Build Process"
echo "=========================================="

echo "==> Python version:"
python --version

echo "==> Upgrading pip..."
pip install --upgrade pip

echo "==> Installing dependencies..."
pip install -r requirements.txt

echo "==> Collecting static files..."
python manage.py collectstatic --no-input --clear
echo "Static files collected successfully!"

echo "==> Running database migrations..."
python manage.py migrate --noinput
echo "Migrations completed successfully!"

echo "==> Creating cache table (if needed)..."
python manage.py createcachetable || echo "Cache table already exists or not needed"

echo "=========================================="
echo "Build completed successfully!"
echo "=========================================="
