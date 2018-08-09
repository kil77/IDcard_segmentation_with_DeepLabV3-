import numpy as np
import os
OUT_PUT_PATH = '/home/gq/PycharmProjects/deeplabV3+/IDImage/list'
IMG_PATH = '/home/gq/PycharmProjects/deeplabV3+/IDImage/JPGImage'
LABEL_PATH = '/home/gq/PycharmProjects/deeplabV3+/IDImage/Label'
def split():
    img_path = os.listdir(IMG_PATH)
    train_filename = os.path.join(OUT_PUT_PATH,'train.txt')
    val_filename = os.path.join(OUT_PUT_PATH,'val.txt')
    for item in img_path:
        item_id = item.split('.')[0]
        n = np.random.randint(0,10)
        if n < 8:
            if not os.path.exists(train_filename):
                os.system(r'touch %s' % train_filename)
            with open(train_filename,'a+') as train:
                train.write(item_id + '\n')
        else:
            if not os.path.exists(val_filename):
                os.system(r'touch %s' % val_filename)
            with open(val_filename,'a+') as val:
                val.write(item_id + '\n')
    # img_path = os.listdir(IMG_PATH)
    # label_path = os.listdir(LABEL_PATH)
    # img_id = [item.split('.')[0] for item in img_path]
    # label_id = [item.split('.')[0] for item in label_path]
    # for item in label_id:
    #     if item not in img_id:
    #         print(item)



if __name__ == '__main__':
    split()