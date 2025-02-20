# register.py
from modules.database import insert_user
from modules.face_recognition import capture_face

def register_user():
    """Register a new user by capturing their face and storing it in the database."""
    name = input("Enter your name: ")
    face_encoding = capture_face()
    insert_user(name, face_encoding)
    print(f"User {name} registered successfully!")

if __name__ == "__main__":
    register_user()