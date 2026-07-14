import cv2


def preprocess_image(image_path):

    # Read image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Apply thresholding
    threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]


    # Save processed image (optional)
    cv2.imwrite(
        "uploads/processed_image.png",
        threshold
    )


    return threshold