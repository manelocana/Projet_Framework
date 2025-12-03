

from app import create_app
from app.extensions import db
from app.models.post import Post


app = create_app()


with app.app_context():
    new_post = Post(title='post test', content='test conexion db')
    db.session.add(new_post)
    db.session.commit()

    print('post created ok')



posts = Post.query.all()
for p in posts:
    print(p.id, p.title, p.content)