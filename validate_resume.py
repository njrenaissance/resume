import json
import sys
from pathlib import Path
import requests
from jsonschema import Draft7Validator, exceptions

repo_root = Path(__file__).parent
resume_path = repo_root / 'resume.json'
if not resume_path.exists():
    print(f"ERROR: {resume_path} not found")
    sys.exit(2)

with open(resume_path, 'r', encoding='utf-8') as f:
    resume = json.load(f)

local_schema_path = repo_root / 'jsonresume-schema.json'
schema = None
if local_schema_path.exists():
    try:
        with open(local_schema_path, 'r', encoding='utf-8') as sf:
            schema = json.load(sf)
        print(f"Using local schema at {local_schema_path}")
    except Exception as e:
        print(f"WARN: failed to load local schema {local_schema_path}: {e}")

if schema is None:
    schema_url = 'https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json'
    try:
        r = requests.get(schema_url, timeout=10)
        r.raise_for_status()
        schema = r.json()
        print(f"Fetched schema from {schema_url}")
    except Exception as e:
        print(f"ERROR: failed to fetch schema from {schema_url}: {e}")
        sys.exit(2)

validator = Draft7Validator(schema)
errors = sorted(validator.iter_errors(resume), key=lambda e: e.path)
if not errors:
    print('VALID: resume.json conforms to the JSON Resume schema')
    sys.exit(0)

print('INVALID: resume.json does NOT conform to the JSON Resume schema')
print(f'{len(errors)} error(s) found:')
for i, err in enumerate(errors, 1):
    # path to the failing element
    path = '.'.join(str(p) for p in err.absolute_path)
    if not path:
        path = '(root)'
    print(f"\n{i}) Path: {path}\n   Message: {err.message}")

sys.exit(2)
