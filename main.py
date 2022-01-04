"""
A general purpose classifier pipeline to classify tweet sentiment by 'News Topic'
"""


from datasources.tweets import TweetDump
from classifiers.topic_pipeline import TopicPipeline

tweet_data = TweetDump()
pipeline = TopicPipeline()

def main():
    print(tweet_data, pipeline)
# TODO: Streth Goal - Ask twitter a question/Generate a 'generalized' response

# TODO: Scrape twitter for data
# TODO: Load data into classifier
# TODO: Visualize Data
#    df = tweets()


if __name__ == "__main__":
    main()
