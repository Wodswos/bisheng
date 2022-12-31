
import os
import sys
import yaml

# 野蛮的引入方式，至少 work
sys.path.append(os.path.abspath('./'))
from common.indexing import get_all_markdown_file
# print(sys.path)


def removing_dir(to_delete_path):
    if not os.path.exists(to_delete_path):
        print('要删除的目录 ' + to_delete_path + ' 不存在')
        return
    if os.path.isdir(to_delete_path):
        for item in os.listdir(to_delete_path):
            removing_dir(to_delete_path + '/' + item)
    else:
        os.remove(to_delete_path)
    print('目录 ' + to_delete_path + ' 已经删除')


def markdown_moving(source_root_path, dist_root_path):
    parent_dirs = []
    for markdown_file in get_all_markdown_file(source_root_path):
        parent_dir = ''
        for subdir in markdown_file.split('/')[:-1]:
            parent_dir = parent_dir + subdir + '/'
        parent_dir = parent_dir.rstrip('/')
        parent_dirs.append(parent_dir)
    
    for parent_dir in parent_dirs:
        dist_parent_dir = parent_dir.replace(source_root_path, dist_root_path)
        print(dist_parent_dir)
        if not os.path.exists(dist_parent_dir):
            print(dist_parent_dir + ' not exists, and createing it...')
            os.makedirs(dist_parent_dir)
    
    for markdown_file in get_all_markdown_file(source_root_path):
        print('copy ' + markdown_file + ' ' + markdown_file.replace(source_root_path, dist_root_path))
        os.system('copy ' + markdown_file.replace('/','\\') + ' ' + markdown_file.replace(source_root_path, dist_root_path).replace('/','\\'))


if __name__=='__main__':
    # 一些基本参数
    source_file_folder = 'C:/Users/Five/Desktop/note'
    github_folder = 'C:/Users/Five/Documents/Github'
    
    user_name = 'wodswos'
    repository_name = 'wodswos.github.io'
    repository_path = github_folder + '/' + repository_name

    # 一系列会用到的 git 命令，默认已配置 ssh
    git_clone_command = 'git clone git@github.com:' + user_name + '/' + repository_name
    git_add_command = 'git add --all'
    git_commit_command = "git commit -m debugging"
    git_push_command = 'git push git@github.com:'  + user_name + '/' + repository_name

    # 仓库已经存在则切换到目录，否则先 clone 仓库
    if not os.path.exists(repository_path):
        os.chdir(github_folder)
        os.system(git_clone_command)
    os.chdir(repository_path)

    # 清空除 .git 以外的文件夹，从零重新生成
    rebuild_flag = True
    for item in os.listdir(repository_path):
        if item != '.git' and rebuild_flag == True:
            print(item)
            removing_dir(repository_path + '/' + item)


    # 主逻辑
    if not os.path.exists(repository_path):
        os.mkdir(repository_path)
    pages_path = repository_path + '/src/pages'
    markdown_moving(source_file_folder, repository_path)


    # 提交，收尾
    os.system(git_add_command)
    print('Added to index.')
    os.system(git_commit_command)
    print('Committed to local repository.')
    os.system(git_push_command)
    print('Pushed to Github.')
