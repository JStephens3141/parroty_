"""
A general purpose classifier pipeline to predict tweet sentiment by 'Topic'
"""


from ast import And
from src.datasources.twitter.tweets import TweetDump
from src.datasources.twitter.twitter_handle_lookup import UserLookup
from src.classifiers.topic_pipeline import TopicPipeline

from pathlib import Path
import csv

force_analysis_creation = False

home = str(Path.home())
project_folder = r'\_parroty_workspace'
output_folder = home + project_folder
analysis_csv = Path(output_folder + r'\output.csv')

if analysis_csv.exists() and not force_analysis_creation:
  with analysis_csv.open('r', newline='') as _file:
    dict_reader = csv.DictReader(_file)
    analysis_data = [row for row in dict_reader]
  print('analysis loaded!')
else:
  tweet_data = TweetDump()
  pipeline = TopicPipeline()
  #docs is assembled in a for loop that iterates through
  #each tweet scraped and places just the tweet text into a list
  docs = []
  #the following should be moved into the tweet_data object as tweet_data.docs.
  #Code  can then be revised to docs = tweet_data.docs
  for tweet in tweet_data.df['data'][0]:
      docs.append(tweet['text'])
  predict = pipeline.text_clf.predict(docs)

  analysis_data = [{'tweet': doc,
                    'category': pipeline.twenty_train.target_names[category]
                   } for doc, category in zip(docs, predict)]
  print('Analysis created!')

  fieldnames = ['tweet', 'category']
  with analysis_csv.open('w', encoding='utf-8') as _file:
    csv_writer = csv.DictWriter(_file, fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(analysis_data)


def main():
  print('Analysis Data: ' + str(analysis_data[0]))
  ##File TODOs
  # TODO: load csv to dataframe instead of list/dicts 
  # TODO: Create 'cache' tool to pass a file and hold the 'if it exists load it, else create and write to it logic
  
  ##Project TODOs
  # TODO: Stretch Goal - Ask twitter a question/Generate a 'generalized' response
  # TODO: Analyze Data - Sentiment, Topic
  # TODO: Visualize Analysis - Word blob by sentiment


if __name__ == "__main__":
    main()
