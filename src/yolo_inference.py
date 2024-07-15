# %%
from ultralytics import YOLO

# %%
model = YOLO("yolov8x")

# %%
model.predict("../data/input_image.png", save = True)

# %%
model.predict("../data/input_video.mp4", save = True)


# %%
