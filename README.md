# Virtual Column (pandas)

Utility function that adds a computed ("virtual") column to a pandas DataFrame based on a simple rule:

`<column> <op> <column>` where `op` is one of: `+`, `-`, `*`.

Whitespace is optional (e.g. `quantity*price` and `quantity * price` both work).

## Setup

### Create virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
