from django.test import TestCase
import json
import unittest
import requests
import base

# Create your tests here.
class NewVisitorTest(unittest.TestCase):
    def test_can_add_a_film_and_retrieve_it_later_then_delete(self):
        #FrankhasheardaboutanewcoolRESTfulWebApplicationon
        #whichyoucansaveyourfavouriteFilmandTvseries.
        #Hethinks
        #forawhile,thenrememberthewonderfulTvseriescalled
        #"Lupin",hewatchedonNetflix.
        #Createanewmovie
        movie={
            "title": "Lupin III",
            "subtitle": "Il castello di Cagliostro",
            "director": "Hayao Miyazaki",
            "description": "The Castle of Cagliostro follows gentleman thief Lupin III..."
        }

        post_response = requests.post(#è una create
            f"{base.api_urls}/movies/",
            json = movie #ci pensa già lui a fare dump(?)
        )

        pk = json.loads(post_response.content.decode("UTF-8"))['id']

        if __name__ == '__main__':
            unittest.main()


        self.assertEqual(201,post_response.status_code) #201=oggetto creato

        #dopo get su stesso endpoint
        #Afterthreemonths,Frankcan'trememberanymorethename of thatbeautifulmoviehewatched.Butheremembers
        #heused
        #tosavehisfavouriteonesontheWebAppaboutmovies.
        #Hegoestocheckoutthehomepage.
        #Andhereitis,LupinIII!
        get_response=requests.get(f"{base.api_url}/movies/")

        self.assertEqual(200,get_response.status_code) #oggetto trovato

        movie_list=get_response.json()
        self.assertIn(
            movie['title'],
            [movie['title']for movie in movie_list]
        )

        self.assertIn(
            movie['director'],
            [movie['director']for movie in movie_list]
        )

        self.assertIn(
            movie['description'],
            [movie['description']for movie in movie_list]
        )

        #Frank wants this film
        #no longer to be with in hisfavourites list, so he deletes it.
        delete_response=requests.delete(
            f"{base.api_url}/movies/{pk}/"
        )

        self.assertEqual(204,delete_response.status_code)
