import os

dir_path = [os.path.join('my_project', 'settings'), os.path.join('my_project', 'mainapp'),
            os.path.join('my_project', 'adminapp'), os.path.join('my_project', 'authapp')]
for i in dir_path:
    if not os.path.exists(i):
        os.makedirs(i)
