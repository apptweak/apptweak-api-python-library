from apptweak.ressource import *
import apptweak
import json

#api url parts
API_DOMAIN = 'https://api.apptweak.com'


API_SUB_PATH = {
    'applications':'applications','categories':'categories',
    'keywords':'keywords','reviews':'reviews','displayed':'displayed',
    'filter':'filter'
    }

API_END_PATH = {
    'metadata':'metadata.json', 'ratings':'ratings.json','ratings-history':'ratings-history.json',
    'rankings':'rankings.json', 'power':'power.json', 'backlinks':'backlinks.json',
    'downloads':'downloads.json','revenues':'revenues.json',
    'searches':'searches.json','top':'top.json','reviews':'reviews.json',
    'list':'list.json','stats':'stats.json','competitors':'competitors.json',
    'app-rankings':'app-rankings.json','trendings':'trendings.json',
    'volume-history':'volume-history.json'
    }

API_PLATEFORM_PATH = {
    'ios':'ios','android':'android'
    }


#options
#{'free':'free.json','paid':'paid.json','grossing':'grossing.json'}
REVIEWS_SORTING_OPTIONS = {
    'most_useful':'most_useful.json','most_recent':'most_recent.json',
    'most_critical':'most_critical.json','most_positive':'most_positive.json'
    }

def urljoin(url1, url2):
    if url1.endswith('/'):
        url1 = url1[0:-1]
    if not url2.startswith('/'):
        url2 = '/' + url2
    return url1 + url2

def urlConstruct(urls):
    finalUrl = API_DOMAIN
    for u in urls:
        finalUrl = urljoin(finalUrl,u)
    return finalUrl


def list_to_string(l):
    l2 = [str(it) for it in l]
    return ','.join(l2)


class Plateform():

    def __init__(self,plateform_name):
        self.plateform_name = plateform_name
        pass

    @classmethod
    def applications(self, application_id, end_path, params = {}):
        Validation().id(application_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'],str(application_id), end_path])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def metadata(self, application_id, params = {}):
        """
        fetch a specific app metadata

        parameters
        ---------- 
        application_id : int
             an application id
        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            language : ISO Alpha-2, optional
                default en

            device : string, optional !!! IOS
                default iphone

            max-age : int, optional
                default : 94608000
                in seconds
        """
        return self.applications(application_id, API_END_PATH['metadata'], params)

    @classmethod
    def ratings(self, application_id, params = {}):
        """
        fetch a specific app ratings

        parameters
        ----------
        application_id : int
             an application id
        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional
        """
        Validation().id(application_id)
        Validation().params(params)
        pass

    @classmethod
    def rankings(self, application_id, params = {}):
        """
        fetch a specific app ranking

        parameters
        ----------
        application_id : int
             an application id
        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional

            type : string (free, paid, grossing), optional
        """
        return self.applications(application_id, API_END_PATH['rankings'], params)

    @classmethod
    def power(self, application_id, params = {}):
        """
        the power of the app based on its rankings in its category and in the overall category.

        parameters
        ----------
        application_id : int
             an application id
        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, required
                defualt us

            device : string, optional !!! IOS
                default iphone

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional
        """
        required = ['country']
        Validation().require_params(params, required)
        return self.applications(application_id, API_END_PATH['power'], params)

    @classmethod
    def backlinks(self, application_id):
        return self.applications(application_id, API_END_PATH['backlinks'])

    @classmethod
    def downloads(self, application_id, params = {}):
        """
        estimation download of an app in a specific country in a date range

        parameters
        ----------
        application_id : int
             an application id

        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional
        """
        return self.applications(application_id, API_END_PATH['downloads'], params)

    @classmethod
    def revenues(self, application_id, params = {}):
        """
        estimation revenues of an app in a specific country in a date range

        parameters
        ----------
        application_id : int
             an application id

        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional
                default iphone

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional
        """
        return self.applications(application_id, API_END_PATH['revenues'], params)

    @classmethod
    def reviews(self, application_id, params = {}):
        """
        fetch the top 100 reviews for a specific country

        parameters
        ----------
        application_id : int
             an application id

        params : dict(), optional
            the params keys are (country)

                country : ISO Alpha-2, optional
                    defualt us
        """
        return self.applications(application_id, API_END_PATH['reviews'], params)

    @classmethod
    def searches(self, params):
        """
        query the appstore

        parameters
        ----------
        params : dict()
            the params keys are (country, device, language, term, num)

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            language : ISO Alpha-2, optional
                default en

            term : string, required
                term you want to search in the appstore

            num : int, optional
                default 10
                number of items you want to fetch
        """
        Validation().params(params)
        required = ['term']
        Validation().require_params(params, required)
        url = urlConstruct([self.plateform_name, API_END_PATH['searches']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def top_charts(self, category_id, params = {}):
        """
        Top Chart allows you to fetch the most popular applications for a category
        and type in a country for a device. We return the top 200 applications.
        Results are updated daily.
        The first application is the one that has the best rank for the requested chart.

        parameters
        ----------
        category_id : int
             the store category id

        params : dict()
            the params keys are (country, device, language, type)

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            language : ISO Alpha-2, optional
                default en

            term : string, required
                term you want to search in the appstore

            type : string (free, paid, grossing), optional
        """
        Validation().id(category_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name,API_SUB_PATH['categories'],str(category_id),API_END_PATH['top']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def top_displayed_reviews(self, application_id, sort_type, params={}):
        """
        Application Top Displayed Reviews allows you to fetch all the top displayed reviews
        entries about a specific app on the App Store in the selected country and based on the given sort parameter.
        Apple classes by default the application's reviews by the Most Useful.
        With that endpoint you would be able to get the top displayed reviews for an application,
        based on that criterion.

        parameters
        ----------
        application_id : int
             an application id
        sort_type : 

        params : dict()
            the params keys are (country, size)

            country : ISO Alpha-2, optional
                defualt us

            size : int, optional
                default 100
                The number of reviews you want to fetch
        """
        Validation().id(application_id)
        Validation().params(params)
        Validation().sort_type(sort_type)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'], str(application_id),API_SUB_PATH['reviews'],API_SUB_PATH['displayed'],REVIEWS_SORTING_OPTIONS[sort_type]])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def filtered_reviews(self, application_id, params):
        """
        Application Filtered Reviews allows you to fetch all the reviews entries about a specific app
        on the App Store in the selected country and based on several criteria like date,
        rating or even to search for a specific word or expression in the reviews's body.

        parameters
        ----------
        application_id : int
             an application id

        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            max_rating : int, optional
                default 5

            min_rating : int, optional
                default 1

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional

            from : int, optional
                default 1
                Index from which we start to fetch the data (pagination)

            term : string, required
                term you want to search in the revieuws

            size : int, optional
                default 100
                The number of reviews you want to fetch
        """
        Validation().id(application_id)
        Validation().params(params)
        required = ['term']
        Validation().require_params(params, required)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'], str(application_id),API_SUB_PATH['reviews'],API_SUB_PATH['filter'],API_END_PATH['list']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def review_stats(self, application_id,params = {}):
        """
        Application Reviews Stats allows you to fetch all the stats
        related to the reviews entries about a specific app

        parameters
        ----------
        application_id : int

        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, optional
                    defualt us

            max_rating : int, optional
                default 5

            min_rating : int, optional
                default 1

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional

            term : string, optional
                term you want to search in the reviews

        """
        Validation().id(application_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'], str(application_id),API_SUB_PATH['reviews'],API_SUB_PATH['filter'],API_END_PATH['stats']])
        return json.loads(Ressource.http_request(url, params))

    #keywords

    @classmethod
    def app_top_keywords(self, application_id,params = {}):
        """
        App top keywords allows you to retrieve a list of keywords
        an app is performing well on.
        This is useful to investigate the keywords you should target.

        parameters
        ----------
        application : int
             the store category id

        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            language : ISO Alpha-2, optional
                default en
        """
        Validation().id(application_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'],str(application_id),API_SUB_PATH['keywords'],API_END_PATH['top']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def keywords_stats(self, params):
        """
        This method returns the list of provided keywords
        and evaluates the volume and competiton in a given country,
        language and device.

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            keywords : list of string <= 10

            language : ISO Alpha-2, optional
                default en
        """
        Validation().params(params)
        required = ['keywords']
        Validation().require_params(params, required)
        Validation().keywords_list(params['keywords'])
        params['keywords'] = list_to_string(params['keywords'])
        url = urlConstruct([self.plateform_name,API_SUB_PATH['keywords'],API_END_PATH['stats']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def keywords_competitors(self, application_id, params={}):
        """
        This method returns the top 10 most relevant competitors we found.
        application_id :

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            language : ISO Alpha-2, optional
                default en
        """
        Validation().id(application_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['applications'],str(application_id),API_SUB_PATH['keywords'],API_END_PATH['competitors']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def keywords_ranking_competitors(self,  params):
        """
        The keywords rankings for Applications allow you to get the 90 days rankings
        for one or several applications for a keywords list. We compute the position of the apps
        for each keyword on a best effort basis and the list may thus be incomplete or even empty.
        However, once an App Keyword Ranking is performed asking for data for a specifi keyword,
        the keyword is flagged in our system and fetched once a day.
        Subsequent calls for the same keyword should thus yield complete results.

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            keywords : list of string <= 10

            applications : list <=5

            language : ISO Alpha-2, optional
                default en
        """
        Validation().params(params)
        required = ['applications','keywords']
        Validation().require_params(params, required)
        Validation().applications_list(params['applications'])
        Validation().keywords_list(params['keywords'])
        params['keywords'] = list_to_string(params['keywords'])
        params['applications'] = list_to_string(params['applications'])
        url = urlConstruct([self.plateform_name,API_SUB_PATH['keywords'],API_END_PATH['app-rankings']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def category_top_keywords(self, category_id, params = {}):
        """
        This method returns the top 10 most relevant competitors we found.

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

            language : ISO Alpha-2, optional
                default en

            type : string ( free or paid ) optional

        """
        Validation().id(category_id)
        Validation().params(params)
        url = urlConstruct([self.plateform_name, API_SUB_PATH['categories'],str(category_id),API_SUB_PATH['keywords'],API_END_PATH['top']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def keywords_trending(self, params = {}):
        """
        The trending keywords are the list of 10 suggested keywords
        search displayed in the search result of the appstore when the user has not typed anything.

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            device : string, optional !!! IOS
                default iphone

        """
        Validation().params(params)
        url = urlConstruct([API_PLATEFORM_PATH['ios'], API_SUB_PATH['keywords'],API_END_PATH['trendings']])
        return json.loads(Ressource.http_request(url, params))

    @classmethod
    def keywords_volume_history(self, params):
        """
        The Application Keywords Volume History allows you to fetch information
        about the popularity and competition of a list of keywords for a selected period.
        This is useful to estimate if it would be interesting to put an emphasis on
        a given the word in the app title, description or to target it in the keywords field.
        But also to compare how this keyword performs in comparison to new ones
        or those used by your competition, and evaluate them on a selected period.

        parameters
        ----------
        params : dict()
            the params keys are :

            country : ISO Alpha-2, optional
                defualt us

            keywords : list of string <= 10

            language : ISO Alpha-2, optional
                default en

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional
        """
        Validation().params(params)
        required = ['keywords']
        Validation().require_params(params, required)
        Validation().keywords_list(params['keywords'])
        params['keywords'] = list_to_string(params['keywords'])
        url = urlConstruct([API_PLATEFORM_PATH['ios'], API_SUB_PATH['keywords'],API_END_PATH['volume-history']])
        return json.loads(Ressource.http_request(url, params))
