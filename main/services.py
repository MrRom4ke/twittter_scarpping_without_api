import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date


def get_username(urls):
    names = []
    for elem in urls.split():
        names.append(elem.split("/")[-1])
    return names


def get_main_info(names):
    main_info = []
    for elem in names:
        for info in sntwitter.TwitterSearchScraper(f'(from:{elem})').get_items():
            main_info.append([info.user.username,
                              info.user.followersCount,
                              info.user.friendsCount,
                              info.user.description])
            break
    df = pd.DataFrame(main_info, columns=['User', 'Followers', 'Friends', 'Descriptions'])
    df['User'] = df['User'].apply(lambda x: f'<a href="/tweets/{x}">{x}</a>')
    mydict = {'df_main': df.to_html(escape=False)}
    return mydict


def get_tweets(username):
    current_date = date.today()
    query = f'(from:{username}) until:{current_date}'
    tweets = []
    limit = 10
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.user.username,
                           tweet.content,
                           tweet.date
                           ])
    df = pd.DataFrame(tweets, columns=['User', 'Tweet', 'Date'])
    df = df.replace(r'\r+|\n+|\t+', '', regex=True)
    return df.to_html()
