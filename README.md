
# CourseWeb — Online Course Finder (Flask)

A lightweight Online Course Finder called **CourseWeb** built with HTML/CSS/JS frontend and a Python (Flask) backend.
Theme: Light / white. Logo inspired by colorful social-camera style using the name "CourseWeb".

## Features
- Browse courses, filter by category/platform/price, search and sort.
- Submit courses via a server-side POST endpoint (stored in `data/courses.json`).
- Simple API: `GET /api/courses` and `POST /api/courses`.
- Ready to run locally and deploy to Python-capable hosts (Render, Fly, Railway, Heroku alternatives).

## Run locally (Linux/macOS/WSL)
1. Create a venv: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open http://localhost:5000

## Deploy
- For simple deploy, use platforms that support Python (Render, Railway, Fly.io, etc.).
- Ensure `requirements.txt` is used and set web command to `gunicorn app:app` or use `python app.py` for development.

## Notes & Next steps
- Replace example course URLs with real affiliate links for monetization.
- Add authentication and admin UI to approve submissions for production.
- Use a real database (Postgres, Supabase) for concurrency and reliability.
