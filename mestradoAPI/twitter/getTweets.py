import GetOldTweets3 as got
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import random as sparse_random


from gensim.test.utils import common_texts
from gensim.models import Word2Vec

# print(common_texts)
common_texts = [['gato','comeu','rato','felino','comeu','roedor']]
model = Word2Vec(sentences=common_texts, size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")

model = Word2Vec.load("word2vec.model")
model.train(common_texts, total_examples=1, epochs=1)

vector = model.wv['rato']

print(model.wv.most_similar('rato'))







# #No sklearn você consegue transformar as sentenças em bag of words usanod o CountVectorizer
# #E depois, fazer o LSA usando o TruncatedSVC, onde o número de dimensões é o tamanho de representação
# #E pra encontrar os sinônimos você pode usar o NearestNeighbors
# def sinonimos():
#     text = ["", "John é um bom garoto. John sempre assiste futebol."]
#     vectorizer = CountVectorizer()
#     # tokenize and build vocab
#     vectorizer = vectorizer.fit(text)
#     # encode document
#     vector = vectorizer.transform(text)
#     svdT = TruncatedSVD(n_components=5, n_iter=7, random_state=42)
#     svdTFit = svdT.fit_transform(vector)
#
#     nbrs = NearestNeighbors(n_neighbors=1)
#     nbrs.fit(svdTFit)
#     # print(nbrs.kneighbors(svdTFit))
#
#     distances, indices = nbrs.kneighbors(svdTFit)
#     # print(distances)
#     # print(indices)
#
#     print(nbrs.kneighbors_graph(svdTFit).toarray())



# sinonimos()

def username_tweets_to_csv(username, count):
    print("elo")
#     tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama whitehouse").setMaxTweets(2)
#     tweets = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    # print(tweets.text)

    # user_tweets = [[tweet.date, tweet.text] for tweet in tweets]
    # print(user_tweets)
    #
    # \<\s*div\s*class\s*=\"dir-ltr\"\s*dir=\"ltr\"\s*>(.+?)(?=\<\/div\>)
    #
    # < div class ="dir-ltr" dir="ltr" > </div>

    # # Creation of query object
    # tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count)
    # # Creation of list that contains all tweets
    # tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    #
    # user_tweets = [tweet.text + " " for tweet in tweets]

    # Creating list of chosen tweet data
    # user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    # tweets_df = pd.DataFrame(user_tweets, columns=['Datetime', 'Text'])

    # Converting dataframe to CSV
    # tweets_df.to_csv('{}-{}k-tweets.csv'.format(username, int(count / 1000)), sep=',')

# username = 'pryscila02_'
# count = 5

# Calling function to turn username's past x amount of tweets into a CSV file
# username_tweets_to_csv(username, count)