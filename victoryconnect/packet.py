from enum import Enum
class PacketType(Enum):
    ERROR = -1
    SUBMIT = 0
    REQUEST = 1
    COMMAND = 2

class Packet:
    packetType = PacketType.ERROR
    path =  ""
    data = []
    protocol = "DEFAULT"
    raw  = ""

    def __init__(self, type, path, data):
        self.type = type
        self.path = path
        self.data = data 
    
    def set_protocol(self, protocol):
        self.protocol = protocol

    def set_raw (self, rawPacket):
        self.raw = rawPacket

    def __str__ (self):
      
        return str(0)+ " " + self.path + " {" + ';'.join(str(x) for x in self.data) + "}~";

def parse(self, raw):
    raw  = ""
    segments = raw.split(" ")

    packet_type_str = segments[0]
    packet_type     = int(packet_type_str)
    packet_path     = segments[1]

    packet_data_str = raw[raw.index("{"):raw.index("}")]
    packet_data_arr = packet_data_str.split(";")
    