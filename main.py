import socket
import vgamepad as vg

gamepad = vg.VX360Gamepad()

UDP_IP = "192.168.0.152"
UDP_PORT = 50000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def getNewValue(n):
    oldRange = (0.6+0.6) #oldMax -Oldmin
    newRange = (1+1) #newMax - newMin
    newValue = (((n + 0.6)*newRange)/oldRange) - 1
    return newValue


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data.decode('UTF-8')
    data = data[1:-1].split(',')

    if (data==None):
        steering = 0
        accelerator = 'false'
        brake = 'false'
    else:
        steering = (round((float(data[0][1:-1])),4))
        if (steering > 0.6):
            steering = 0.6
        elif (steering < -0.6):
            steering = -0.6
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
    gamepad.left_joystick_float(x_value_float=getNewValue(steering), y_value_float=0)  # values between -1.0 and 1.0
    gamepad.update()
