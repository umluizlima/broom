r'''Functions for cleaning and organizing folders.

'''
import os, shutil

user = os.path.expanduser('~')
desktop = os.path.join(user, 'Desktop')
singularity = os.path.join(user, 'Downloads', 'Singularity')

folders = {'Videos': ['.flv', '.ogg', '.avi', '.mp4', '.wmv'],
           'Images': ['.png', '.jpg', '.jpeg', '.svg', '.ai', '.psd', '.cdr', '.gif'],
           'Audio': ['.mp3', '.wma'],
           'Documents': ['.pdf', '.doc', '.ppt', '.pptx', '.docx', '.txt', '.csv'],
           'Executables': ['.exe', '.msi'],
           'Compressed': ['.zip', '.rar']}

def which_folder(filename, folders = folders):
    '''
    Check in which folder the file fits in based on its extension.
    '''
    ext = os.path.splitext(filename)[1].lower()
    for folder in folders.keys():
        if ext in folders[folder]:
            return folder
    return ''

def path_checking(path):
    '''
    Check if given folder exists. If not, create it.
    '''
    if not os.path.lexists(path):
        os.mkdir(path)

def repeat_checking(src, dst, filename):
    '''
    Check if the file already exists in the destination. If so, enumerate it.
    '''
    if os.path.lexists(os.path.join(dst, filename)):
        n = 1
        root, ext = os.path.splitext(filename)
        while os.path.lexists(os.path.join(dst, root + ' (' + str(n) + ')' + ext)):
            n += 1
        new_filename = root + ' (' + str(n) + ')' + ext
        os.rename(os.path.join(src, filename), os.path.join(src, new_filename))
        return new_filename
    else:
        return filename

def organize(src = singularity, folders = folders):
    '''
    Organizes files in source folder into extension separated folders.
    '''
    for filename in os.listdir(src):
        if which_folder(filename, folders) == '':
            continue
        else:
            dst = os.path.join(src, which_folder(filename, folders))
            path_checking(dst)
            filename = repeat_checking(src, dst, filename)
            shutil.move(os.path.join(src, filename), os.path.join(dst, filename))

def drift(src = desktop, dst = singularity):
    '''
    Sends a source's contents through the event horizon into destination.
    '''
    files = os.listdir(src)
    if len(files) > 0:
        path_checking(dst)
    for filename in files:
        filename = repeat_checking(src, dst, filename)
        try:
            shutil.move(os.path.join(src, filename),
                        os.path.join(dst, filename))
            #print(filename, 'was sent to its destination')
        except shutil.Error:
            print('An error occurred on file:', filename)
