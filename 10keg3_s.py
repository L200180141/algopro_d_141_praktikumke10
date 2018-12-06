import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50005))
s.listen(5)
print "Server sudah siap"
perintah = ''
a=0
t=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'tinggi':
                t = int(data[1])
                respon = "tinggi dicatat"
                komm.send(respon)
            elif perintah == 'alas':
                a = int(data[1])
                respon = "alas dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = float(a*t/2)
            respon = "Luas segitiga dengan alas {} dan tinggi {} adalah {}".format(a,t,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
