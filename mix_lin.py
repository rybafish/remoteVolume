from pulsectl import Pulse, PulseError
from pulsectl.pulsectl import PulseOperationFailed

class Mixer:

    pulse = None
    sink = None
    device_id = None

    def __init__(self):
        pass

    def init(self):
        try:
            self.pulse = Pulse('get-volume')
            self.device_id = self.pulse.server_info().default_sink_name
            self.sink = self.pulse.get_sink_by_name(self.device_id)
        except PulseError as e:
            print('cannot init pulse')

        print(f'device id: {self.device_id}')
        print(f'device: {self.sink.description}')

    def deviceChanged(self):

        if self.sink is None:
            print('1 device init')
            self.init()

        if self.sink is None:
            print('2 device null?')
            return
        
        id = self.pulse.server_info().default_sink_name

        if self.device_id is None:
            self.device_id = id
            print('3 device id change')
            return False

        if self.device_id == id:
            # print('3 device id no change')
            return False

        print('deviceChanged = True')
        return True
            
    def getVolume(self):
        vol = sum(self.sink.volume.values) / len(self.sink.volume.values)
        vol = round(vol*100)
        return vol
    
    def setVolume(self, vol):
        try:
            self.pulse.volume_set_all_chans(self.sink, vol/100)
        except PulseOperationFailed as ex:
            print(f'setVolume exception, destroy sink')
            self.sink = None
            self.device_id = None
            self.init()

