import os
import shutil

ROOT_PATH = "my_data"
Ann_PATH = "Annotations"
Set_PATH = "ImageSets/Main"
Jpg_PATH = "JPEGImages"

if os.path.exists(ROOT_PATH):
    shutil.rmtree(ROOT_PATH)

os.mkdir(ROOT_PATH)

os.chdir(ROOT_PATH)
if not os.path.exists(Ann_PATH):
    os.mkdir(Ann_PATH)
if not os.path.exists(Set_PATH):
    os.makedirs(Set_PATH)
if not os.path.exists(Jpg_PATH):
    os.mkdir(Jpg_PATH)
os.chdir("..")

def get_class(class_name, ann_dir, jpg_dir, output_dir=None):
    class_item = list()
    for i in os.listdir(ann_dir):
        # print ann_file
        ann_name = i
        ann_file = os.path.join(ann_dir, i)
        name = i.split(".")[0]
        jpg_name = name + ".JPEG"
        jpg_file = os.path.join(jpg_dir, jpg_name)
        if os.path.exists(jpg_file):
            class_item.append(name)
            ann_new = os.path.join(ROOT_PATH, Ann_PATH, ann_name)
            jpg_new = os.path.join(ROOT_PATH, Jpg_PATH, jpg_name)
            ann_old = os.path.join(ann_dir, ann_name)
            jpg_old = os.path.join(jpg_dir, jpg_name)
            shutil.copy(ann_old, ann_new)
            shutil.copy(jpg_old, jpg_new)

    train_size = int(len(class_item)*0.7)
    train = class_item[0: train_size]
    test_size = int(len(class_item)*0.2)
    test = class_item[train_size: train_size+test_size]
    val = class_item[train_size+test_size: len(class_item)]
    return train, test, val

# get_class("ha", "/home/ocean/lab/Faster-RCNN_TF/get_my_data/Ann/n02876657", "/home/ocean/lab/Faster-RCNN_TF/get_my_data/ImageSet/n02876657")
train = list()
test = list()
val = list()
for i in os.listdir("Ann"):
    train_t, test_t, val_t = get_class(i, os.path.join("Ann", i), os.path.join("ImageSet", i))
    train.extend(train_t)
    test.extend(test_t)
    val.extend(val_t)

train_txt = os.path.join(ROOT_PATH, Set_PATH, "train.txt")
with open(train_txt, "wb") as f:
    for i in train:
        f.write(i+'\n')
test_txt = os.path.join(ROOT_PATH, Set_PATH, "test.txt")
with open(test_txt, "wb") as f:
    for i in test:
        f.write(i+'\n')
val_txt = os.path.join(ROOT_PATH, Set_PATH, "val.txt")
with open(val_txt, "wb") as f:
    for i in test:
        f.write(i+'\n')


