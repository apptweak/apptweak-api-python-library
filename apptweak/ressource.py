# internal imports
import apptweak
import sys
# external imports
import urllib.parse
import urllib.request


class Ressource(object):

    @classmethod
    def http_request(cls, url, params):
        respdata = None
        Validation().api_key()
        headers = {}
        headers['X-Apptweak-Key'] = apptweak.API_KEY
        params = urllib.parse.urlencode(params)
        if len(params) >= 1:
            url = url + '?' + params
        req = urllib.request.Request(url, headers=headers)
        respdata = cls.reader(req)

        return respdata

    @classmethod
    def reader(cls, request):
        resp = urllib.request.urlopen(request)
        if resp.getcode() != 200:
            raise Exception('ERROR CODE : ' + str(resp.getcode() +
                                                  "\n Response : "+str(resp.read().decode('utf-8'))))
        return resp.read().decode('utf-8')


class Validation(object):

    def api_key(self):
        if apptweak.API_KEY is None:
            raise Exception('ERROR : apptweak.API_KEY not set')

    def lists(self, l, size):
        if not (isinstance(l, list) and len(l) <= size):
            raise Exception(
                'ERROR : must be a list && the list must be <= ' + str(size))

    def keywords_list(self, keywords):
        self.lists(keywords, apptweak.KEYWORDS_MAX_LENGTH)

    def applications_list(self, applications):
        self.lists(applications, apptweak.APPLICATIONS_MAX_LENGTH)

    def require_params(self, params, required):
        if not all(key in params for key in required):
            raise Exception(
                'ERROR : params must contain at least the following key(s) : ' + ', '.join(required))

    def id(self, id):
        if not isinstance(id, (str, int)):
            raise Exception('ERROR : id must be a string or an int ')

    def params(self, params):
        if not isinstance(params, dict):
            raise Exception('ERROR : params must be a dict')

    def sort_type(self, sort_type):
        if not isinstance(sort_type, str):
            raise Exception('ERROR : sort_type must be a dict')
