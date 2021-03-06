# This script uses your bearer token to authenticate and retrieve the specified Tweet objects (by List ID)

require 'json'
require 'typhoeus'

# The code below sets the bearer token from your environment variables
# To set environment variables on Mac OS X, run the export command below from the terminal:
# export BEARER_TOKEN='YOUR-TOKEN'
bearer_token = ENV["BEARER_TOKEN"]

# Be sure to replace list-id with any List ID
id = "list-id"
url = "https://api.twitter.com/2/lists/#{id}/tweets"


params = {
  # Tweet fields are adjustable.
  # Options include:
  # attachments, author_id, context_annotations,
  # conversation_id, created_at, entities, geo, id,
  # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
  # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
  # source, text, and withheld
  "tweet.fields": "lang,author_id",
}

def list_tweets(url, bearer_token, params)
  options = {
    method: 'get',
    headers: {
      "User-Agent": "v2ListTweetsLookupRuby",
      "Authorization": "Bearer #{bearer_token}"
    },
    params: params
  }

  request = Typhoeus::Request.new(url, options)
  response = request.run

  return response
end

response = list_tweets(url, bearer_token, params)
puts response.code, JSON.pretty_generate(JSON.parse(response.body))
