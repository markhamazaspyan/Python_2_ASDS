import cv2
# Problem 4.
# Rescale the video vid1.jpg by 0.5 and display the original video and the rescaled one in separate windows.


def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


capture = cv2.VideoCapture('vid1.mp4')

while True:
    frame_loaded, frame = capture.read()

    if frame is not None:  # or if isTrue
        frame_rescaled = rescaleFrame(frame, 0.5)
        cv2.imshow('Video', frame)
        cv2.imshow('Video_rescaled', frame_rescaled)
    else:
        print('empty frame')
        exit(1)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
cv2.waitKey(0)