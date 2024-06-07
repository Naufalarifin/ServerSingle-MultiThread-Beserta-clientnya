import socket

# Definisikan alamat dan port server
HOST = "localhost"
PORT = 8080

# Membuat fungsi untuk mengirim permintaan dan menerima respons dari server
def request_file(filename):
    # Membuat objek socket TCP
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Menghubungkan ke server
    clientSocket.connect((HOST, PORT))
    
    # Membuat permintaan HTTP GET
    request = f"GET /{filename} HTTP/1.1\r\nHost: {HOST}:{PORT}\r\n\r\n"
    
    # Mengirim permintaan ke server
    clientSocket.sendall(request.encode())
    
    # Menerima respons dari server
    response = clientSocket.recv(4096).decode()
    
    # Memisahkan header dan body respons
    header, body = response.split("\r\n\r\n", 1)
    
    # Menampilkan header dan body respons
    print("Header:\n", header)
    print("Body:\n", body)
    
    # Menutup koneksi dengan server
    clientSocket.close()

# Menggunakan fungsi untuk meminta file dari server
filename = "index.html"  # Ganti dengan nama file yang ingin Anda minta
request_file(filename)