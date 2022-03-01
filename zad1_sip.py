#from  sipfullproxy import UDPHandler
import sipfullproxy
import socket
import socketserver
import logging

PORT = 5060
HOST = '0.0.0.0'

def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='zaznam_hovorov.log',level=logging.INFO,datefmt='%H:%M:%S')
    ipaddress = socket.gethostbyname(socket.gethostname())
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    server.serve_forever()



if __name__ == "__main__":
    main()