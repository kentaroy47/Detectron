# -*- coding: utf-8 -*-

import subprocess
import argparse
import time
parser = argparse.ArgumentParser(description='Train a Fast R-CNN network')
parser.add_argument('--data', dest='data',
                      default=200)
args = parser.parse_args()

com = "conda run -n detectron python /home/ken/Detectron/tools/infer_dataset.py --cfg configs/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_2x.yaml     --output-dir /tmp/detectron-visualizations     --image-ext jpg     --wts https://dl.fbaipublicfiles.com/detectron/35859745/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_2x.yaml.02_00_30.ESWbND2w/output/train/coco_2014_train%3Acoco_2014_valminusminival/generalized_rcnn/model_final.pkl --target jackson "+args.data
subprocess.call(com, shell=True)
