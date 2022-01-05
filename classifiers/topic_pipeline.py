import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

import pickle
from pathlib import Path

class TopicPipeline():
    # TODO: Refresh Dataset - Use scrapers/keywords/Social Media Pages/automated sources
    # TODO: Train Model with ALL categories

    def __init__(self):
        environment = 'test'
        self.home = str(Path.home())
        self.project_folder = r'\_parroty_workspace'
        self.output_folder = self.home + self.project_folder
        self.pipeline_filename = self.output_folder + r'\parroty_pipeline.pickle'

        #Load dataset
        # TODO: add all categories
        self.categories = ['alt.atheism','soc.religion.christian','comp.graphics', 'sci.med']
        self.twenty_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42)
        self.test_data = fetch_20newsgroups(subset='test', shuffle=True, random_state=42)

        #pipeline cache
        # TODO: add check/creation step for self.project_folder
        # TODO: add a 'Force Refresh' flag that checks if a model should be dumped or kept in cache
        
        if Path(self.pipeline_filename).is_file():
            print('Pipeline Loaded!')
            with open(self.pipeline_filename, 'rb') as input:
                self.text_clf = pickle.load(input)
        else:
            #Tokenizing Text
            self.count_vect = CountVectorizer()

            self.tfidf_transformer = TfidfTransformer()

            self.text_clf = Pipeline([
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                      alpha=1e-3, random_state=42,
                                      max_iter=5, tol=None))
            ])

            self.text_clf.fit(self.twenty_train.data, self.twenty_train.target)

            with open(self.pipeline_filename, 'wb') as output:
                pickle.dump(self.text_clf, output)
                print('Pipeline Cached!')

        self.docs = self.test_data.data#['God is love', 'OpenGL on the GPU is fast']
        self.predict = self.text_clf.predict(self.docs)

        # for doc, category in zip(self.docs, self.predict):
        #     print('%r => %s' % (doc, self.twenty_train.target_names[category]))

        print(np.mean(self.predict == self.test_data.target))

if __name__ == '__main__':
    pipeline = TopicPipeline()
