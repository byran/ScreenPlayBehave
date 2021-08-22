@echo off

cd "%~dp0"

rmdir /S /Q .venv
python -m venv .venv

echo run '.venv\Scripts\activate.bat' to active the environment
