from pandas.core.construction import sanitize_array
import pandas as pd
import requests

import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

class TweetDump():

    def __init__(self):
        self.bearer_token = 'AAAAAAAAAAAAAAAAAAAAAEk1RAEAAAAAzjosLGY5ZBoI2510JOg0eZqgPGA%3DTITTljCJgajS4IbV0sUKVysU8KggUUVMYAEgfbpxOATsQPKKYZ'#os.environ.get("BEARER_TOKEN")
        url = self.create_url()
        params = self.get_params()
        json_response = self.connect_to_endpoint(url, params)
        self.df = pd.json_normalize(json_response)


    def create_url(self):
        # Replace with user ID below
        user_id = 1037321378
        return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

    def get_params(self):
        # Tweet fields are adjustable.
        # Options include:
        # attachments, author_id, context_annotations,
        # conversation_id, created_at, entities, geo, id,
        # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
        # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
        # source, text, and withheld
        return {"tweet.fields": "created_at", "max_results": "5"}#, "pagination_token": "7140dibdnow9c7btw3z3al3eejvt8zgiv6ko889o8zfhu", "max_results": "5"}

    def bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r


    def connect_to_endpoint(self, url, params):
        response = requests.request("GET", url, auth=self.bearer_oauth, params=params)
        print('Response Status: ' + str(response.status_code))
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

if __name__ == '__main__':
    dump = TweetDump()