import socket

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysock.connect(('data.pr4e.org', 80))

# Send the HTTP GET request
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

# Retrieve and print the response headers
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()
