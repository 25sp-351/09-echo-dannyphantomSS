
import socket
import threading
import argparse

def handle_client(conn, addr, verbose):
    with conn:
        if verbose:
            print(f"[+] Connection from {addr}")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                lines = data.split(b'\n')
                for line in lines:
                    if line:
                        line += b'\n'
                        if verbose:
                            print(f"Received: {line.decode().rstrip()}")
                        conn.sendall(line)
        except Exception as e:
            if verbose:
                print(f"[-] Error: {e}")
        finally:
            if verbose:
                print(f"[-] Connection closed: {addr}")

def main():
    parser = argparse.ArgumentParser(description="TCP Echo Server")
    parser.add_argument("-p", type=int, default=2345, help="Port to listen on (default: 2345)")
    parser.add_argument("-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    HOST = '0.0.0.0'
    PORT = args.p
    verbose = args.v

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        if verbose:
            print(f"[*] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr, verbose))
            client_thread.daemon = True
            client_thread.start()

if __name__ == "__main__":
    main()
