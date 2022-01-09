import pandas as pd
import requests

import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

class UserLookup():

    def __init__(self):
        self.bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEk1RAEAAAAAzjosLGY5ZBoI2510JOg0eZqgPGA%3DTITTljCJgajS4IbV0sUKVysU8KggUUVMYAEgfbpxOATsQPKKYZ'#os.environ.get("BEARER_TOKEN")
        url = self.create_url()
        json_response = self.connect_to_endpoint(url)
        self.df = pd.json_normalize(json_response)


    def create_url(self):
        # Replace with user ID below
        usernames = 'usernames=SenatorBaldwin,SenJohnBarrasso'#list, of, usernames'
        user_fields = 'user.fields=description,created_at'
        return "https://api.twitter.com/2/users/by/?{}&{}".format(usernames, user_fields) #"https://api.twitter.com/2/users/{}/tweets".format(user_id)


    #Probably insecure, remove 'self' by passing bearer token as a param
    def bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "parroty_test"
        return r


    def connect_to_endpoint(self, url):
        
        response = requests.request("GET", url, auth=self.bearer_oauth)
        print('Response Status: ' + str(response.status_code))
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

if __name__ == '__main__':
    dump = UserLookup()