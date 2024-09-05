import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions,
)
from tensorflow.keras.preprocessing import image

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights="imagenet")


def classify_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)

    # Decode predictions
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Print the top three predictions
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

    # Display the image
    img = cv2.imread(
        "C:\coding projects\python\image classification\German-Shepherd-dog-Alsatian.webp"
    )  # Put the image path here
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
image_path = "C:\coding projects\python\image classification\German-Shepherd-dog-Alsatian.webp"  # Put the image path here
classify_image(image_path)
