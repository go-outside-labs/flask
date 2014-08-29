#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


''' USE MD5 HASHING FUCNTION TO CREATE A HASH FOR THE URL.
    ENCODES IN BASE64. '''

import base64
import md5
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def hashFunction(url, SIZEURL=4):
    url = url + id_generator()
    shorter = base64.b64encode(md5.new(url).digest()[-SIZEURL:])
    sanitized = shorter.replace('=','').replace('/','_')
    return sanitized

