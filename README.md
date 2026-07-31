# ICPMS-data

ICP-MS run data analysis tool. Upload the run spreadsheet on the Home page,
then step through the analysis using the pages in the sidebar.

## Getting started on a new laptop

This repo is **private** - whoever's setting this up needs to be added as a
collaborator on .[github.com/jennyl28/ICPMS-data](https://github.com/jennyl28/ICPMS-data)
first (by Jenny), as cloning will fail with a permission error.

**1. Install `uv`** (Python's package/dependency manager - skip if already installed):

- macOS/Linux:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Windows (Terminal - Command Prompt):
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

Close and reopen your terminal afterward, then confirm it worked with `uv --version`.

**2. Clone the repo and move into it:**

```bash
git clone https://github.com/jennyl28/ICPMS-data.git
cd ICPMS-data
```

**3. Install dependencies** (run this from inside the `ICPMS-data` folder -
`uv` needs to find `pyproject.toml` in the current directory):

```bash
uv sync
```

**4. Run the app:**

```bash
uv run streamlit run Home.py
```

This opens the app in your browser at `http://localhost:8501`. The terminal
