


import sqlite3
from app import create_app, db
from app.models import User, Post, Project, About

# --- Crear app context para MySQL ---
app = create_app()

with app.app_context():

    # --- Conectar a SQLite ---
    sqlite_conn = sqlite3.connect("ilaria_db_backup.db")
    sqlite_conn.row_factory = sqlite3.Row
    sqlite_cursor = sqlite_conn.cursor()

    print("🚀 Migrando datos...")

    # =========================
    # USERS
    # =========================
    sqlite_cursor.execute("SELECT * FROM user")
    users = sqlite_cursor.fetchall()

    for u in users:
        user = User(
            id=u["id"],
            username=u["username"],
            password=u["password"],
            role=u["role"]
        )
        db.session.add(user)

    print(f"✅ Users: {len(users)}")

    # =========================
    # POSTS
    # =========================
    sqlite_cursor.execute("SELECT * FROM post")
    posts = sqlite_cursor.fetchall()

    for p in posts:
        post = Post(
            id=p["id"],
            title=p["title"],
            description=p["description"],
            image=p["image"]
        )
        db.session.add(post)

    print(f"✅ Posts: {len(posts)}")

    # =========================
    # PORTFOLIO
    # =========================
    sqlite_cursor.execute("SELECT * FROM project")
    projects = sqlite_cursor.fetchall()

    for p in projects:
        project = Project(
            id=p["id"],
            title=p["title"],
            description=p["description"],
            image=p["image"]
        )
        db.session.add(project)

    print(f"✅ Portfolio: {len(projects)}")

    # =========================
    # ABOUT
    # =========================
    sqlite_cursor.execute("SELECT * FROM about")
    abouts = sqlite_cursor.fetchall()

    for a in abouts:
        about = About(
            id=a["id"],
            content=a["content"]
        )
        db.session.add(about)

    print(f"✅ About: {len(abouts)}")

    # Guardar en MySQL
    db.session.commit()

    print("🎉 MIGRACIÓN COMPLETADA CON ÉXITO")
