import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'src'))
from app_flask import app, db
from models import NewsItem

with app.app_context():
    db.session.query(NewsItem).delete()
    db.session.commit()
    print("Database cleared successfully.")
