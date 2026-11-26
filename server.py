import socket

# 設定監聽的 IP 與 Port (0.0.0.0 代表接受所有網卡的連線)
HOST = '0.0.0.0'
PORT = 5001

# 建立 TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[*] 伺服器已啟動，正在監聽 {HOST}:{PORT}...")

# 等待客戶端連線
conn, addr = server_socket.accept()
print(f"[+] 已連線：{addr}")

# 接收資料並寫入本地檔案
with open('received_github_link.txt', 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("[+] 檔案接收完成，已儲存為 received_github_link.txt")
conn.close()
server_socket.close()
