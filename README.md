# HSV Color Range Detector using OpenCV (Jetson Nano)

This Python script allows users to detect specific colors in a video stream using the HSV color space on the NVIDIA Jetson Nano platform. It provides a graphical user interface (GUI) with trackbars to adjust the lower and upper bounds of the hue, saturation, and value (HSV) components in real-time.

## Prerequisites

Before running the script on the NVIDIA Jetson Nano, ensure you have the following setup:

- NVIDIA Jetson Nano Developer Kit
- JetPack 4.6 installed (includes Ubuntu 18.04 LTS)
- Python 3.x
- OpenCV (`sudo apt-get install python3-opencv`)
- NumPy (`pip3 install numpy`)

## Usage

1. Clone the repository or download the script to your Jetson Nano.
2. Run the script using the command `python3 hsv_color_range_detector_jetson.py`.
3. Adjust the trackbars in the GUI window to set the desired HSV color range.
4. The script will display the original video stream, the mask showing the detected color, and the foreground extracted from the original frame.
5. Press 'q' to exit the script.

## Script Overview

- The script captures video from the webcam connected to the Jetson Nano or a video file and allows users to adjust HSV color range thresholds using trackbars.
- It creates a graphical user interface (GUI) window using OpenCV's `namedWindow` and `createTrackbar` functions to adjust HSV color range parameters.
- The script converts the captured frames from the BGR color space to the HSV color space using OpenCV's `cvtColor` function.
- It applies a series of morphological operations to the mask obtained from the specified HSV color range to refine and extract the foreground object.
- The script displays the original video stream, the mask showing the detected color, and the foreground extracted from the original frame in separate windows.
- Users can adjust the trackbars to refine the HSV color range detection in real-time.

## Acknowledgments

- This script utilizes the OpenCV library for image processing and GUI creation.
- Special thanks to NVIDIA for developing the Jetson Nano platform, which provides high-performance computing for edge AI applications.

## References

- [NVIDIA Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
- [JetPack](https://developer.nvidia.com/embedded/jetpack)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

Feel free to modify and extend this script according to your requirements! If you have any questions or suggestions, please feel free to reach out.
