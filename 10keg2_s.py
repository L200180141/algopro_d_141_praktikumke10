import socket
import platform
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50001))
s.listen(5)
print "Server sudah siap"
perintah = ''
while perintah.lower() != 'quit':
    komm, addr = s.accept()
    while perintah.lower() != 'quit':
        perintah = komm.recv(1024)
        if perintah.lower() == 'quit':
            s.close()
            break
        print 'Command:', perintah
        if perintah.lower() == 'machine':
            respon = platform.machine()
            komm.send(respon)
        elif perintah.lower() == 'release':
            respon = platform.release()
            komm.send(respon)
        elif perintah.lower() == 'system':
            respon = platform.system()
            komm.send(respon)
        elif perintah.lower() == 'version':
            respon = platform.version()
            komm.send(respon)
        elif perintah.lower() == 'node':
            respon = platform.node()
            komm.send(respon)
        else:
            komm.send('unknown command')
