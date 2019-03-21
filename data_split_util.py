
import json
import random

import os

def random_get_val(json_label_path,
                   json_train_path,
                   json_val_path,
                   validation_split_ratio):
    with open(json_label_path, 'r', encoding='utf-8') as f:
        image_label = json.load(f)
        image_fn_list = [i for i, j in image_label.items()]
        nums = len(image_fn_list)
        val_size = int(nums * validation_split_ratio)
        choosed_idx_arr = random.sample(range(0, nums), val_size)
        val_dic = {}
        for idx in choosed_idx_arr:
            image_name = image_fn_list[idx]
            val_dic[image_name] = image_label[image_name]
            image_label.pop(image_name)
        train_length = len(image_label)  # remain samples
        val_length = len(val_dic)  # selected samples
        json_val_file = open(json_val_path, 'w', encoding='utf-8')
        json.dump(val_dic, json_val_file, ensure_ascii=False)
        json_val_file.close()
        json_train_file = open(json_train_path, 'w', encoding='utf-8')
        json.dump(image_label, json_train_file, ensure_ascii=False)
        json_train_file.close()

#
# def combine_label_dict(meta_json_dir=cfg.label_output_dir):
#     meta_json_files = os.listdir(meta_json_dir)
#     total_labels = {}
#     for meta_json_file in meta_json_files:
#         if 'meta_' in meta_json_file:
#             with open(os.path.join(meta_json_dir, meta_json_file), 'r', encoding='utf-8') as meta_f:
#                 image_label = json.load(meta_f)
#                 total_labels = dict(total_labels, **image_label)
#     json_file = open(cfg.json_label_path, 'w', encoding='utf-8')
#     json.dump(total_labels, json_file, ensure_ascii=False)
#     json_file.close()
#
# if __name__=='__main__':
#
#
#     # init directory of train_data
#     if not os.path.exists('/data/data/crnn_train_data'):
#         os.mkdir('/data/data/crnn_train_data')
#     if not os.path.exists('/data/data/crnn_train_data/json'):
#         os.mkdir('/data/data/crnn_train_data/json')
#     if not os.path.exists('/data/data/crnn_train_data/key'):
#         os.mkdir('/data/data/crnn_train_data/key')
#     if not os.path.exists('/data/data/crnn_train_data/cut_images'):
#         os.mkdir('/data/data/crnn_train_data/cut_images')
#     if not os.path.exists('/data/output'):
#         os.mkdir('/data/output')
#     if not os.path.exists('/data/output/CRNN_draft'):
#         os.mkdir('/data/output/CRNN_draft')
#
#
#
#
#     num_img_generator.batch_generating()
#
#
#
#     # ramdom select part of labels as validation dataset
#     random_get_val(json_label_path=cfg.json_label_path,
#                    json_train_path=cfg.json_train_path,
#                    json_val_path=cfg.json_val_path,
#                    validation_split_ratio=cfg.validation_split_ratio)