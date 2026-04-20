


from sqlalchemy import text
from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    try:
        # Con SQLAlchemy 2.x hay que usar text()
        with db.engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("Conexión MySQL OK:", result.fetchone())
    except Exception as e:
        print("❌ Error al conectar con MySQL:", e)
