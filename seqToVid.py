import argparse
import os
import cv2
import numpy as np

parser = argparse.ArgumentParser(description = 'Converting seq/s of images to video/s')
parser.add_argument('-s', '--source', metavar=" ", required=True, help='source of the sequence')
parser.add_argument('-o', '--output', metavar=" ",default='output_videos', help='output directory')
parser.add_argument('-f', '--format', metavar=" ", default='png', help= 'image format')
parser.add_argument('-m', '--multiple', action="store_true", help ='multiple sequence to convert')
args = parser.parse_args()

def seq_to_vid(path):
    names = [os.path.join(path, x) for x in os.listdir(path) if x[-3:] == args.format]
    names.sort()
    if len(names)==0:
        return
    img = cv2.imread(names[0])

    (height,width,depth) = img.shape
    size = (width,height)
    path_holder = path.split('/')
    if args.multiple:
        path_holder = path.split("\\")
        path_holder = path.split('/')
    print(path_holder[-1])
    out = cv2.VideoWriter(os.path.join(args.output, path_holder[-1]+'.avi'),cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for name in names:
        out.write(cv2.imread(name))

    out.release()

if not os.path.exists(args.output):
    os.mkdir(args.output)
if args.multiple:
    dir_names = [os.path.join(args.source,x) for x in os.listdir(args.source)]
    for dir_name in dir_names:
        if os.path.isdir(dir_name):
            seq_to_vid(dir_name)

else:
    seq_to_vid(args.source)