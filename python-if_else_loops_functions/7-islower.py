#!/usr/bin/env python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return 1
    else:
        return 0
# On met ord(c) pour comparer nombre entre nombre et pas lettre avec nombre
