# 🏨 Grand Vista Hotel — Booking System

A full-stack hotel booking web application built with **FastAPI**, **Jinja2**, and **PostgreSQL**.

---

## 🚀 Tech Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Backend    | Python 3.11+, FastAPI, Uvicorn |
| Frontend   | HTML5, CSS3, Vanilla JS        |
| Database   | PostgreSQL (psycopg2)          |
| Templating | Jinja2                         |
| Deployment | Vercel                         |

---

## 📁 Project Structure

```
hotel-booking-project/
│
├── main.py              # FastAPI app — routes & logic
├── database.py          # PostgreSQL connection
├── models.py            # Pydantic schemas
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel deployment config
├── .env.example         # Environment variable template
├── .gitignore
│
├── templates/
│   ├── index.html       # Booking form page
│   └── bookings.html    # All reservations page
│
├── static/
│   └── style.css        # Stylesheet
│
└── sql/
    └── create_table.sql # Database schema
```

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hotel-booking-project.git
cd hotel-booking-project
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env and fill in your PostgreSQL credentials
```

### 5. Create the database table
```bash
psql -U postgres -d hotel_booking -f sql/create_table.sql
```

### 6. Run the development server
```bash
uvicorn main:app --reload
```

Visit **http://localhost:8000** in your browser.

---

## 🌐 API Endpoints

| Method | Path       | Description                      |
|--------|------------|----------------------------------|
| GET    | `/`        | Render the booking form           |
| POST   | `/book`    | Submit a booking (stores to DB)   |
| GET    | `/bookings`| View all reservations             |

---

## ☁️ Deployment on Vercel

1. Push this repo to GitHub.
2. Log in to [vercel.com](https://vercel.com) and click **New Project**.
3. Import your GitHub repository.
4. Add environment variables under **Settings → Environment Variables**:
   - `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`
5. Click **Deploy**.
6. Test the live URL — submit a booking and verify it appears in `/bookings`.

> **Tip:** Use [Supabase](https://supabase.com) or [Neon](https://neon.tech) for a free hosted PostgreSQL instance compatible with Vercel.
