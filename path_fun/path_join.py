#!/usr/bin/python3

import os

localtime_path='/etc/localtime'

chroot_path='/chroot/named'

chroot_localtime_path=os.path.join(chroot_path, localtime_path)

print(chroot_localtime_path)

"""
First off, yes, the behavior is documented, and it's documented as being "intelligent".

The Single Unix Standard specifies:
    3.266 Pathname - ... "Multiple successive slashes are considered to be the same as one slash."
  - http://pubs.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap03.html#tag_03_266
  
So, one would think that the result of joining 2 paths,
    * /etc/localtime
    * /chroot/named

would result in

	* /chroot/named//etc/localtime

(which is a valid unix path).

"""
