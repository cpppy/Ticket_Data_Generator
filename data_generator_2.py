

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import parameter as params
import font_cfg




if __name__=='__main__':

    font_path_list = font_cfg.font_path_list
    for idx, font_path in enumerate(font_path_list):
        b_img = Image.new("RGB", (800, 200), (0, 0, 0))
        text = '2019-05-27'

        draw = ImageDraw.Draw(b_img)
        char_pos = (0, 0)
        # font_path = './font_data/fangzheng_heiti_jianti.ttf'
        font_size = 100
        font_type = ImageFont.truetype(font_path, font_size)
        font_color = (255, 255, 255)
        draw.text(char_pos, str(text), font_color, font=font_type)
        font_type = ImageFont.truetype(font_path, 30)
        draw.text((0, 100), str(font_path), font_color, font=font_type)

        b_img.save('./gen_data/%d_test.jpg'%idx)






















