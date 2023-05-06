import os
from shutil import move
from tqdm import tqdm
from translators.server import *

root = "./txt"
files = os.listdir(root)
for file in tqdm(files):
    try:
        src = open(os.path.join(root, file), 'r').readlines()[0]
        # dst = youdao(src)
        # dst = baidu(src)
        # dst = google(src)
        # dst = qqFanyi(src)
        # dst = sougou(src)
        # dst = alibaba(src)
        f = open("./res/" + file, 'w')
        f.write(src)
        f.write(dst + '\n')
        f.close()
    except:
        move(os.path.join(root, file), "./error/")
