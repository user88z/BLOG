import socket

def get_message():
    sock = socket.socket()
    sock.bind(('', 2020))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    data_all=''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())
        data_all = data_all + str(data.decode('utf-8'))
    print(data_all)
    conn.close()
    return data_all
