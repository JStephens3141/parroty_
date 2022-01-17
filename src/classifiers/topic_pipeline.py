import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

import pickle
from pathlib import Path

class TopicPipeline():
    # TODO: Datasets - Use scrapers/keywords/Social Media Pages/automated sources

    def __init__(self):
        self.environment = 'test'
        self.refresh_model = False
        home = str(Path.home())
        project_folder = r'\_parroty_workspace'
        output_folder = home + project_folder
        pipeline_filename = output_folder + r'\parroty_pipeline.pickle'

        #Load dataset
        #self.categories = ['alt.atheism','soc.religion.christian','comp.graphics', 'sci.med']
        self.twenty_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=11)
        test_data = fetch_20newsgroups(subset='test', shuffle=True, random_state=11)

        #pipeline cache
        # TODO: add check/creation step for project_folder
        
        if Path(pipeline_filename).is_file() and self.refresh_model == False:
            with open(pipeline_filename, 'rb') as input:
                self.text_clf = pickle.load(input)
            print('Pipeline Loaded!')
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

            with open(pipeline_filename, 'wb') as output:
                pickle.dump(self.text_clf, output)
            print('Pipeline Cached!')

        #self.docs = test_data.data#['God is love', 'OpenGL on the GPU is fast']
        #self.predict = self.text_clf.predict(self.docs)

        # for doc, category in zip(self.docs, self.predict):
        #     print('%r => %s' % (doc, twenty_train.target_names[category]))

        #Displays the mean correct prediction based on test dataset - will be meaningless for unknown values without manually tagging the data
        #print(np.mean(self.predict == test_data.target))

if __name__ == '__main__':
    pipeline = TopicPipeline()
