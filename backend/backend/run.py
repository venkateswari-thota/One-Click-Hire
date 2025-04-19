from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Initialize the database
    app.run(debug=True, host='localhost', port=5000, use_reloader=True)
