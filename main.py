"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from datasources.tweets import TweetDump
from datasources.twitter_handle_lookup import UserLookup
from classifiers.topic_pipeline import TopicPipeline

tweet_data = TweetDump()#UserLookup()
pipeline = TopicPipeline()

def main():
    print(tweet_data.df.data[0])#print(tweet_data.df.tail())
# TODO: Streth Goal - Ask twitter a question/Generate a 'generalized' response

# TODO: Scrape twitter for data
# TODO: Load data into classifier
# TODO: Visualize Data

if __name__ == "__main__":
    main()
