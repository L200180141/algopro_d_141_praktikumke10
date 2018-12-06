import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 5001))
print 'mesin penjawab sudah ready'
while pesan.lower() != 'q':
    pesan = raw_input('permintaan:')
    s.send(pesan)
    if pesan.lower() != 'q':
        response = s.recv(1024)
        print 'jawab', response
s.close()
