import nltk
from nltk.corpus import movie_reviews
from nltk import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

def extract_features(words):
    return dict([(word,True) for word in words])

def sentiment_score_analyser(text):
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')
    
    features_pos = [(extract_features(movie_reviews.words(fileids=[f])),'Positive') for f in fileids_pos]
    features_neg = [(extract_features(movie_reviews.words(fileids=[f])),'Negative') for f in fileids_neg]
    
    threshold = 0.8
    num_pos = int(threshold*len(features_pos))
    num_neg = int(threshold*len(features_neg))
    
    #now making the training and testing data for classification of th model
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]
    
    #incase need to  print number of training datapoints :len(features_train)
    #incase want print number of test datapoints :len(features_test)
    classifier = NaiveBayesClassifier.train(features_train)
    
    probabilities = classifier.prob_classify(extract_features(text.split()))
    
    predicted_sentiment = probabilities.max()
    #print("Acccuracy Level",nltk_accuracy(classifier,features_test))
    #print("Probability",round(probabilities.prob(predicted_sentiment),2))

    #the final sentiment analysed data though not such Good indicates some sense
    return predicted_sentiment