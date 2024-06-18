import socket
class connect_to_server():
    def __init__(self, ip, port):
        self.ip=ip
        self.port=port
        self.client = socket.socket()
    def connect_to_s(self):
        self.client.connect((self.ip, self.port))
        messege="connected!"
        self.client.send(messege.encode())
        data = self.client.recv(1024)

        print("Server sent: ", data.decode())

    def send_somewhat(self, messege):
        self.client.send(messege.encode())
    def led(self, status):
        messege=""
        if status==1:
            messege = "led_on"
        elif status==0:
            messege = "led_off"
        self.client.send(messege.encode())
    def zummer(self, status):
        messege=""
        if status==1:
            messege = "buzzer_on"
        elif status==0:
            messege = "buzzer_off"
        self.client.send(messege.encode())
#client.close()