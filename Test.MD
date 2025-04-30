python3 tcp_echo_server.py -p 2345 -v
[*] Listening on 0.0.0.0:2345



telnet localhost 2345
hello from terminal 1


Expected server output:
[+] Connection from ('127.0.0.1', 50930)
Received: hello from terminal 1



telnet localhost 2345
hi from terminal 2


Expected output in Terminal 2:

hi from terminal 2
Expected server output:


[+] Connection from ('127.0.0.1', 50932)
Received: hi from terminal 
