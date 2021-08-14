# Description✏️

This repository holds the code for the client side of the [iOS](https://github.com/AaryaGadekar/udp-gamepad-ios) app. Works by plugging accelerometer data received via UDP into an emulated gamepad.

**Currently only supports Windows.**

# Requirements✔️

1. **Python 3.0+**
2. **vgamepad**
3. **bottle==0.12.19**
4. **bottle-websocket==0.2.9**
5. **cffi==1.14.6**
6. **Eel==0.14.0**
7. **future==0.18.2**
8. **gevent==21.8.0**
9. **gevent-websocket==0.10.1**
10. **greenlet==1.1.1**
11. **pycparser==2.20**
12. **pyparsing==2.4.7**
13. **whichcraft==0.6.1**
14. **zope.event==4.5.0**
15. **zope.interface==5.4.0**

# Installation💽

1.  **Clone the repo**

        git clone https://github.com/AaryaGadekar/py-udp-gamepad.git

2.  **Navigate to the directory**

        cd py-udp-gamepad

3.  **Install requirements**

        pip install -r requirements.txt

4.  **Run the program**

        python main.py

    The program should output the following if installed correctly:

        Running on IP: 192.168.0.152 and port 50000

5.  View repository for instructions to run the [iOS](https://github.com/AaryaGadekar/udp-gamepad-ios) app with the given IP and port
