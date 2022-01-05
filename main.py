"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from datasources.tweets import TweetDump
from classifiers.topic_pipeline import TopicPipeline

tweet_data = TweetDump()
pipeline = TopicPipeline()

def main():
    ''
# TODO: Streth Goal - Ask twitter a question/Generate a 'generalized' response

# TODO: Scrape twitter for data
# TODO: Load data into classifier
# TODO: Visualize Data

if __name__ == "__main__":
    main()
