from scapy.all import sniff, Ether, IP, IPv6, TCP, UDP, ICMP


def packet_handler(packet):
    if Ether in packet:
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        print(f"\nEthernet: {src_mac} -> {dst_mac}")

    if IP in packet:
        print(f"IPv4: {packet[IP].src} -> {packet[IP].dst}")

    elif IPv6 in packet:
        print(f"IPv6: {packet[IPv6].src} -> {packet[IPv6].dst}")

    if TCP in packet:
        print(
            f"TCP: {packet[TCP].sport} -> {packet[TCP].dport} "
            f"flags={packet[TCP].flags}"
        )

    elif UDP in packet:
        print(f"UDP: {packet[UDP].sport} -> {packet[UDP].dport}")

    elif ICMP in packet:
        print("ICMP")

    print(f"Length: {len(packet)} bytes")


print("Nasłuchiwanie pakietów... Ctrl+C aby zakończyć.")

sniff(prn=packet_handler, store=False)
