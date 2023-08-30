# poll_app

This repository contains a simple polls app created following Django's documentation tutorial. The app utilizes Django's features to manage a database, including generic views and tests.

## Repository Structure

### django_apps (project directory)
- **main files:**
  - `settings.py`: Contains project configurations.
  - `urls.py`: Connects to the poll app.

### Poll (app directory):
- **templates** (contains necessary HTML files):
  - `details.html`
  - `index.html`
  - `layout.html`
  - `result.html`
- `models.py`: Defines application models.
- `admin.py`: Configures the admin interface.
- `tests.py`: Includes tests for app functionality.
- `urls.py`: Defines URLs for the app views.
- `views.py`: Contains views for app functionality.

## Setup Instructions

1. Clone the repository onto your system.
2. Create a virtual environment and install Django.
3. Create a superuser for the admin interface.
4. Start the server and navigate to `/poll` to use the app.
