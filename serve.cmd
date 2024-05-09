@echo off

if not exist ".venv" (
    python -m venv .venv
) else (
    echo venv exists
)

start cmd.exe /k ".\.venv\Scripts\activate.bat && uvicorn main:app --reload --host 0.0.0.0 --port 8000"
