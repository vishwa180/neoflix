from app import create_app
import os


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    debug = bool(int(os.environ.get("DEBUG", 0)))
    host = "0.0.0.0"

    app.run(debug=debug, host=host, port=port)
