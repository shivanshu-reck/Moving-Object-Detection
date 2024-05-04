# Moving-Object-Detection
This Python script is designed to detect moving objects in a video feed and play different sounds based on whether an object is moving or not. It uses the OpenCV library for image processing and the pygame library for sound playback.

The script begins by importing the necessary libraries: cv2 for computer vision tasks, time for time-related functions, imutils for image utility functions, and pygame for playing sounds.

The pygame.mixer.init() function is called to initialize the pygame mixer module, which is used for sound playback. Two sound files are then loaded using pygame.mixer.Sound(). These sounds are played when an object is detected moving and when no movement is detected, respectively.

The script then initializes a video capture object cam using cv2.VideoCapture(0). The argument 0 indicates that the video feed comes from the default webcam. A time.sleep(1) call is made to allow the camera to warm up.

The firstFrame variable is initialized to None. This variable will later hold the first frame of the video feed, which will be used as a reference for detecting movement. The area variable is set to 2000, which will be used to filter out small contours that are not of interest.

The script then enters an infinite loop where it continuously reads frames from the video feed, processes them, and checks for movement. Each frame is converted to grayscale and blurred using a Gaussian filter to reduce high frequency noise. The absolute difference between the current frame and the first frame is computed, and a binary threshold is applied to the difference image to create a binary image where white pixels represent areas of the frame that have changed.

The cv2.findContours() function is then used to find contours in the binary image. Each contour is a continuous curve that forms the boundary of an object in the image. The script then iterates over each contour. If the area of a contour is less than the area threshold, it is ignored. Otherwise, a rectangle is drawn around the contour, the text "Moving Object detected" is set, and the moving object sound is played.

If no moving object is detected in a frame, the text "Normal" is set and the normal sound is played. The text is then printed to the console and displayed on the frame, which is shown in a window named "cameraFeed".

The script waits for a key press after displaying each frame. If the 'q' key is pressed, the script breaks out of the loop, releases the video capture object, and closes all OpenCV windows.
