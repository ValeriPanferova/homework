import os

ROOT = os.path.dirname(__file__)
root_dir = os.path.join(ROOT, 'my_project')
template_path = os.path.join(root_dir, 'templates')

if not os.path.exists(template_path):
    os.makedirs(template_path)


def move_into_templates(file):
    if os.path.basename(file) != 'templates':
        os.rename(os.path.join(root_dir, os.path.basename(file)), os.path.join(template_path, os.path.basename(file)))


for i in os.listdir(root_dir):
    move_into_templates(i)
