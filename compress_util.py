import os
import parameter as params
import tarfile


def compress_dir_to_tarfile(dir_path, tarfile_path):
    # cwd = os.getcwd()
    tar = tarfile.open(tarfile_path, 'w:gz')

    for root, dir, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            save_tag = file_path.replace('/data/data/', '')
            tar.add(file_path, arcname=save_tag)
    tar.close()

def compress_crnn_train_data():
    dir_path = params.train_data_dir

    tarfile_path = params.tarfile_path

    compress_dir_to_tarfile(dir_path, tarfile_path)
