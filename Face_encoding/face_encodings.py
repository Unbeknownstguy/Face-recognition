import face_recognition

# Loads the jpg files into numpy arrays
image = face_recognition.load_image_file("person.jpg")

# Generates the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    #prints only if No faces found in the image.
    print("No faces were found.")

else:
    # Grabing the first face encoding
    first_face_encoding = face_encodings[0]

    # Printing the results
    print(first_face_encoding)
