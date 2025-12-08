from pulsectl import Pulse, PulseError

class Mixer:

    pulse = None
    device = None
    device_id = None
    volume = None

    def __init__(self):
        pass

    def init(self):
        try:
            self.pulse = Pulse('get-volume')
            self.sink = self.pulse.get_sink_by_name(self.pulse.server_info().default_sink_name)
        except PulseError as e:
            print('cannot init pulse')

        self.device_id = self.sink.index
        print(f'device id: {self.device_id}')

    def deviceChanged(self):

        if self.sink is None:
            self.init()

        if self.sink is None:
            return
        
        id = self.sink.index
        

        if self.device_id is None:
            self.device_id = id
            return False

        if self.device_id == id:
            return False

        return True
            
    def getVolume(self):
        vol = sum(self.sink.volume.values) / len(self.sink.volume.values)
        return vol
    
    def setVolume(self, vol):
        self.pulse.volume_set_all_chans(self.sink, vol/100)
