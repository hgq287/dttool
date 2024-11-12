# Setup Python virtual environment (virtualenv)

You will run flotool in separated `virtual environment`

```bash
# create virtualenv in directory /dttool/.venv
python3 -m venv .venv

# run virtualenv
source .venv/bin/activate
```

# Install python dependencies

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
