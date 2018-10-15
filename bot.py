from socket import *
import ssl
import time


server = "server"
port = 0000
ch = "#channel"
nick = "nick"
username = "username"
realname = "realname"

s = socket(AF_INET, SOCK_STREAM)
s = ssl.wrap_socket(s, keyfile="/etc/ssl/private/server.key",
                       certfile="/etc/ssl/certs/server.crt",
                       server_side=False, cert_reqs=ssl.CERT_NONE,
                       ssl_version=ssl.PROTOCOL_TLSv1,
                       ca_certs="/etc/ssl/certs/ca-certificates.crt",
                       do_handshake_on_connect=False,
                       suppress_ragged_eofs=True, ciphers=None)
s.connect((server, port))

cmd1 = [("USER %s %s %s :%s\n" % (username, username, username, realname)), ("NICK %s\n" % username)]
s.send(cmd1[0])
time.sleep(2)
s.send(cmd1[1])
time.sleep(2)

while 1:
  data = s.recv(1024)
  if data.find("PING") != -1:
    pong = data.split()[1]
    s.send("PONG " + pong + "\n")
    time.sleep(2)
    print "Ping replied!"
    time.sleep(2)
    break

cmd = ("JOIN %s\n" % ch)
s.send(cmd)
time.sleep(2)

while 1:
  data = s.recv(4096)
  if data.find("PING") != -1:
    pong = data.split()[1]
    s.send("PONG " + pong + "\n")
    time.sleep(2)
    print "Ping replied!"
    time.sleep(2)
    continue
