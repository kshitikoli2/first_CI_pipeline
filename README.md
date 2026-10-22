# Assignment 4: CI Pipeline Using GitHub Actions

Programs 21–30 and their Pytest test cases.

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m pytest -v
```

## GitHub Actions

The workflow in `.github/workflows/python-ci.yml` runs the test suite on pushes and pull requests to `main`.
