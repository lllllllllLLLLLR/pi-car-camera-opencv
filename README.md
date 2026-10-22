# Pi Car Camera — OpenCV MJPEG Stream

A project that opens an MJPEG video stream from a Raspberry Pi–powered robot car camera and displays the live frame feed with OpenCV.

## Highlights
- Connects to a Raspberry Pi MJPEG stream (`http://<pi-ip>:8080/?action=stream`) via OpenCV `VideoCapture`.
- Continuously reads frames and shows them in a desktop window; press `q` to quit.
- Serves as a minimal skeleton for plugging in downstream image processing (lane detection, object tracking, etc.).

## Quick start
1. Install dependencies: `pip install -r requirements.txt`
2. On the Raspberry Pi, start the MJPEG stream server (e.g. `motion` or `raspivid` + `mjpg-streamer`) on port `8080`.
3. Edit `python控制小车摄像头.py` and replace `<raspberry-pi-ip>` with the Pi's actual IP address.
4. Run: `python python控制小车摄像头.py`

## Layout
```
.
├── python控制小车摄像头.py   # main stream-reading script
├── 小车摄像头.ipynb           # empty notebook stub (notebook-based exploration, unused)
├── requirements.txt
└── README.md
``` 
