import torch
import os
print("Cuda available: ", torch.cuda.is_available())
print("Device name:", torch.cuda.get_device_name())

from model import Model
model = Model(device = "cpu", dtype = torch.float16)

import os
prompt = "A horse galloping on a street"
params = {"t0": 44, "t1": 47 , "motion_field_strength_x" : 12, "motion_field_strength_y" : 12, "video_length": 8}

out_path, fps = f"./text2video_{prompt.replace(' ','_')}.mp4", 4
model.process_text2video(prompt, fps = fps, path = out_path, **params)