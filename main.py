"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from src.datasources.twitter.tweets import TweetDump
from src.datasources.twitter.twitter_handle_lookup import UserLookup
from src.classifiers.topic_pipeline import TopicPipeline

tweet_data = TweetDump()#UserLookup()
pipeline = TopicPipeline()

#docs is assembled in a for loop that iterates through each tweet scraped and places just the tweet text into a list
fieldnames = ['tweet', 'category']
docs = []#list(tweet_data.df['data'][0].values())#['Tweeter', 'Docs']
for tweet in tweet_data.df['data'][0]:
    docs.append(tweet['text'])
predict = pipeline.text_clf.predict(docs)
analysis_data = {'tweet':[], 'category':[]}
rows = [{'tweet': doc,
         'category': pipeline.twenty_train.target_names[category]
        } for doc, category in zip(docs, predict)]

#analysis_data = {'tweet':[docs], 'category':pipeline.twenty_train.target_names[category]}

def main():
  print('predict: ' + str(predict[0])
  print('rows: ' + rows[0])

    # TODO: The following dataframe needs to be fed into doc as a string of comma separated values in order to achieve large scale topic classification
    #print(tweet_data.df.data[0])#print(tweet_data.df.tail())
   ### for doc, category in zip(docs, predict):
        #pipeline.twenty_train.target_names[category]
        #analysis_data['tweet'].append(doc.copy())
        #analysis_data['category'].append(category.copy())
        #print('%r => %s' % (doc, pipeline.twenty_train.target_names[category]))
  print(analysis_data)        

    # TODO: Stretch Goal - Ask twitter a question/Generate a 'generalized' response
    # TODO: Analyze Data - Sentiment, Topic
    # TODO: Visualize Analysis - Word blob by sentiment


if __name__ == "__main__":
    main()
