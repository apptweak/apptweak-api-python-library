import apptweak.ressource
import apptweak.ios
import apptweak.android
import apptweak.plateform

__version__ = "1.0"


#needed to acces apptweak.io data
API_KEY = None

#list size restriciton
KEYWORDS_MAX_LENGTH = 10
APPLICATIONS_MAX_LENGTH = 5


#synthax object simplifaction
Ios = ios.Ios
Android = android.Android

#for test purpose only
list_to_string = plateform.list_to_string
urljoin = plateform.urljoin
Ressource = ressource.Ressource
Validation = ressource.Validation
