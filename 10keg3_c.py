import socket
hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "Menghitung luas segitiga"
while pesan.lower() != 'keluar':
    pesan = raw_input('Pesan: ')
    s.send(pesan)
    if pesan.lower() != 'keluar':
        response = s.recv(1024)
        print 'Respon:', response
    else:
        print "Respon: -"
s.close()
