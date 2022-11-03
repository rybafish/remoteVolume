#
# Simple server side script to adjust system msater volume via http
#
# 2022-11-02 EVN

# some details https://learn.microsoft.com/en-us/windows/win32/api/endpointvolume/nf-endpointvolume-iaudioendpointvolume-setmastervolumelevelscalar

import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from math import log

from pynput.keyboard import Key, Controller

import os
import socket
import time

conf_port = 8000

global_volume = None
global_keyboard = None

def init_globals():

    global global_volume
    global global_keyboard

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    
    global_volume = cast(interface, POINTER(IAudioEndpointVolume))            
    global_keyboard = Controller()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    '''
    # makes no sence as it is called on every request
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
    '''
        
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        
        s = self.path
                
        if s[:12] == '/volume?set=':
            vol = int(s[12:])
            self.doVolume(vol)
        elif s == '/':
            self.doIndex()
        elif s == '/icon.png':
            self.doIcon()
        elif s == '/splash.png':
            self.doSplash()
        elif s[:10] == '/send?key=':
            keyCode = int(s[10:])
            self.doKey(keyCode)
        else:
            print(f'unexpected request: {s}')
            pass    # unexpected input
            
    def doKey(self, keyCode):
    
        #keyCode = chr(keyCode)
        
        mapping = {
            37: Key.left,
            39: Key.right,
            176: Key.media_next,
            177: Key.media_previous,
            179: Key.media_play_pause
        }
        
        key = mapping.get(keyCode)
        
        sys.stdout.write(f'\rKey: {keyCode}    ')
        
        if key is None:
            key = chr(keyCode)
            
        self.keyboard = Controller()
            
        self.keyboard.press(key)
        self.keyboard.release(key)
    
    def doVolume(self, vol):

        sys.stdout.write(f'\rVolume: {vol} ')
        sys.stdout.flush()

        try:
            global_volume.SetMasterVolumeLevelScalar(vol/100.0, None)            
        except OSError as e:
            print(f'\n{e}')
        
    def getCurrentVolume(self):

        v = int(global_volume.GetMasterVolumeLevelScalar()*100)
        
        return v
    
    def doIndex(self):
        with open('index.html', 'rb') as f:
            index = f.read()
            
            volume = self.getCurrentVolume()
            htmlVol = f'setValue({volume});'.encode()
            
            #index = index.replace(b'value="50"', htmlVol)
            index = index.replace(b'setValue(22);', htmlVol)
            self.wfile.write(index)
            #print(f'Volume: {volume}')
            sys.stdout.write(f'\rVolume: {volume}<')
            sys.stdout.flush()


    def doIcon(self):
        with open('icon.png', 'rb') as f:
            index = f.read()
            self.wfile.write(index)
    
    def doSplash(self):
        print('\nSplash!')
        with open('splash.png', 'rb') as f:
            index = f.read()
            self.wfile.write(index)
            
    def log_message(self, format, *args):
        pass

#understand local ip:
ip1 = socket.gethostbyname(socket.gethostname())        

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip2 = s.getsockname()[0]
s.close()

print(f'server listening on port {conf_port}, ip:')
if ip1 != ip2:
    print('primary ip:', ip2)
print('ip:', ip1)

#execute the server:

while True:

    print('\nListen...')

    #redirect stderr
    #nul = os.open(os.devnull, os.O_RDWR)
    #os.dup2(nul, 2)
    
    init_globals()
        
    try:
        httpd = HTTPServer(('192.168.5.6', conf_port), SimpleHTTPRequestHandler)
        httpd.serve_forever()

        print('\nserve_forever exited for some reason')
    
    except Exception as ex:
        print(f'\nCrash in endless loop... {ex}')

print('\nShould not ever reach this point')
