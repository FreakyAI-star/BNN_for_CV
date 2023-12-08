import os
import numpy as np
cls = []
for i in os.listdir("/workspace/pytorch-video-recognition/UCF101"):
  cls.append(i.split('_')[1])
all_classes = np.unique(np.array(cls))
for i in all_classes:
  os.system('mkdir /workspace/pytorch-video-recognition/UCF-101/' + i)
for i in os.listdir("/workspace/pytorch-video-recognition/UCF101"):
  if i.split('_')[1] in all_classes:
    os.system('cp -r /workspace/pytorch-video-recognition/UCF101/' + i + ' /workspace/pytorch-video-recognition/UCF-101/' + i.split('_')[1])
