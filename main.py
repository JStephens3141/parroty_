"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from datasources.tweets import TweetDump
from datasources.twitter_handle_lookup import UserLookup
from classifiers.topic_pipeline import TopicPipeline

tweet_data = TweetDump()#UserLookup()
pipeline = TopicPipeline()
docs = []#list(tweet_data.df['data'][0].values())#['Tweeter', 'Docs']
for tweet in tweet_data.df['data'][0]:
    docs.append(tweet['text'])
predict = pipeline.text_clf.predict(docs)

def main():
    print(predict[0])

    # TODO: The following dataframe needs to be fed into doc as a string of comma separated values in order to achieve large scale topic classification
    #print(tweet_data.df.data[0])#print(tweet_data.df.tail())
    for doc, category in zip(docs, predict):
        print('%r => %s' % (doc, pipeline.twenty_train.target_names[category]))
        
    # TODO: Stretch Goal - Ask twitter a question/Generate a 'generalized' response
    # TODO: Analyze Data - Sentiment, Topic
    # TODO: Visualize Analysis - Word blob by sentiment


if __name__ == "__main__":
    main()
