"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from datasources.tweets import TweetDump
from datasources.twitter_handle_lookup import UserLookup
from classifiers.topic_pipeline import TopicPipeline

docs = ['Tweeter Docs']
tweet_data = TweetDump()#UserLookup()
pipeline = TopicPipeline()
predict = pipeline.text_clf.predict(docs)

def main():
    print(predict[0])

    # TODO: The following dataframe needs to be fed into doc as a string of comma separated values in order to achieve large scale topic classification
    #print(tweet_data.df.data[0])#print(tweet_data.df.tail())
    for doc, category in zip(docs, predict):
        print('%r => %s' % (doc, pipeline.twenty_train.target_names[category]))
        
    # TODO: Streth Goal - Ask twitter a question/Generate a 'generalized' response

    # TODO: Scrape twitter for data
    # TODO: Load data into classifier
    # TODO: Visualize Data


if __name__ == "__main__":
    main()
