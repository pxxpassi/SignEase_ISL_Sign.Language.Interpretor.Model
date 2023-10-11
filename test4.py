import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the camera
cap = cv2.VideoCapture(0)

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combine with the model filename
model_path = os.path.join(script_dir, 'model.h5')

# Load the model
model = tf.keras.models.load_model(model_path)

# Define a mapping of class labels to sign language words
class_to_word = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F"
    # Add more mappings as needed
}

# Load the Kaggle dataset outside the loop
dataset_path = "C:/Users/Purvi/Documents/SLI Files/dataset/data"


def load_kaggle_dataset():
    data = []
    labels = []

    for class_label in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_label)
        for filename in os.listdir(class_path):
            img_path = os.path.join(class_path, filename)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB format
            img = cv2.resize(img, (50, 50))  # Resize to match your model's input size
            img = img / 255.0  # Normalize pixel values (if your model requires it)
            data.append(img)
            labels.append(class_label)

    return np.array(data), np.array(labels)

# Load Kaggle dataset
kaggle_data, kaggle_labels = load_kaggle_dataset()

while True:
    ret, frame = cap.read()

    # Convert the frame to RGB format for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands using MediaPipe Hands
    results = hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Extract hand landmarks
            hand_landmarks = np.array([(lm.x, lm.y) for lm in landmarks.landmark]).flatten()

            # Resize landmarks to match the input size of your model
            input_data = cv2.resize(hand_landmarks, ((50,50)))

            # Normalize input data if necessary
            input_data = input_data / 255.0

            # Perform inference using your sign language translation model
            prediction = model.predict(np.expand_dims(input_data, axis=0))

            # Get the index of the class with the highest probability
            predicted_class = np.argmax(prediction)

            # Translate the predicted class to the corresponding sign language word
            sign_language_word = class_to_word.get(predicted_class, class_to_word[0])

            # Overlay the sign language word on the frame
            cv2.putText(frame, sign_language_word, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Sign Language Translation', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
