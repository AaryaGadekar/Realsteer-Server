import socket
import vgamepad as vg
import argparse


class NetworkInfo:
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)
    UDP_IP = str(socket.gethostbyname(socket.gethostname()))
    udp_port = 0
    didReceiveData = False
    sens = 0.6
    running = False

    def __init__(self, port=None) -> None:
        if(port != None):
            self.udp_port = port
            self.didReceiveData = False
            self.sens = 0.6
            self.running = False

    def storePort(self, portInt):
        try:
            self.udp_port = portInt
            self.__init__
        except:
            raise TypeError("Expected integer as port number")

    def storeSens(self, sensInt):
        try:
            self.sens = sensInt
        except:
            raise TypeError("Expected integer as sensitivity")

    def processData(self):
        self.sock.bind((self.UDP_IP, self.udp_port))
        while True:
            try:
                data, addr = net.sock.recvfrom(
                    1024)  # buffer size is 1024 bytes
                data = data.decode('UTF-8')
                data = data[1:-1].split(',')
                # didReceiveData = True

                while (data == None):
                    steering = 0
                    accelerator = 'false'
                    brake = 'false'
                    gamepad.right_trigger(value=0)
                    gamepad.left_trigger(value=0)
                    gamepad.left_joystick_float(
                        x_value_float=0, y_value_float=0)
                    gamepad.update()
                    print(steering)
                    print(accelerator)
                    print(brake)

                steering = (round((float(data[0][1:-1])), 4))
                if (steering > net.sens):
                    steering = net.sens
                elif (steering < -net.sens):
                    steering = -net.sens
                accelerator = ((data[1][1:-1]))
                brake = ((data[2][1:-1]))

                if(accelerator == 'true'):
                    gamepad.right_trigger(value=255)
                else:
                    gamepad.right_trigger(value=0)
                if(brake == 'true'):
                    gamepad.left_trigger(value=255)
                else:
                    gamepad.left_trigger(value=0)

                print(f"Accelerator:{accelerator}")
                print(f"Brake:{brake}")
                print(f"Steering:{getNewValue(steering)}")
                gamepad.left_joystick_float(x_value_float=getNewValue(
                    steering), y_value_float=0)  # values between -1.0 and 1.0
                gamepad.update()
            except KeyboardInterrupt:
                break


gamepad = vg.VX360Gamepad()
net = NetworkInfo()


def getNewValue(n):
    oldRange = (net.sens+net.sens)  # oldMax -Oldmin
    newRange = (1+1)  # newMax - newMin
    newValue = (((n + net.sens)*newRange)/oldRange) - 1
    return newValue


def main():
    my_parser = argparse.ArgumentParser()
    my_parser.version = '1.0'
    my_parser.add_argument('--port', default=50000,
                           const=50000, type=int, nargs='?', help='set custom port number; default:50000')
    my_parser.add_argument('--sensitivity', default=0.6,
                           const=0.6, type=int, nargs='?', help='Set custom sensitivity (0 to 1); default:0.6')
    args = my_parser.parse_args()

    net.storePort(int(args.port))
    print(
        f'Running on IP: {str(socket.gethostbyname(socket.gethostname()))} and port {net.udp_port}')
    net.processData()


if __name__ == '__main__':
    main()
