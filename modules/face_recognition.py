import face_recognition
import cv2

def capture_face():
    """Capture a face from the webcam and return its encoding."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Capture Face", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) == 1:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                break
    cap.release()
    cv2.destroyAllWindows()
    return face_encoding

def compare_faces(face_encoding, stored_encoding):
    """Compare two face encodings."""
    return face_recognition.compare_faces([stored_encoding], face_encoding, tolerance=0.5)[0]