# CI/CD Pipeline Demo

![Tests](https://github.com/jeelanbasha/ci-cd-pipeline-demo/actions/workflows/test.yml/badge.svg)

A simple Flask application with automated testing and CI/CD pipeline.

## What This Does
- Flask REST API with 3 endpoints
- Automated testing with pytest
- CI/CD with GitHub Actions
- Containerized with Docker (coming next)

## Run Locally
```bash
python -m venv venv
source venv/bin/activate
pip install flask pytest
python app.py
```

## Run Tests
```bash
pytest -v
```

## Endpoints
- `GET /` - Hello World
- `GET /health` - Health check
- `GET /api/test` - Test endpoint
