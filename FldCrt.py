import os

path = '/Users/USER NAME/Desktop/'  # <- Past your PATH

prjname = input('Project name please: ')
folders = \
    ['input',
     'output',
     'other',
     'test1',
     'test2']


def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)


fullpath = os.path.join(path, prjname)
createFolder(fullpath)

for i in folders:
    folder = os.path.join(fullpath, i)
    createFolder(folder)
