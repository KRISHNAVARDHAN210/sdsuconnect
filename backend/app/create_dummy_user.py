from app.core.database import SessionLocal
from app.models.user import User

db = SessionLocal()

# Create a dummy user
dummy_user = User(
    username="admin",
    password="admin123"
)

db.add(dummy_user)
db.commit()
db.close()

print("Dummy user created successfully!")
