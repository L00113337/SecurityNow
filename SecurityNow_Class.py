import os


class SecurityNow:

    def build_log(self):
        if not os.path.isfile(self.path):
            if not os.path.exists(self.path.split('/')[0]):
                print('Creating Data Directory')
                os.makedirs(self.path.split('/')[0])
            print('Creating Log File')
            with open(self.path, 'w') as f:
                f.write('0')

    def read_log(self):
        with open(self.path, 'r') as f:
            return int(f.read())

    def write_log(self):
        with open(self.path, 'w') as f:
            f.write(str(self.currentEP))

    def get_current_episode(self):
        return self.currentEP

    def set_current_episode(self, ep):
        self.currentEP = ep

    def update_current(self):
        self.currentEP = self.get_next_ep()

    def get_next_ep(self):
        return self.currentEP + 1

    def get_url_for_next_ep(self):
        if self.get_next_ep() < 10:
            audio = self.baseAudioURL + 'sn000' + str(self.get_next_ep()) + '/sn000' + str(self.get_next_ep()) + '.mp3'
            transcript = self.baseTranscriptURL + '/sn-00' + str(self.get_next_ep()) + '.pdf'
        elif self.get_next_ep() < 100:
            audio = self.baseAudioURL + 'sn00' + str(self.get_next_ep()) + '/sn00' + str(self.get_next_ep()) + '.mp3'
            transcript = self.baseTranscriptURL + '/sn-0' + str(self.get_next_ep()) + '.pdf'
        elif self.get_next_ep() <= self.newestEP:
            audio = self.baseAudioURL + 'sn0' + str(self.get_next_ep()) + '/sn0' + str(self.get_next_ep()) + '.mp3'
            transcript = self.baseTranscriptURL + '/sn-' + str(self.get_next_ep()) + '.pdf'
        else:
            print("Episode Does Not Exist Or self.newestEP Variable Has Not Been Updated It is Equal To = 599")
            exit(0)
        audio_name = 'Security Now #' + str(self.get_next_ep()) + '.mp3'
        transcript_name = 'Security Now #' + str(self.get_next_ep()) + '.pdf'
        full_url = {'audio': [audio, audio_name], 'transcript': [transcript, transcript_name]}
        return full_url

    def __init__(self):
        print('Initializing Variables & Log')
        self.path = 'data/log.txt'
        self.baseAudioURL = 'http://twit.cachefly.net/audio/sn/'
        self.baseTranscriptURL = 'http://grc.com/sn'
        self.newestEP = 601
        self.build_log()
        self.currentEP = self.read_log()
