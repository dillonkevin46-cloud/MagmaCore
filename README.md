# MagmaCore

A unified IT management platform containing a Helpdesk (Ticketing), Asset Registry, and Knowledge Base.

## Design Philosophy

MagmaCore features a "Glassmorphism" aesthetic with semi-transparent backgrounds, modern typography (Inter/Poppins), and soft shadows.

## Tech Stack

*   **Backend:** Django 5.x (Python)
*   **Database:** PostgreSQL (with `psycopg2-binary`)
*   **Frontend:** HTML5, Bootstrap 5, Custom SCSS
*   **Server:** Waitress (for Windows/IIS)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd MagmaCore
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/Mac
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup (PostgreSQL):**
    Ensure PostgreSQL is installed and running. Create a database named `magmacore_db`.
    Update environment variables or `MagmaCore/settings.py` with your DB credentials if different from defaults.

    To run with SQLite for development/testing:
    ```bash
    export USE_SQLITE=True  # Linux/Mac
    set USE_SQLITE=True     # Windows
    ```

5.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run Server:**
    ```bash
    python manage.py runserver
    ```
    or for production simulation with Waitress:
    ```bash
    waitress-serve --port=8000 MagmaCore.wsgi:application
    ```

## Project Structure

*   `app_core`: Base layout, navigation, authentication.
*   `app_tickets`: Helpdesk system (Tickets, Comments).
*   `app_assets`: Asset Registry (Assets with dynamic JSON specs).
*   `app_kb`: Knowledge Base (Articles).

## Verification

The frontend has been verified to meet the Glassmorphism design requirements.
