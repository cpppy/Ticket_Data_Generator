import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import parameter as params
import font_cfg
import random
from effects import data_process
import compress_util
import tqdm
import json
import data_split_util


def gen_digit_list(sample_num):
    num_dict = range(0, 10)
    digit_list = random.choices(num_dict, k=sample_num)
    digit_list = [str(elem) for elem in digit_list]
    return digit_list


def get_random_font_color():
    gray_val = random.randint(30, 90)
    return tuple([gray_val] * 3)


def get_random_pos(bg_im_w, bg_im_h, t_width, t_height):
    dx_left, dx_right, dy_top, dy_bottom = 0, 0, 0, 0
    # calc text pos
    lt_pos = [random.randint(dx_left, bg_im_w - t_width - dx_right),
              random.randint(dy_top, bg_im_h - t_height - dy_bottom)]
    # calc crop coordinates
    x0 = lt_pos[0] - dx_left
    y0 = lt_pos[1] - dy_top
    x2 = lt_pos[0] + t_width + dx_right
    y2 = lt_pos[1] + t_height + dy_bottom
    crop_coords = [x0, y0, x2, y2]
    return lt_pos, crop_coords


def gen_one_date_sample(text, font_path):
    b_img = Image.new("RGB", (100, 30), (255, 255, 255))
    draw = ImageDraw.Draw(b_img)
    # text = '2019-05-27'
    font_size = 20
    font_type = ImageFont.truetype(font_path, font_size)
    text_w, text_h = draw.textsize(str(text), font=font_type)
    # print('text, w/h', text_w, text_h)
    # b_w = text_w + random.randint(0, 30)
    # b_h = text_h + random.randint(0, 30)
    b_w = b_h = max(text_w, text_h) + random.randint(0, 30)
    b_img = Image.new("RGB", (b_w, b_h), (255, 255, 255))
    draw = ImageDraw.Draw(b_img)

    lt_pos, crop_coords = get_random_pos(bg_im_w=b_w,
                                         bg_im_h=b_h,
                                         t_width=text_w,
                                         t_height=text_h)

    char_pos = lt_pos
    # font_color = (0, 0, 0)
    font_color = get_random_font_color()
    draw.text(char_pos, str(text), font_color, font=font_type)

    # pil ---> cv2
    res_img = cv2.cvtColor(np.asarray(b_img, np.uint8), cv2.COLOR_RGB2BGR)
    # res_img = cv2.resize(res_img, (150, 50))

    # res_img = cv2.resize(res_img, (150, 50))
    # res_img = cv2.resize(res_img, (300, 100))

    # res_img = cv2.resize(res_img, (300, 900))

    shrink_ratio = 3
    res_img = cv2.resize(res_img, (int(b_w * shrink_ratio), int(b_h * shrink_ratio)))

    process_switch = random.choice(['erode', 'dilate', 'open', 'close'])
    if process_switch is 'erode':
        res_img = data_process.erode_process(res_img, ksize=(3, 3))
    elif process_switch is 'dilate':
        res_img = data_process.dilate_process(res_img, ksize=(3, 3))
    elif process_switch is 'open':
        res_img = data_process.erode_process(res_img, ksize=(3, 3))
        res_img = data_process.dilate_process(res_img, ksize=(3, 3))
    elif process_switch is 'close':
        res_img = data_process.dilate_process(res_img, ksize=(3, 3))
        res_img = data_process.erode_process(res_img, ksize=(3, 3))
    else:
        pass
    res_img = cv2.resize(res_img, (b_w, b_h))
    # res_img = cv2.resize(res_img, (3 * b_w, 3 * b_h))
    # res_img = data_process.erode_process(res_img, ksize=(3, 3))

    ret, res_img = cv2.threshold(src=cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY),
                                 thresh=200,
                                 maxval=255,
                                 type=cv2.THRESH_BINARY)
    return res_img


if __name__ == '__main__':

    params.sample_num = 1000
    params.train_data_dir = '/data/data/mnist_train_data'
    params.tarfile_path = tarfile_path = '/data/data/ticket_train_data_1k_ticket_id_special_num_20190327_init.tar'
    params.train_img_dir = os.path.join(params.train_data_dir, 'images')
    params.train_label_dir = os.path.join(params.train_data_dir, 'labels')

    # init directory
    if not os.path.exists(params.train_data_dir):
        os.mkdir(params.train_data_dir)
    if not os.path.exists(params.train_img_dir):
        os.mkdir(params.train_img_dir)
    if not os.path.exists(params.train_label_dir):
        os.mkdir(params.train_label_dir)

    sample_num = params.sample_num
    date_list = gen_digit_list(sample_num)
    font_path_list = font_cfg.font_path_list
    # save_dir = './gen_data/expire_date'
    save_dir = params.train_img_dir

    label_dict = {}
    pbar = tqdm.tqdm(total=sample_num, desc='process_status')
    for idx, text in enumerate(date_list):
        font_path = random.choice(font_path_list)
        res_img = gen_one_date_sample(text, font_path)
        img_fn = '%d.jpg' % idx
        img_save_path = os.path.join(save_dir, '%d.jpg' % idx)
        cv2.imwrite(img_save_path, res_img)
        label_dict[img_fn] = text
        # print(img_fn, font_path)

        pbar.update(1)
    pbar.close()
    label_path = os.path.join(params.train_label_dir, 'label.json')
    with open(label_path, 'w', encoding='utf-8') as f:
        json.dump(label_dict, f, ensure_ascii=False)
    # split
    data_split_util.random_get_val(os.path.join(params.train_label_dir, 'label.json'),
                                   os.path.join(params.train_label_dir, 'train.json'),
                                   os.path.join(params.train_label_dir, 'val.json'),
                                   0.1)

    compress_util.compress_crnn_train_data()
