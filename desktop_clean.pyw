#!/usr/bin/env python3
r'''
This script makes use of the blackhole module to move
every file on Desktop to Downloads/Singularity. Then,
it organizes the files in Downloads/Singularity into
folders separated by extensions.
'''

import blackhole

blackhole.drift()
blackhole.organize()
