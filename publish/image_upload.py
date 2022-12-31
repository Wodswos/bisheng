import os
import sys
import oss2
import json
from tqdm import tqdm

sys.path.append(os.path.abspath('./'))
from edit.batch_processing import replace_str_pair

def ali_oss( access_id, access_secret, endpoint, bucket_name, local_img_folder):
    auth = oss2.Auth(access_id, access_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    print('start to upload')
    for img_file_name in tqdm(os.listdir(local_img_folder)):
        bucket.put_object_from_file('img/'+ img_file_name, local_img_folder + '/' + img_file_name)
        # print('uploaded ' + img_file_name + '.')
    print('finished upload')

if __name__=='__main__':
    info = json.load(open(r'C:\Users\Five\Documents\projects\Pythons\bisheng\config.json'))
    oss_info = info['oss']
    ali_oss(oss_info['accessKeyID'], oss_info['accessKeySecret'], oss_info['endpoint'], oss_info['bucketName'], 'C:/Users/Five/Desktop/note/img')