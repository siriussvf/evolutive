from src.app_flask import app, db
from src.models import NewsItem

with app.app_context():
    NewsItem.query.delete()
    db.session.commit()
    print("Database cleared for news items.")
