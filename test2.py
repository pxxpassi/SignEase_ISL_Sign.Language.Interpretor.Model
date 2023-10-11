import cv2
import numpy as np
import tensorflow as tf
model = tf.keras.applications.MobileNetV2(weights='imagenet')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    
    # Resize the frame to the input size expected by the model (e.g., 224x224)
    resized_frame = cv2.resize(frame, (224, 224))
    
    # Preprocess the frame for inference
    input_data = tf.keras.applications.mobilenet_v2.preprocess_input(resized_frame)
    
    # Expand dimensions to match the input shape (1, 224, 224, 3)
    input_data = np.expand_dims(input_data, axis=0)
    
    # Perform inference using the pre-trained model
    predictions = model.predict(input_data)
    
    # Decode the predictions and get the top-1 class index
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)
    top_prediction = decoded_predictions[0][0]
    
    # Display the top prediction label and confidence score on the frame
    label = f"{top_prediction[1]} ({top_prediction[2]*100:.2f}%)"
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Show the frame with the prediction
    cv2.imshow('Hand Gesture Detection', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
