import os
import sys

sys.path.append(os.path.abspath('./'))
from common.indexing import get_all_markdown_file
from publish.JekllPagesWorkflow import markdown_moving
# print(sys.path)

def replace_str_pair(root_path, key, value):
    for file_path in get_all_markdown_file(root_path=root_path):
        with open(file_path, encoding='utf8') as f:
            text = f.read()
        text = text.replace(key, value)
        with open(file_path, 'w', encoding='utf8') as f:
            f.write(text)



if __name__=='__main__':
    # os.mkdir('C:/Users/Five/Desktop/note_test')
    # markdown_moving('C:/Users/Five/Desktop/note','C:/Users/Five/Desktop/note_test')
    # replace_str_pair('C:/Users/Five/Desktop/note_test','C:/Users/Five/Desktop/note/img/', 'https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/')
    # replace_str_pair('C:/Users/Five/Desktop/note_test','C:\\Users\\Five\\Desktop\\note\\img\\', 'https://zehua-markdown.oss-cn-shanghai.aliyuncs.com/img/')
    
    pass
