import os
import parameter as params


font_dir = params.font_dir

font_fn_list = os.listdir(font_dir)

font_path_list = [os.path.join(font_dir, font_fn) for font_fn in font_fn_list]



#
# if __name__=='__main__':
#
#
#
#     print(font_path_list)

