# YOLOv5 Object Detection

This project detects objects in a live camera feed using **YOLOv5**, **OpenCV**, and **PyTorch**. Bounding boxes and labels are drawn on detected objects in real-time.

---

## Features

* Real-time object detection from webcam
* Uses **YOLOv5s** pre-trained on the COCO dataset
* Draws bounding boxes and confidence labels on detected objects

---

## Requirements

* Python 3.12
* Git
* Webcam

---

## Installation & Setup

### Step 1: Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install main dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up YOLOv5

```bash
cd yolov5
pip install -r requirements.txt
cd ..
```

### Step 4: Run the object detection

```bash
python main.py
```

* The webcam feed will open in a window with detected objects highlighted.
* Press **`q`** to quit and close the window.

---

## Notes

* Ensure your webcam is properly connected and accessible.
* YOLOv5 will automatically download pre-trained weights on first run.
* For external cameras, change `cap = cv2.VideoCapture(0)` to the correct device index.

---

## Credits

* Code developed by **Jishnu Setia**
* Built using **YOLOv5**, **OpenCV**, and **PyTorch**

---

## License

No License. All rights reserved.
