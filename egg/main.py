import cv2 as cv
import numpy as np

max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type:'
trackbar_value = 'Value'
window_name = 'Test'


def remove_background(img):
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # (1) Threshold
    th, threshed = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

    # (2) Find the min-area contour
    contours = cv.findContours(threshed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[-2]
    contours = sorted(contours, key=cv.contourArea)
    for contour in contours:
        if cv.contourArea(contour) > 100:
            break

    # (3) Create mask and do bitwise-op
    mask = np.zeros(img.shape[:2], np.uint8)
    cv.drawContours(mask, [contour], -1, 255, -1)
    return cv.bitwise_and(img, img, mask=mask)


def apply_changes(val):
    # 0: Binary
    # 1: Binary Inverted
    # 2: Threshold Truncated
    # 3: Threshold to Zero
    # 4: Threshold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    _, threshold = cv.threshold(gray_image, threshold_value, max_binary_value, threshold_type)
    contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    """
        for contour in contours:
        area = cv.contourArea(contour)
        print(area)
    """

    print("*********** RESULT ***********")
    areas = map(lambda contour: cv.contourArea(contour), contours)
    filtered = filter(lambda area: area >= 200, list(areas))
    filtered = list(filtered)

    clone = image.copy()
    cv.drawContours(clone, contours, -1, (0, 255, 0), 3)
    result = ""
    if len(filtered) > 1:
        result = "Fertile"
    elif len(filtered) == 1:
        result = "Infertile"
    else:
        print("Can't Identify")

    print(result)
    cv.putText(clone, result, (0, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
    cv.imshow(window_name, clone)


image_name = "input/infertile_a.png"

image = cv.imread(image_name)

image = cv.resize(image, (648, 480))

altered_image = remove_background(image)

gray_image = cv.cvtColor(altered_image, cv.COLOR_BGR2GRAY)

cv.namedWindow(window_name, cv.WINDOW_FULLSCREEN)
cv.imshow(window_name, image)
cv.createTrackbar(trackbar_type, window_name, 0, max_type, apply_changes)
cv.createTrackbar(trackbar_value, window_name, 127, max_value, apply_changes)

cv.waitKey()
cv.destroyAllWindows()
