# 00 — Setup

## Create a virtual environment
Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run notebooks in VS Code or start Jupyter with `jupyter notebook`.

## Verify installation
```python
import numpy, pandas, matplotlib, sklearn
print("NumPy:", numpy.__version__)
print("pandas:", pandas.__version__)
print("scikit-learn:", sklearn.__version__)
```

If installation fails, record the Python version and full error message before troubleshooting.
