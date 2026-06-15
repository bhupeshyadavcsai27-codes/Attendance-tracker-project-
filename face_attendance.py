import face_recognition
import cv2
import os

known_faces = []
known_names = []

path = "faces"

for file in os.listdir(path):

    image = face_recognition.load_image_file(
        f"{path}/{file}"
    )

    encoding = face_recognition.face_encodings(image)[0]

    known_faces.append(encoding)

    known_names.append(
        os.path.splitext(file)[0]
    )

print("Faces Loaded Successfully")