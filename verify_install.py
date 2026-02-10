import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from app_flask import app, db, User, SiteConfig

def verify():
    print("🔮 Iniciando verificación de Inteligencia Evolutiva...")
    
    with app.app_context():
        # 1. Crear Base de Datos
        print("🛠️  Verificando Base de Datos...")
        db.create_all()
        print("✅ Base de Datos creada/verificada.")
        
        # 2. Verificar Admin
        admin = User.query.filter_by(username="admin").first()
        if not admin:
            print("⚠️  Usuario Admin no encontrado. Creándolo...")
            # Logic is already in app_flask main, but good to have here explicitly or trigger it
            from werkzeug.security import generate_password_hash
            hashed_pw = generate_password_hash("admin", method='pbkdf2:sha256')
            admin = User(username="admin", password_hash=hashed_pw, is_admin=True)
            db.session.add(admin)
            db.session.commit()
            print("✅ ADMIN creado: user='admin', pass='admin'")
        else:
            print("✅ Usuario Admin existente detectado.")
            
        # 3. Verificar Configuración
        config = SiteConfig.query.first()
        if not config:
            print("ℹ️  Configuración vacía. Inyectando valores por defecto...")
            db.session.add(SiteConfig(key="hero_title", value="Explora tu Consciencia Digital"))
            db.session.add(SiteConfig(key="hero_subtitle", value="Donde la tecnología y el espíritu convergen."))
            db.session.commit()
            print("✅ Configuración inicial inyectada.")
            
    print("\n✨ TODO LISTO. El sistema está preparado para el lanzamiento.")

if __name__ == "__main__":
    verify()
