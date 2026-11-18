from django.test import TestCase
import json
import unittest
import requests
import base
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Movie, StreamingChannel

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


class AdminWritePermissionTests(APITestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="consumer",
            password="test-password",
        )
        self.admin = user_model.objects.create_user(
            username="platform-manager",
            password="test-password",
            is_staff=True,
        )
        self.movie_data = {
            "title": "Movie",
            "director": "Director",
            "description": "Description",
        }

    def test_regular_user_cannot_create_update_or_delete_instances(self):
        movie = Movie.objects.create(**self.movie_data)
        channel = StreamingChannel.objects.create(name="Channel")
        self.client.force_authenticate(user=self.user)

        requests_to_check = (
            ("post", "/api/v1/movies/", self.movie_data),
            ("patch", f"/api/v1/movies/{movie.pk}/", {"title": "Updated"}),
            ("delete", f"/api/v1/movies/{movie.pk}/", None),
            ("post", "/api/v1/streaming-channel/", {"name": "New channel"}),
            (
                "patch",
                f"/api/v1/streaming-channel/{channel.pk}/",
                {"name": "Updated"},
            ),
            ("delete", f"/api/v1/streaming-channel/{channel.pk}/", None),
        )

        for method, url, data in requests_to_check:
            with self.subTest(method=method, url=url):
                request = getattr(self.client, method)
                response = request(url, data=data) if data is not None else request(url)
                self.assertEqual(403, response.status_code)

    def test_platform_manager_can_create_update_and_delete_instances(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post("/api/v1/movies/", self.movie_data)
        self.assertEqual(201, response.status_code)
        movie_id = response.data["id"]
        self.assertEqual(self.admin.pk, Movie.objects.get(pk=movie_id).owner_id)

        response = self.client.patch(
            f"/api/v1/movies/{movie_id}/",
            {"title": "Updated movie"},
        )
        self.assertEqual(200, response.status_code)
        response = self.client.delete(f"/api/v1/movies/{movie_id}/")
        self.assertEqual(204, response.status_code)

        response = self.client.post(
            "/api/v1/streaming-channel/",
            {"name": "Channel"},
        )
        self.assertEqual(201, response.status_code)
        channel_id = response.data["id"]
        response = self.client.patch(
            f"/api/v1/streaming-channel/{channel_id}/",
            {"name": "Updated channel"},
        )
        self.assertEqual(200, response.status_code)
        response = self.client.delete(f"/api/v1/streaming-channel/{channel_id}/")
        self.assertEqual(204, response.status_code)
