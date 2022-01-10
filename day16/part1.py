with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

def seperate_packets(packetsToParse, packetAmount = None):
    splitPackets = {}
    while len(packetsToParse) > 8 and (packetAmount is None or len(splitPackets) < packetAmount):
        packetVersion = int(packetsToParse[:3], 2)
        packetType = int(packetsToParse[3:6], 2)
        if packetType == 4:
            contents = packetsToParse[6:]
            literal = ''
            for i in range(5, len(contents) + 1, 5):
                literal += contents[i-4:i]
                if contents[i-5:i][0] == '0':
                    key = packetsToParse[:i + 6]
                    while key in splitPackets:
                        key = '0' + key
                    splitPackets[key] = [packetVersion, packetType, int(literal, 2)]
                    packetsToParse = contents[i:]
                    break
        else:
            packetLengthType = int(packetsToParse[6], 2)
            if packetLengthType == 0:
                packetLength = int(packetsToParse[7:22], 2)
                contents = packetsToParse[22:]
                key = packetsToParse[:packetLength + 22]
                while key in splitPackets:
                    key = '0' + key
                splitPackets[key] = [packetVersion, packetType, seperate_packets(contents[:packetLength])]
                packetsToParse = contents[packetLength:]
            else:
                packetNumber = int(packetsToParse[7:18], 2)
                contents = packetsToParse[18:]
                key = packetsToParse
                while key in splitPackets:
                    key = '0' + key
                splitPackets[key] = [packetVersion, packetType, seperate_packets(contents, packetNumber)]
                packetsToParse = ''
    return splitPackets

def count_versions(packets):
    version = 0
    for key in packets:
        version += packets[key][0]
        if packets[key][1] != 4:
            version += count_versions(packets[key][2])
    return version

for line in lines:
    packet = bin(int(line, 16))[2:]
    while len(packet) < len(line) * 4:
        packet = "0" + packet
    packets = seperate_packets(packet)
    print(count_versions(packets))