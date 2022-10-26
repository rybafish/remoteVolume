import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from math import log

#from contextlib import redirect_stderr

import os
import socket
            
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

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
        else:
            print(f'unexpected request: {s}')
            pass    # unexpected input
            
    def doVolume(self, vol):

        sys.stdout.write(f'\rVolume: {vol}')
        sys.stdout.flush()

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))            

        volume.SetMasterVolumeLevelScalar(vol/100.0, None)            
        
    def getCurrentVolume(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))            

        v = int(volume.GetMasterVolumeLevelScalar()*100)
        
        return v
    
    def doIndex(self):
        with open('index.html', 'rb') as f:
            index = f.read()
            
            volume = self.getCurrentVolume()
            htmlVol = f'value="{volume}"'.encode()
            
            index = index.replace(b'value="50"', htmlVol)
            self.wfile.write(index)
            
    def doIcon(self):
        with open('icon.png', 'rb') as f:
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

print('server listening on:')
if ip1 != ip2:
    print('primary ip:', ip2)
print('ip:', ip1)

#execute the server:

while True:

    #redirect_stderr()
    nul = os.open(os.devnull, os.O_RDWR)
    os.dup2(nul, 2)
    
    httpd = HTTPServer(('192.168.5.6', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

    print('Exit for some reason')

print('Exit for some reason???')
