import cv2
# Problem 2.
# Open the video vid1.mp4 and display it frame by frame in a window named vid1.

vid1 = cv2.VideoCapture('vid1.mp4')

while True:
    frame_loaded, frame = vid1.read()


    if frame_loaded:
        cv2.imshow('vid1', frame)
    else:
        print('empty frame')
        exit(1)


    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

vid1.release()
cv2.destroyAllWindows()  # distroying all windows since we don't need them anymore
cv2.waitKey(0)
