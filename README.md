# WhiteBoard Project

WhiteBoard is a collaborative drawing application built using Django and Django Channels. It allows multiple users to draw on a shared canvas in real-time.

## Features

- Real-time collaborative drawing using WebSockets.
- Room-based whiteboards for separate collaborative sessions.
- Clear board functionality.
- Cross-origin support for frontend integration.

## Technologies Used

- **Backend**: Django, Django Channels, Daphne
- **WebSocket**: Channels, Channels Redis
- **Frontend**: HTML5 Canvas, JavaScript
- **Database**: SQLite (default, can be replaced with other databases)
- **Other**: Redis (optional for production)

## Prerequisites

- Python 3.8 or higher
- Redis (optional, for production WebSocket handling)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishav-Upadhaya/WhiteBoard.git
   cd WhiteBoard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`.

## WebSocket Configuration

- By default, the project uses an in-memory channel layer for WebSocket communication.
- To use Redis for production, update the `CHANNEL_LAYERS` configuration in `settings.py`:
  ```python
  CHANNEL_LAYERS = {
      'default': {
          'BACKEND': 'channels_redis.core.RedisChannelLayer',
          'CONFIG': {
              "hosts": [('127.0.0.1', 6379)],
          },
      },
  }
  ```

## Usage

1. Navigate to the homepage.
2. Enter a room name to create or join a whiteboard session.
3. Start drawing on the canvas. Changes will be reflected in real-time for all users in the same room.

## File Structure

- **WhiteBoard**: Main Django project folder.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing for the project.
  - `asgi.py`: ASGI configuration for WebSocket support.
  - `wsgi.py`: WSGI configuration for HTTP requests.
- **board**: App folder for the whiteboard functionality.
  - `views.py`: Handles HTTP requests.
  - `urls.py`: URL routing for the app.
  - `consumers.py`: WebSocket consumer for real-time communication.
  - `routing.py`: WebSocket URL routing.
  - `templates/board`: HTML templates for the app.

## Frontend

- The frontend uses HTML5 Canvas for drawing.
- WebSocket is used to send and receive drawing data in real-time.

## Deployment

1. Install a production-grade ASGI server like Daphne or Uvicorn.
2. Use Redis for the channel layer in production.
3. Configure `ALLOWED_HOSTS` and set `DEBUG = False` in `settings.py`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Channels Documentation](https://channels.readthedocs.io/)
