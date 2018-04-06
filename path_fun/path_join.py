#!/usr/bin/python3

import os

localtime_path='/etc/localtime'

chroot_path='/chroot/named'

chroot_localtime_path=os.path.join(chroot_path, localtime_path)

print(chroot_localtime_path)
