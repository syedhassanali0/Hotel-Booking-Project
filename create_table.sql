-- Hotel Booking System — PostgreSQL Schema
-- Run this file once to create the required table.

CREATE TABLE IF NOT EXISTS bookings (
    id               SERIAL PRIMARY KEY,
    full_name        VARCHAR(120)  NOT NULL,
    email            VARCHAR(120)  NOT NULL,
    phone            VARCHAR(30)   NOT NULL,
    check_in         DATE          NOT NULL,
    check_out        DATE          NOT NULL,
    room_type        VARCHAR(50)   NOT NULL,
    guests           SMALLINT      NOT NULL CHECK (guests BETWEEN 1 AND 10),
    special_requests TEXT          DEFAULT '',
    created_at       TIMESTAMPTZ   NOT NULL DEFAULT NOW()
);

-- Optional: index for fast lookups by email
CREATE INDEX IF NOT EXISTS idx_bookings_email ON bookings (email);
