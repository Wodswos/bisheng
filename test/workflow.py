import yaml
import os

# template_file_path='C:/Users/Five/Documents/projects/Pythons/bisheng/resouce/workflow_template/jekyll-gh-pages.yml'
# with open(template_file_path) as f:
#     # print(f.readlines())
#     data = yaml.load(f, yaml.FullLoader)
#     print(data)

repository_name = 'wodswos.github.io'
user_name = repository_name.split('.')[0]
git_clone_command = 'git clone git@github.com:' + user_name + '/' + repository_name


os.system('git --version')
os.chdir('C:/Users/Five/Desktop/')
# os.system(git_clone_command)