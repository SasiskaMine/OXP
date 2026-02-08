from sys import argv
import parametrs as pr


parameter = argv[1]

match parameter:
    case "-h" | "-help":
        pr.help_info()
    case "-i" | "-install":
        packet_url = argv[2]; """URL"""
        packet_name = argv[3]; """Packet Name"""
        pr.install(packet_url,packet_name)
    case "-r" | "-remove":
        packet_name = argv[2]; """Packet Name"""
        pr.remove(packet_name)
    case "-l" | "-list":
        pr.list_packages()
