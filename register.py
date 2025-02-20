# register.py
from modules.database import insert_user
from modules.face_recognition import capture_face

def register_user(name):
    """Register a new user by capturing their face and storing it in the database."""
    face_encoding = capture_face()
    insert_user(name, face_encoding)
    print(f"User {name} registered successfully!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    register_user(name)