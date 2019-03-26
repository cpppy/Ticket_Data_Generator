import os

sample_num = 1000

tarfile_path = '/data/data/ticket_train_data_1k_bank_id_20190326_init.tar'


font_dir = './font_data'


train_data_dir = '/data/data/ticket_train_data'
train_img_dir = os.path.join(train_data_dir, 'images')
train_label_dir = os.path.join(train_data_dir, 'labels')

# init directory
if not os.path.exists(train_data_dir):
    os.mkdir(train_data_dir)
if not os.path.exists(train_img_dir):
    os.mkdir(train_img_dir)
if not os.path.exists(train_label_dir):
    os.mkdir(train_label_dir)





