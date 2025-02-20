# login.py
from modules.database import get_all_users
from modules.face_recognition import capture_face, compare_faces
import numpy as np

def login():
    """Authenticate a user by comparing their face with stored encodings."""
    face_encoding = capture_face()
    users = get_all_users()
    for user in users:
        stored_encoding = np.frombuffer(user[1], dtype=np.float64)
        if compare_faces(face_encoding, stored_encoding):
            print(f"Welcome back, {user[0]}!")
            return
    print("User not recognized. Please register first.")

if __name__ == "__main__":
    login()