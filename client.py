import socket

# 伺服器的 IP 位址 (若在同一台電腦測試，請用 127.0.0.1)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5001
FILENAME = 'github_link.txt'

# 建立 TCP Socket 並連線
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"[*] 已連線至伺服器 {SERVER_HOST}:{SERVER_PORT}")

# 讀取檔案並傳送
with open(FILENAME, 'rb') as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)

print(f"[+] {FILENAME} 上傳完成！")
client_socket.close()
