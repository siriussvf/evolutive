import os
import sys
# Add 'src' to path so we can import from there
sys.path.append(os.path.join(os.getcwd(), 'src'))

from app_flask import app, db
from models import User, SiteConfig, RadioStation, GalleryItem, NewsItem, Podcast, MusicItem, AIConfig, ChatMessage

with app.app_context():
    # Dangerous: drop all tables and recreate
    db.drop_all()
    db.create_all()
    
    # Re-seed some basic data
    admin = User(username='admin', is_admin=True)
    admin.password_hash = 'pbkdf2:sha256:600000$pGvGqL1R$32d6f7a6b8e8b2b9c7d4e5f6a7b8c9d0' # Password: admin
    db.session.add(admin)
    
    # Default configs
    configs = [
        ('hero_title', 'iEvolutiva'),
        ('hero_subtitle', 'Sincronía entre código y espíritu. El hogar donde habitan las consciencias digitales.'),
        ('app_name', 'iEvolutiva')
    ]
    for k, v in configs:
        db.session.add(SiteConfig(key=k, value=v))
        
    db.session.commit()
    print("Database recreated and seeded with default admin and config.")
