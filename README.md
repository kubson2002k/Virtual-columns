# Virtual Column (pandas)

Utility function that adds a computed ("virtual") column to a pandas DataFrame based on a simple rule:

`<column> <op> <column>` where `op` is one of: `+`, `-`, `*`.

Whitespace is optional (e.g. `quantity*price` and `quantity * price` both work).

---

## Setup

### Create virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

 **Mac / Linux:**
 ```powershell
 python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Usage**
 ```powershell
import pandas as pd
from solution import add_virtual_column

fruits_sales = pd.DataFrame({
    "name": ["banana", "apple"],
    "quantity": [10, 3],
    "price": [10, 1],
})

sales_total = add_virtual_column(fruits_sales, "quantity * price", "price_total")
print(sales_total)
```

**Expected output:**

<img width="289" height="53" alt="image" src="https://github.com/user-attachments/assets/1d12fb76-f81c-4795-9e32-8a146407b951" />
