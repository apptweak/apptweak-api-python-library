from apptweak import apptweak
import unittest
from unittest.mock import patch

@patch("apptweak.Ressource.http_request",return_value=True)
@patch("json.loads",return_value=True)
class TestPlateform(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_metadata(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.metadata(123,{'a':'b'}))
        self.assertTrue(apptweak.Ios.metadata(123))
        with self.assertRaises(Exception):
            apptweak.Ios.metadata({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.metadata()
        with self.assertRaises(Exception):
            apptweak.Ios.metadata(123,'string')
        #ANDROID
        self.assertTrue(apptweak.Android.metadata("com.company",{'a':'b'}))
        self.assertTrue(apptweak.Android.metadata("com.company"))
        with self.assertRaises(Exception):
            apptweak.Android.metadata({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.metadata()
        with self.assertRaises(Exception):
            apptweak.Android.metadata("com.company",'string')

    def test_ratings(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.ratings(123,{'a':'b'}))
        self.assertTrue(apptweak.Ios.ratings(123))
        with self.assertRaises(Exception):
            apptweak.Ios.ratings({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.ratings()
        with self.assertRaises(Exception):
            apptweak.Ios.ratings(123,'string')
        #ANDROID
        self.assertTrue(apptweak.Android.ratings("com.company",{'a':'b'}))
        self.assertTrue(apptweak.Android.ratings("com.company"))
        with self.assertRaises(Exception):
            apptweak.Android.ratings({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.ratings()
        with self.assertRaises(Exception):
            apptweak.Android.ratings("com.company",'string')

    def test_rankings(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.rankings(123,{'a':'b'}))
        self.assertTrue(apptweak.Ios.rankings(123))
        with self.assertRaises(Exception):
            apptweak.Ios.rankings({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.rankings()
        with self.assertRaises(Exception):
            apptweak.Ios.rankings(123,'string')
        #ANDROID
        self.assertTrue(apptweak.Android.rankings("com.company",{'country':'us'}))
        with self.assertRaises(Exception):
            apptweak.Android.rankings("com.company",{'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.rankings("com.company")
        with self.assertRaises(Exception):
            apptweak.Android.rankings({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.rankings()
        with self.assertRaises(Exception):
            apptweak.Android.rankings("com.company",'string')

    def test_power(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.power(app_id,{'country':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.power(app_id)
        with self.assertRaises(Exception):
            apptweak.Ios.power(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Ios.power({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.power()
        with self.assertRaises(Exception):
            apptweak.Ios.power(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.power(app_id,{'country':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.power(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.power(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.power({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.power()
        with self.assertRaises(Exception):
            apptweak.Android.power(app_id,'string')

    def test_backlinks(self, mock_load, mock_res):
        #IOS
        app_id = 123
        with self.assertRaises(Exception):
            apptweak.Ios.backlinks(app_id)
        with self.assertRaises(Exception):
            apptweak.Ios.backlinks(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Ios.backlinks({'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Ios.backlinks()
        with self.assertRaises(Exception):
            apptweak.Ios.backlinks(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.backlinks(app_id))
        self.assertTrue(apptweak.Android.backlinks(app_id),{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.backlinks({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.backlinks()
        with self.assertRaises(TypeError):
            apptweak.Android.backlinks(app_id,'string')

    def test_downloads(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.downloads(app_id,{'a':'b'}))
        self.assertTrue(apptweak.Ios.downloads(app_id))
        with self.assertRaises(Exception):
            apptweak.Ios.downloads({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.downloads()
        with self.assertRaises(Exception):
            apptweak.Ios.downloads(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.downloads(app_id,{'a':'b'}))
        self.assertTrue(apptweak.Android.downloads(app_id))
        with self.assertRaises(Exception):
            apptweak.Android.downloads({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.downloads()
        with self.assertRaises(Exception):
            apptweak.Android.downloads(app_id,'string')

    def test_revenues(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.revenues(app_id,{'a':'b'}))
        self.assertTrue(apptweak.Ios.revenues(app_id))
        with self.assertRaises(Exception):
            apptweak.Ios.revenues({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.revenues()
        with self.assertRaises(Exception):
            apptweak.Ios.revenues(app_id,'string')
        #ANDROID
        app_id = "com.company"
        with self.assertRaises(Exception):
            apptweak.Android.revenues(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.revenues(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.revenues({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.revenues()
        with self.assertRaises(Exception):
            apptweak.Android.revenues(app_id,'string')

    def test_reviews(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.reviews(app_id,{'a':'b'}))
        self.assertTrue(apptweak.Ios.reviews(app_id))
        with self.assertRaises(Exception):
            apptweak.Ios.reviews({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.reviews()
        with self.assertRaises(Exception):
            apptweak.Ios.reviews(app_id,'string')
        #ANDROID
        app_id = "com.company"
        with self.assertRaises(Exception):
            apptweak.Android.reviews(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.reviews(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.reviews({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.reviews()
        with self.assertRaises(Exception):
            apptweak.Android.reviews(app_id,'string')

    def test_searches(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.searches({'term':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.searches(app_id)
        with self.assertRaises(Exception):
            apptweak.Ios.searches("string")
        with self.assertRaises(TypeError):
            apptweak.Ios.searches()
        with self.assertRaises(TypeError):
            apptweak.Ios.searches(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.searches({'term':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.searches(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.searches({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.searches()
        with self.assertRaises(TypeError):
            apptweak.Android.searches(app_id,'string')

    def test_top_charts(self, mock_load, mock_res):
        #IOS
        cat_id = 123
        self.assertTrue(apptweak.Ios.top_charts(cat_id,{'a':'b'}))
        self.assertTrue(apptweak.Ios.top_charts(cat_id))
        with self.assertRaises(Exception):
            apptweak.Ios.top_charts({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.top_charts()
        with self.assertRaises(Exception):
            apptweak.Ios.top_charts(cat_id,'string')
        #ANDROID
        cat_id = "GAME"
        self.assertTrue(apptweak.Android.top_charts(cat_id,{'a':'b'}))
        self.assertTrue(apptweak.Android.top_charts(cat_id))
        with self.assertRaises(Exception):
            apptweak.Android.top_charts({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.top_charts()
        with self.assertRaises(Exception):
            apptweak.Android.top_charts(cat_id,'string')

    def test_top_displayed_reviews(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.top_displayed_reviews(app_id,'most_useful',{'a':'b'}))
        self.assertTrue(apptweak.Ios.top_displayed_reviews(app_id,'most_useful'))
        with self.assertRaises(Exception):
            apptweak.Ios.top_displayed_reviews(app_id,'most_us')
        with self.assertRaises(TypeError):
            apptweak.Ios.top_displayed_reviews(app_id)
        with self.assertRaises(TypeError):
            apptweak.Ios.top_displayed_reviews()
        with self.assertRaises(Exception):
            apptweak.Ios.top_displayed_reviews(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Ios.top_displayed_reviews(app_id,'most_useful','string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.top_displayed_reviews(app_id,'most_useful',{'language':'us'}))
        with self.assertRaises(TypeError):
            apptweak.Android.top_displayed_reviews(app_id,'most_useful')
        with self.assertRaises(Exception):
            apptweak.Android.top_displayed_reviews(app_id,'most_us',{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.top_displayed_reviews(app_id,'most_us')
        with self.assertRaises(TypeError):
            apptweak.Android.top_displayed_reviews(app_id)
        with self.assertRaises(TypeError):
            apptweak.Android.top_displayed_reviews()
        with self.assertRaises(Exception):
            apptweak.Android.top_displayed_reviews(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.top_displayed_reviews(app_id,'most_useful','string')

    def test_filtered_reviews(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.filtered_reviews(app_id,{'term':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.filtered_reviews({'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Ios.filtered_reviews(app_id,{'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.filtered_reviews()
        with self.assertRaises(Exception):
            apptweak.Ios.filtered_reviews(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.filtered_reviews(app_id,{'language':'en','term':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.filtered_reviews(app_id,{'term':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.filtered_reviews({'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.filtered_reviews(app_id,{'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.filtered_reviews()
        with self.assertRaises(Exception):
            apptweak.Android.filtered_reviews(app_id,'string')

    def test_review_stats(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.review_stats(app_id))
        self.assertTrue(apptweak.Ios.review_stats(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.review_stats({'a':'b'})

        with self.assertRaises(TypeError):
            apptweak.Ios.review_stats()
        with self.assertRaises(Exception):
            apptweak.Ios.review_stats(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.review_stats(app_id))
        self.assertTrue(apptweak.Android.review_stats(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.review_stats({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.review_stats()
        with self.assertRaises(Exception):
            apptweak.Android.review_stats(app_id,'string')

    def test_app_top_keywords(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.app_top_keywords(app_id))
        self.assertTrue(apptweak.Ios.app_top_keywords(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.app_top_keywords({'a':'b'})

        with self.assertRaises(TypeError):
            apptweak.Ios.app_top_keywords()
        with self.assertRaises(Exception):
            apptweak.Ios.app_top_keywords(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.app_top_keywords(app_id))
        self.assertTrue(apptweak.Android.app_top_keywords(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.app_top_keywords({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.app_top_keywords()
        with self.assertRaises(Exception):
            apptweak.Android.app_top_keywords(app_id,'string')

    def test_keywords_stats(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.keywords_stats({'keywords':['a']}))
        self.assertTrue(apptweak.Ios.keywords_stats({'keywords':['a','b']}))
        with self.assertRaises(TypeError):
            self.assertTrue(apptweak.Ios.keywords_stats())
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_stats({'keyword':['a','b']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_stats({'keywords':['a','b','a','b','a','b','a','b','9','10','11']}))
        #ANDROID
        self.assertTrue(apptweak.Android.keywords_stats({'keywords':['a']}))
        self.assertTrue(apptweak.Android.keywords_stats({'keywords':['a','b']}))
        with self.assertRaises(TypeError):
            self.assertTrue(apptweak.Android.keywords_stats())
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Android.keywords_stats({'keyword':['a','b']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Android.keywords_stats({'keywords':['a','b','a','b','a','b','a','b','9','10','11']}))

    def test_keywords_competitors(self, mock_load, mock_res):
        #IOS
        app_id = 123
        self.assertTrue(apptweak.Ios.keywords_competitors(app_id))
        self.assertTrue(apptweak.Ios.keywords_competitors(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.keywords_competitors({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.keywords_competitors()
        with self.assertRaises(Exception):
            apptweak.Ios.keywords_competitors(app_id,'string')
        #ANDROID
        app_id = "com.company"
        self.assertTrue(apptweak.Android.keywords_competitors(app_id))
        self.assertTrue(apptweak.Android.keywords_competitors(app_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.keywords_competitors({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.keywords_competitors()
        with self.assertRaises(Exception):
            apptweak.Android.keywords_competitors(app_id,'string')

    def test_keywords_ranking_competitors(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keywords':['a'],'applications':[12]}))
        self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keywords':['a','b'],'applications':[12,13]}))
        with self.assertRaises(TypeError):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors())
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keyword':['a','b']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keywords':['a','b','a','b','a','b','a','b','9','10','11']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'applcations':[1,2]}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'applications':[5,4,3,2,1,6]}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keywords':['a','b','a','b','a','b','a','b','9','10','11'],'applications':[1,2]}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keyword':['a','b'],'applications':[5,4,3,2,1,6]}))
        #ANDROID
        self.assertTrue(apptweak.Android.keywords_ranking_competitors({'keywords':['a'],'applications':['12']}))
        self.assertTrue(apptweak.Android.keywords_ranking_competitors({'keywords':['a','b'],'applications':['12','13']}))
        with self.assertRaises(TypeError):
            self.assertTrue(apptweak.Android.keywords_ranking_competitors())
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Android.keywords_ranking_competitors({'keyword':['a','b']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Android.keywords_ranking_competitors({'keywords':['a','b','a','b','a','b','a','b','9','10','11']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'applcations':['1','2']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'applications':['a','b','a','b','a','b','a']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keywords':['a','b','a','b','a','b','a','b','9','10','11'],'applications':['a','b']}))
        with self.assertRaises(Exception):
            self.assertTrue(apptweak.Ios.keywords_ranking_competitors({'keyword':['a','b'],'applications':['5','4','3','2','1','6']}))

    def test_category_top_keywords(self, mock_load, mock_res):
        #IOS
        cat_id = 123
        self.assertTrue(apptweak.Ios.category_top_keywords(cat_id))
        self.assertTrue(apptweak.Ios.category_top_keywords(cat_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.category_top_keywords({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Ios.category_top_keywords()
        with self.assertRaises(Exception):
            apptweak.Ios.category_top_keywords(cat_id,'string')
        #ANDROID
        cat_id = "com.company"
        self.assertTrue(apptweak.Android.category_top_keywords(cat_id))
        self.assertTrue(apptweak.Android.category_top_keywords(cat_id,{'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Android.category_top_keywords({'a':'b'})
        with self.assertRaises(TypeError):
            apptweak.Android.category_top_keywords()
        with self.assertRaises(Exception):
            apptweak.Android.category_top_keywords(cat_id,'string')

    def test_keywords_trending(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.keywords_trending())
        self.assertTrue(apptweak.Ios.keywords_trending({'a':'b'}))
        with self.assertRaises(Exception):
            apptweak.Ios.keywords_trending('string')
        #ANDROID
        app_id = "com.company"
        with self.assertRaises(Exception):
            apptweak.Android.keywords_trending(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.keywords_trending(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.keywords_trending({'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.keywords_trending()
        with self.assertRaises(Exception):
            apptweak.Android.keywords_trending(app_id,'string')


    def test_keywords_volume_history(self, mock_load, mock_res):
        #IOS
        self.assertTrue(apptweak.Ios.keywords_volume_history({'keywords':['b']}))
        with self.assertRaises(Exception):
            apptweak.Ios.keywords_volume_history({'keywrds':['b']})
        with self.assertRaises(TypeError):
            apptweak.Ios.keywords_volume_history()
        with self.assertRaises(Exception):
            apptweak.Ios.keywords_trending('string')
        #ANDROID
        app_id = "com.company"
        with self.assertRaises(Exception):
            apptweak.Android.keywords_volume_history(app_id,{'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.keywords_volume_history(app_id)
        with self.assertRaises(Exception):
            apptweak.Android.keywords_volume_history({'a':'b'})
        with self.assertRaises(Exception):
            apptweak.Android.keywords_volume_history()
        with self.assertRaises(Exception):
            apptweak.Android.keywords_volume_history(app_id,'string')


if __name__ == '__main__':
    unittest.main()
