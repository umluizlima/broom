#!/usr/bin/env python3
# event_horizon.pyw - Moves files from Desktop to Singularity (within Downloads)
# Usage:
#   black_hole - moves every file on Desktop to Downloads/Singularity
#   TODO: black_hole eject - moves files from the singularity to specific folders based on extensions

import os, shutil

if os.name == 'nt':
    base_path = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
else:
    base_path = os.environ['HOME']
desktop = os.path.join(base_path, 'Desktop')
singularity = os.path.join(base_path, 'Downloads', 'Singularity')

if not os.path.lexists(singularity):
    os.mkdir(singularity)
    
for filename in os.listdir(desktop):

    #Check if the file already exists in the singularity. If so, enumerate it
    if os.path.lexists(os.path.join(singularity, filename)):
        n = 1
        root, ext = os.path.splitext(filename)
        while os.path.lexists(os.path.join(singularity, root + ' (' + str(n) + ')' + ext)):
            n += 1
        new_filename = root + ' (' + str(n) + ')' + ext
        os.rename(os.path.join(desktop, filename), os.path.join(desktop, new_filename))
        filename = new_filename

    #Send file to singularity
    try:
        shutil.move(os.path.join(desktop, filename), singularity)
        print(filename, 'was sent to the singularity')
    except shutil.Error:
        print('An error occurred on file:', filename)
