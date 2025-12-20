Django backend scaffold

Setup (Windows PowerShell):

1. Create and activate a virtual environment
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies
```powershell
pip install -r requirements.txt
```

3. Run migrations and start server
```powershell
python manage.py migrate
python manage.py runserver
```

4. Health check
Open `http://127.0.0.1:8000/api/status/` — should return JSON {"status":"ok"}

Notes:
- CORS is enabled for all origins in development via `CORS_ALLOW_ALL_ORIGINS = True` in settings.
- Replace `SECRET_KEY` with a secure value and set `DEBUG = False` in production.
