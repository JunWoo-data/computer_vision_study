# %%
from roboflow import Roboflow

# %%
#### Download the data for the tennis ball detection 
rf = Roboflow(api_key="K9cmvoVzGOwhrE8eNiVI")
project = rf.workspace("viren-dhanwani").project("tennis-ball-detection")
version = project.version(6)
dataset = version.download("yolov5")

# %%
