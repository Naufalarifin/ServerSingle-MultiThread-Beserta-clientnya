#import socket module
from socket import *
# Membuat objek socket TCP ke local host
serverSocket = socket(AF_INET,SOCK_STREAM)

# Mendefinisikan host dan port yang akan digunakan
HOST = "localhost"
PORT = 8080

# Menghubungkan socket ke local host dan port yang telah ditentukan
serverSocket.bind((HOST, PORT))

# Memastikan program telah terhubung ke koneksi server
serverSocket.listen(5)
print("Server is ready....")

# Fungsi makeResponse disini bertugas untuk memberi response kepada client
def makeResponse(filename):
    try: #syntax try akan mengecek apakah file ada atau tidak
        with open(filename, 'r') as file: # Membuka file dengan mode read & Membaca isi file
            # File read akan disimpan dalam file_content
            file_content = file.read()
            # Membuat response kepada client yang isinya :"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
            # Menyertakan isi file sebagai body respons
            response_body = file_content
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        # Menyertakan pesan 404 Not Found sebagai body respons
        response_body = "<html><body><h1>404 Not Found</h1></body></html>"
    
    return response + response_body

def handle_client(client_socket):
    # Menerima permintaan dari klien
    request = client_socket.recv(1024).decode()
    
    # Parsing permintaan untuk mendapatkan nama file yang diminta
    # Memisahkan string permintaan berdasarkan spasi
    request_parts = request.split()
    # Mengambil elemen kedua dari array yang merupakan nama file
    file_name = request_parts[1][1:]  # Menghilangkan karakter '/' di depan nama file
    
    # Membuat respons berdasarkan file yang diminta
    response = makeResponse(file_name)
    
    # Mengirim respons ke klien
    client_socket.sendall(response.encode())
    
    # Menampilkan respons di server
    print("Response:\n", response.split("\r\n\r\n")[0])
    
    # Menutup koneksi dengan klien
    client_socket.close()

while True:
    # Menerima koneksi dari klien
    client_socket, client_address = serverSocket.accept()
    print("Connected: ", client_address)
    
    # Membuat jawaban untuk klien
    handle_client(client_socket)