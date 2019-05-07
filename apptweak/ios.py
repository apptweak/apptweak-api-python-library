from apptweak.plateform import *

class Ios(Plateform):

    plateform_name = 'ios'
    def __init__(self):
        super().__init__(self.plateform_name)

    @classmethod
    def ratings(self, application_id, params = {}):
        return self.applications(application_id, API_END_PATH['ratings'], params)

    @classmethod
    def backlinks(self, application_id):
        raise Exception('Not implemented for this plateform')
