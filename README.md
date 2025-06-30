# 🧪 Data Quality Automation Framework

This project uses Great Expectations to validate data pipelines. It includes:

- ✅ Expectation suite
- ✅ Sample CSV input
- ✅ CI/CD via GitHub Actions
- ✅ Docker support
- ✅ Data Docs for visual reports

## 🚀 Quickstart

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python scripts/validate_batch.py
```

To build Data Docs:

```bash
python scripts/build_docs.py
open great_expectations/uncommitted/data_docs/local_site/index.html
```

To run in Docker:

```bash
docker build -t dq-check .
docker run --rm dq-check
```
