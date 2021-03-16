# qtbooth

A photobooth-like application built with qt and python

## TODO

* Figure out how to have modules `opencv-python-headless` and `opencv-python` coexist because having `opencv-python-headless` will break other programs
* add a way to safely switch filters for webcam inputs
* add a way to safely switch webcam inputs
* move image_filter into its own package and create an `Image` class with a `filter` and a `buffer` and conversion methods
* add to / fix image_filter so it works with more conversions (this has caused an issue with RGBA images)
