from scapy.all import sniff, get_if_list
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP, UDP
import argparse
import sys

#fonction de détection de paquet
def packet_callback(packet):
    print(packet.summary())
    if Ether in packet:
        print("\nEthernet Frame:")
        print(f"Source MAC: {packet[Ether].src}")
        print(f"Destination MAC: {packet[Ether].dst}")
    if IP in packet:
        print("\nIP Packet:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"TTL: {packet[IP].ttl}")
    if TCP in packet:
        print("\nTCP Segment:")
        print(f"Source Port: {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
        print(f"Flags: {packet[TCP].flags}")
    if UDP in packet:
        print("\nUDP Datagram:")
        print(f"Source Port: {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

#Définition des arguments du programme
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
parser.add_argument("-l", "--list", default=False, type=bool)
parser.add_argument("-i", "--interface", type=str)
args = parser.parse_args()

#Si l'argument list est présent, on retourne la liste des interfaces et le programme s'arrete.
if args.list:
    print(get_if_list())
    sys.exit(0)

#Si aucune interface est renseigné, le programme s'arrete.
if not args.interface:
    print("Merci de renseigner au moins une interface")
    sys.exit(0)

# Capture les paquets sur l'interface spécifiée
print(f"Démarrage de la capture")
sniff(iface=args.interface, prn=packet_callback, store=0)