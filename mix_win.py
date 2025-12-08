
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL, COMError

class Mixer:

    device = None
    device_id = None
    volume = None

    def __init__(self):
        pass

    def init(self):
        try:
            self.device = AudioUtilities.GetSpeakers()
            self.device_id = self.device.id

            # interface = global_device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            # global_volume = cast(interface, POINTER(IAudioEndpointVolume))            
            self.volume = self.device.EndpointVolume.QueryInterface(IAudioEndpointVolume)

        except COMError:
            print('Oops, no device detected')

    def deviceChanged(self):
        if self.device is None:
            self.init()

        if self.device is None:
            return

        id = self.device.id

        if self.device_id is None:
            self.device_id = id
            return False

        if self.device_id == id:
            return False

        return True
    

    def setVolume(self, vol):
        try:
            self.volume.SetMasterVolumeLevelScalar(vol/100.0, None)
        except OSError as e:
            print(f'\n{e}')
