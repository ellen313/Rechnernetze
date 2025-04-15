# programmierung von sockets

#tcp.port == 50000 filter in WireShark 
#CurrPorts auch noch öffnen

#schicken von UDP
#links, empfängerseite 
import socket

#2
#currport paket schicken 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('Hallo'.encode('utf-8'), ('127.0.0.1', 50000)) #uft-8 ist default; 50000 ist Port
#in wireshark mit udp.port == 50000 zu sehen
#Port 58062 in WireShark wurde von OS geschickt und wird dann Python in CUrrPort zugewiesen
#4
msg, addr = sock.recvfrom(100)
msg, addr = sock.recvfrom(5) #wenn man zu wenig puffer bereit stellt, dann kommt
#ein fehler raus, message wird trotzdem ausgelsen aber anschließend gelöscht
#timeout
socket.setdefaulttimeout(5) #5 sek warten, der dann mit try accept abgefangen werden kann
msg, addr = sock.recvfrom(5)


#rechts, senderseite
import socket
#1
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',50000))
#eingeben und in currport nachschauen python.exe
#3 
msg, addr=sock.recvfrom(20)
addr #gibt die Adresse des UDP Sockets aus
msg #gibt die Message des UDP Sockets aus
msg.decode()
sock.sendto('Hallo zuruck!'.encode('utf-8'), addr)

#-----------------------------------------------------

#listen socket für TCP 
#links, empfängerseite
#1
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1',50000))

#TCP Port bekommen, ersten drei sind leer und sind nur Header (sagt dass es senden möchte) SYN SYN,ACK ACk
#4 jetzt sind beide sockets connected
conn
conn.send('Hallo zuruck!'.encode())
conn.recv(100).decode()
conn.send('Hallo zuruck!'.encode())

#rechts, senderseite
#1
import socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('127.0.0.1',50000))
listen_socket.listen(1) #warte platz für einen platz
#3
conn, addr= listen_socket.accept() #verbindung aufnehmen 
addr
conn
#5
# auslesen
conn.recv(10).decode() # byteweises auslesen


# in tcp socket schreibt immer nur einer rein dh bei mehreren absendern gibt es mehrere sockets
# tcp sorgt dass alles auch ankommt, also byte für byte; falls etwas verloren gehen sollte, sorgt tcp dafür, dass es nochmal gesendet wird 
# bei udp sockets schreiben alle in ein socket rein 
# RST Reset 

# remote und lokale adresse wird immer benötigt, um die socketverbindung zu ermöglichen
# 