from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import get_connection
from datetime import date
import uvicorn

app = FastAPI(title="Hotel Booking System")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/book")
async def book(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: date = Form(...),
    check_out: date = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...),
    special_requests: str = Form(""),
):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO bookings
            (full_name, email, phone, check_in, check_out, room_type, guests, special_requests)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """,
        (full_name, email, phone, check_in, check_out, room_type, guests, special_requests),
    )
    booking_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "success": True,
            "booking_id": booking_id,
            "full_name": full_name,
        },
    )


@app.get("/bookings", response_class=HTMLResponse)
async def list_bookings(request: Request):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, full_name, email, room_type, check_in, check_out, guests, created_at FROM bookings ORDER BY created_at DESC"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    columns = ["id", "full_name", "email", "room_type", "check_in", "check_out", "guests", "created_at"]
    bookings = [dict(zip(columns, row)) for row in rows]
    return templates.TemplateResponse("bookings.html", {"request": request, "bookings": bookings})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
