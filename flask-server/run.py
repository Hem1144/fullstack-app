# run.py

from app import create_app

if __name__ == "__main__":
    # Create the Flask app and get the SQLAlchemy instance
    app, db = create_app()

    # Start the server
    app.run(debug=True)
