import cv2


def preprocess_image(image_path):

    # Load image
    original_image = cv2.imread(image_path)

    # Convert image to grayscale
    grayscale_image = cv2.cvtColor(
        original_image,
        cv2.COLOR_BGR2GRAY
    )

    # Apply Otsu Thresholding
    binary_image = cv2.threshold(
        grayscale_image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # Save processed image
    cv2.imwrite(
        "uploads/processed_image.png",
        binary_image
    )

    return binary_image