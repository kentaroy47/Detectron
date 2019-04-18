# -*- coding: utf-8 -*-

import subprocess

for day in range(12, 20):
    for hour in range(30, 240, 10):
        com = "python tools/infer_dataset.py     --cfg configs/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_2x.yaml     --output-dir /tmp/detectron-visualizations     --image-ext jpg     --wts https://dl.fbaipublicfiles.com/detectron/35859745/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_2x.yaml.02_00_30.ESWbND2w/output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl --target "+str(day)+"-"+str(hour)+"-jackson /home/ken/jackson-long/VOCdevkit"+str(day)+"-"+str(hour)+"-jackson/VOC2007/JPEGImages"
        subprocess.call(com, shell=True)
