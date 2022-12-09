import os


def get_all_markdown_file(root_path):
    result = []
    for item in os.listdir(root_path):
        item_path = root_path + '/' + item
        if item.endswith('.md'):
            result.append(item_path)
        elif os.path.isdir(item_path):
            result += get_all_markdown_file(item_path)
    
    return result


if __name__ == '__main__':
    pass