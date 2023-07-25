import json
import unittest
import HTMLTestRunner
import main_methods
import dog_list


class TestDogBreeds(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.methods = main_methods.MainMethods()

    ################
    # Tests Here
    ################
    def test_list_of_dog_breeds(self):
        print("Validating all breed types")

        list_of_dog_breeds_response = self.methods.fetch_all_dog_breeds()
        self.assertEqual(200, list_of_dog_breeds_response.status_code, "ERROR: Failed to fetch list of dogs!")
        data = open('../Test_Data/list_of_dogs.json')
        fixed_dog_list = json.load(data)

        # we compare response against our json file
        print("Compare list of dogs from response to our fixed list")
        self.assertEqual(list_of_dog_breeds_response.json()['message'], fixed_dog_list, "ERROR: Dog list do not match!")

        data.close()

    def test_retriever_is_in_dog_list(self):
        print("Validate retriever is in dog list")
        breed_type = "retriever"

        # method for validating dog breeds
        self.validate_list_of_dog_breeds(breed_type)

    def test_list_of_sub_breeds_for_retriever(self):
        print("Testing sub breed for retriever")
        breed_type = 'retriever'

        # method for validating sub breeds
        self.validate_list_of_sub_dog_breeds(breed_type)

    def test_random_image_for_golden_sub_breed(self):
        print("Test random image/link for golden sub breed")
        breed_type = 'retriever'
        sub_breed = 'golden'

        self.validate_dog_image(breed_type, sub_breed)

    #######################
    # Test Validations Here
    #######################
    def validate_list_of_dog_breeds(self, breed_type):
        print(f"Validating {breed_type} in list of dog breeds")

        list_of_dog_breeds = self.methods.fetch_all_dog_breeds()

        breed_found = False
        # we go through all elements in response and check for 'breed_type'
        for x in list_of_dog_breeds.json()['message']:
            if breed_type in x:
                breed_found = True

        if breed_found:
            print(f"PASSED: {breed_type} found!")
        else:
            self.fail(f"ERROR: {breed_type} NOT found!")

    def validate_list_of_sub_dog_breeds(self, breed_type):
        print(f"Validating sub_breeds for {breed_type}")

        list_of_sub_breeds_response = self.methods.fetch_sub_breed_for_specific_dog(breed_type)
        fixed_list_of_sub_breeds_list = dog_list.DogList.list_of_dogs()[breed_type]

        # we compare our fixed list against api response
        self.assertEqual(fixed_list_of_sub_breeds_list, list_of_sub_breeds_response, f"ERROR: Sub-breed for "
                                                                                     f"{breed_type} does not match!")
        # fail if breed_type is not in response
        if not list_of_sub_breeds_response:
            self.fail("ERROR: Could not find dog!")

    def validate_dog_image(self, breed_type, sub_breed):
        print(f"Validating random {breed_type} image for {sub_breed}")

        response = self.methods.get_random_dog_image(breed_type, sub_breed)
        self.assertEqual(200, response.status_code, f"ERROR: Failed to get random image for {sub_breed} {breed_type}")

        #   we could also validate image name if required

        return response


if __name__ == '__main__':
    HTMLTestRunner.main()















