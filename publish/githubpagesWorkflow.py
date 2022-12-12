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


def generate_configuration(dist_folder):
    configuration_file = dist_folder + '/_config.yml'
    configuration = {
    }
    configuration['title'] = 'Five Zehua\'s homepage'
    configuration['description'] = 'Stay Foolish, Stay Hungry'

    with open(configuration_file, 'w') as f:
        f.write(yaml.dump(configuration, default_flow_style=False))


def generate_action_workflow(dist_repository, workflow_name='suibianxie', template_file_path=None):
    if template_file_path:
        with open(template_file_path) as f:
            workflow_configuration = yaml.load(f, yaml.FullLoader)
    else:
        workflow_configuration = {}
        # workflow_configuration['name'] = 'suibian xiexie la'
        # workflow_configuration['on'] = {}
        # workflow_configuration['on']['push'] = {}
        # workflow_configuration['on']['push']['branch'] = ["main"]
        # workflow_configuration['on']['workflow_dispatch']
        # workflow_configuration['permission'] = {
        #     'content':'read',
        #     'pages':'write',
        #     'id-tokent':'write'
        # }

        # workflow_configuration['jobs'] = {}
        # workflow_configuration['jobs']['build'] = {}
        # workflow_configuration['jobs']['deploy'] = {}
            
    # 因为python会把yaml里的 on 读取为 True，故在此修复
    workflow_configuration['on'] = workflow_configuration[True]
    workflow_configuration.pop(True)

    # list directory
    workflow_configuration['jobs']['build']['steps'].insert(1, {'name':'list directory', 'run':'ls -lR'})



    # 写入 configuration yaml
    if not os.path.exists(dist_repository + '/.github/workflows'):
        os.makedirs(dist_repository + '/.github/workflows')
    workflow_file = dist_repository + '/.github/workflows/' + workflow_name + '.yml'
    with open(workflow_file, 'w') as f:
        f.write(yaml.dump(workflow_configuration, default_flow_style=False))



# set_action_workflow('C:/Users/Five/Desktop/test')


if __name__=='__main__':
    # 一些基本参数
    source_file_folder = 'C:/Users/Five/Desktop/note'
    dist_root_path = 'C:/Users/Five/Documents/Github'
    
    repository_name = 'wodswos.github.io'
    repository_path = dist_root_path + '/' +repository_name
    user_name = repository_name.split('.')[0]
    
    # 一系列会用到的 git 命令，默认已配置 ssh
    git_clone_command = 'git clone git@github.com:' + user_name + '/' + repository_name
    git_add_command = 'git add --all'
    git_commit_command = "git commit -m 'update'"
    git_push_command = 'git push git@github.com:'  + user_name + '/' + repository_name

    # 仓库已经存在则切换到目录，否则先 clone 仓库
    if not os.path.exists(repository_path):
        os.chdir(dist_root_path)
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
    markdown_moving(source_file_folder, repository_path)

    generate_configuration(repository_path)
    generate_action_workflow(
        repository_path, 
        workflow_name='my_workflow', 
        template_file_path='C:/Users/Five/Documents/projects/Pythons/bisheng/resouce/workflow_template/jekyll-gh-pages.yml'
    )

    # 提交，收尾
    os.system(git_add_command)
    print('Added to index .')
    os.system(git_commit_command)
    print('Committed to local repository')
    os.system(git_push_command)
    print('Pushed to Github')



