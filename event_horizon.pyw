#!/usr/bin/env python3
# event_horizon.pyw - Moves files from Desktop to Singularity (within Downloads)
# Usage:
#   black_hole - moves every file on Desktop to Downloads/Singularity   

import os, shutil

base_path = os.environ['HOME']
desktop = os.path.join(base_path, 'Desktop')
downloads = os.path.join(base_path, 'Downloads')
singularity = os.path.join(downloads, 'Singularity')

if not os.path.lexists(singularity):
    os.mkdir(singularity)
    
for filename in os.listdir(desktop):
    shutil.move(os.path.join(desktop, filename), singularity)
