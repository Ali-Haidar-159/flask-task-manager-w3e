# init_db.py
from app import app
from config.db import db
import os

def init_database():
    with app.app_context():
        # Show connection details
        db_uri = app.config.get("SQLALCHEMY_DATABASE_URI")
        print(f"Connecting to: {db_uri}")
        
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Verify tables were created
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"Tables in database: {tables}")
        
        # Show table details
        if 'all_task' in tables:
            columns = inspector.get_columns('all_task')
            print(f"Columns in 'all_task': {[c['name'] for c in columns]}")
        else:
            print("'all_task' table not found!")

if __name__ == "__main__":
    init_database()