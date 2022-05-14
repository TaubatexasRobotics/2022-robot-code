def readString(self, port) -> str:
    sz = port.getBytesReceived()
    buf = bytearray(sz)
    sz = port.read(buf)
    return buf[:sz].decode("ascii")
