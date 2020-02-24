import cv2

#creates function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # makes image clearer by using gaussian blur to reduce noise and reduce detail
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # uses canny to detect the edges of the image
    edges = cv2.Canny(img_gray_blur, 10, 70)

    #  inverts binarize the image
    ret, mask = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask
#captures video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Frame', sketch(frame))
    if cv2.waitkey == ord('q') or cv2.waitkey == ord('Q'):
        break
#once loop breaks the windows will be destroyed
cap.release()
cv2.destroyAllWindows()