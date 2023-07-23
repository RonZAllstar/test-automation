import requests


# Class for commonly used functions
class MainMethods(object):

    found_dog = None

    @classmethod
    def fetch_sub_breed_for_specific_dog(cls, breed_type):
        print(f"Fetching list of sub breeds for {breed_type}")

        list_of_dogs_response = MainMethods.fetch_all_dog_breeds().json()['message']

        cls.found_dog = None
        #   we look for specific breed_type in response and return the sub-breeds that belong to it
        for dog in list_of_dogs_response:
            if breed_type in dog:
                sub_breed = list_of_dogs_response.get(breed_type)
                cls.found_dog = True
                return sub_breed
            else:
                cls.found_dog = False

        if not cls.found_dog:
            return False

    @classmethod
    def fetch_all_dog_breeds(cls):
        print("Fetching list of dog breeds")

        url = "https://dog.ceo/api/breeds/list/all"

        response = requests.request("GET", url=url)

        return response

    @classmethod
    def get_random_dog_image(cls, breed_type, sub_breed):
        print(f"Getting random {breed_type} image for {sub_breed}")

        # we pass in parameters to url for better re-usability
        url = f"https://dog.ceo/api/breed/{breed_type}/{sub_breed}/images/random"

        response = requests.request("GET", url)

        return response



