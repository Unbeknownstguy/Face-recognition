import PIL.Image
import PIL.ImageDraw
import face_recognition  #this is the library this gives the access to the face detection model and face land architecture model in dlib

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Loads the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

# Creating a PIL drawing object to be able to draw lines later
draw = PIL.ImageDraw.Draw(pil_image)

# Looping over each face
for face_landmarks in face_landmarks_list:

    # Looping over each facial feature (eye, nose, mouth, lips, etc)
    for name, list_of_points in face_landmarks.items():

        # Printing the location of each facial feature in this image.
        print("The {} in this face has the following points: {}".format(name, list_of_points))

        # tracing out each facial feature in the image with a line.
        draw.line(list_of_points, fill="red", width=2)

pil_image.show()
