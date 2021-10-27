import time
import webbrowser
import os
from os import terminal_size
import socket
from typing import Sized
import eel
import threading
import argparse
import struct


def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ


try:
    import vgamepad as vg
except(Exception):
    if (Is64Windows()):
        os.startfile('ViGEmBusSetup_x64.msi')
    else:
        os.startfile('ViGEmBusSetup_x86.msi')
    pass


eel.init('web')


class NetworkInfo:
    sendCommands = True
    terminate = False
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
            raise TypeError("Expected float as sensitivity")

    def processData(self):
        self.sock.bind((self.UDP_IP, self.udp_port))
        eel.showOutput(
            f'Running on IP: {str(socket.gethostbyname(socket.gethostname()))} and port {net.udp_port}')
        while True:
            try:
                data, addr = net.sock.recvfrom(
                    1024)  # buffer size is 1024 bytes
                if not data:
                    break
                data = data.decode('UTF-8')
                data = data[1:-1].split(',')
                # didReceiveData = True

                # while (data == None):
                #     steering = 0
                #     accelerator = 'false'
                #     brake = 'false'
                #     gamepad.right_trigger(value=0)
                #     gamepad.left_trigger(value=0)
                #     gamepad.left_joystick_float(
                #         x_value_float=0, y_value_float=0)
                #     gamepad.update()
                #     print(steering)
                #     print(accelerator)
                #     print(brake)

                steering = (round((float(data[0][1:-1])), 4))
                if (steering > net.sens):
                    steering = net.sens
                elif (steering < -net.sens):
                    steering = -net.sens
                accelerator = ((data[1][1:-1]))
                brake = ((data[2][1:-1]))

                if (self.sendCommands == True):
                    if(accelerator == 'true'):
                        gamepad.right_trigger(value=255)
                    else:
                        gamepad.right_trigger(value=0)
                    if(brake == 'true'):
                        gamepad.left_trigger(value=255)
                    else:
                        gamepad.left_trigger(value=0)

                    # print(f"Accelerator:{accelerator}")
                    # print(f"Brake:{brake}")
                    # print(f"Steering:{getNewValue(steering)}")
                    eel.rotateImage(getAngle(steering)-90)
                    gamepad.left_joystick_float(x_value_float=getNewValue(
                        steering), y_value_float=0)  # values between -1.0 and 1.0
                    gamepad.update()
            except KeyboardInterrupt:
                return
        print("SLDKJFHLSKDJFHLSKDFJHSLDKFJHTERMINATER")


gamepad = vg.VX360Gamepad()
net = NetworkInfo()


def getNewValue(n):
    oldRange = (net.sens+net.sens)  # oldMax -Oldmin
    newRange = (1+1)  # newMax - newMin
    newValue = (((n + net.sens)*newRange)/oldRange) - 1
    return newValue


def getAngle(n):
    oldRange = (net.sens+net.sens)  # oldMax -Oldmin
    newRange = (90+90)  # newMax - newMin
    newValue = (((n + net.sens)*newRange)/oldRange) - 1
    return newValue


@eel.expose
def togglePython(sens):
    try:
        net.storeSens(float(sens))
        net.sendCommands = not net.sendCommands
    except RuntimeError:
        pass


t1 = threading.Thread(target=net.processData)


def startThread():
    t1.start()


@eel.expose
def main(sens):
    net.storePort(int(50000))
    if (sens != None):
        net.storeSens(float(sens))
    startThread()


eel.updateIP(str(net.UDP_IP))

try:
    eel.start('index.html', size=(1000, 600))

except(SystemExit, MemoryError, KeyboardInterrupt):
    os.system('taskkill /F /IM python.exe /T')
