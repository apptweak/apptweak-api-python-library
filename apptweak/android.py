from apptweak.plateform import *

class Android(Plateform):

    plateform_name = 'android'
    def __init__(self):
        super().__init__(self.plateform_name)

    @classmethod
    def ratings(self, application_id, params = {}):
        return self.applications(application_id, API_END_PATH['ratings-history'], params)

    @classmethod
    def revenues(self, application_id, params = {}):
        raise Exception('Not implemented for this plateform')

    @classmethod
    def rankings(self, application_id, params):
        """
        fetch a specific app ranking

        parameters
        ----------
        application_id : int
             an application id
        params : dict(), optional
            the params keys are :

            country : ISO Alpha-2, required
                defualt us

            start_date : string YYYY-MM-DD, optional

            end_date : string YYYY-MM-DD, optional

            type : string (free, paid, grossing), optional
        """
        Validation().params(params)
        required = ['country']
        Validation().require_params(params,required)
        return self.applications(application_id, API_END_PATH['rankings'], params)

    @classmethod
    def reviews(self, application_id, params = {}):
        Validation().params(params)
        required = ['language']
        Validation().require_params(params,required)
        return self.applications(application_id, API_END_PATH['reviews'], params)

    @classmethod
    def top_displayed_reviews(self, application_id, sort_type,params):
        """
        Application Top Displayed Reviews allows you to fetch all the top displayed reviews
        entries about a specific app on the App Store in the selected country and based on the given sort parameter.
        Classes by default the application's reviews by the Most Useful.
        With that endpoint you would be able to get the top displayed reviews for an application,
        based on that criterion.

        parameters
        ----------
        application_id : int
             an application id

        params : dict()
            the params keys are (country, size)

            country : ISO Alpha-2, reqiored !!! ANDROID
                defualt us

            size : int, optional
                default 100
                The number of reviews you want to fetch
        """
        Validation().params(params)
        required = ['language']
        Validation().require_params(params,required)
        return super().top_displayed_reviews(application_id, sort_type,params)

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
            the params keys are (country, min_rating, max_rating, start_date, end_date, term, from, size)

            language : ISO Alpha-2, required

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
        required = ['language']
        Validation().require_params(params, required)
        return super().filtered_reviews(application_id,params)


    @classmethod
    def keywords_trending(self, params = {}):
        raise Exception('Not implemented for this plateform')

    @classmethod
    def keywords_volume_history(self, params = {}):
        raise Exception('Not implemented for this plateform')
