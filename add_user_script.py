from app import db
from app.models import UserProfile

user = UserProfile(first_name="Rajahni", last_name="Cunningham", username="rajah", password="uwiRaj")

db.session.add(user)
db.session.commit()
quit()