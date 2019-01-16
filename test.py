from victoryconnect.packet import Packet
from victoryconnect.packet import PacketType

test_packet = Packet(PacketType.SUBMIT, "test/packet", [0,0,0,0])
print(test_packet.path)

test_packet.set_raw("TADAdasdasd")
print(test_packet.data)

print(str(test_packet))