from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import pickle
from pathlib import Path

class TopicPipeline():

    def __init__(self):
        environment = 'test'
        self.home = str(Path.home())
        self.project_folder = r'\_parroty_workspace'
        self.output_folder = self.home + self.project_folder
        self.pipeline_filename = self.output_folder + r'\parroty_pipeline.pickle'

        #Load dataset
        # TODO: add all categories
        self.categories = ['alt.atheism','soc.religion.christian','comp.graphics', 'sci.med']
        self.twenty_train = fetch_20newsgroups(subset='train', categories=self.categories, shuffle=True, random_state=42)

        #pipeline cache
        # TODO: add check/creation step for self.project_folder
        if Path(self.pipeline_filename).is_file():
            print('Pipeline Cached!')
            with open(self.pipeline_filename, 'rb') as input:
                self.text_clf = pickle.load(input)
        else:
            #Tokenizing Text
            self.count_vect = CountVectorizer()

            self.tfidf_transformer = TfidfTransformer()

            self.text_clf = Pipeline([
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', MultinomialNB())
            ])

            self.text_clf.fit(self.twenty_train.data, self.twenty_train.target)

            with open(self.pipeline_filename, 'wb') as output:
                pickle.dump(self.text_clf, output)

        # docs_new = ['God is love', 'OpenGL on the GPU is fast']
        # predicted_pipeline = self.text_clf.predict(docs_new)

        # for doc, category in zip(docs_new, predicted_pipeline):
        #     print('%r => %s' % (doc, self.twenty_train.target_names[category]))

if __name__ == '__main__':
    pip = TopicPipeline()
