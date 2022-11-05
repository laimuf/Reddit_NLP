
import praw
import pandas as pd
from praw_credentials import client_id, client_secret, user_agent

reddit = praw.Reddit(client_id=client_id, 
        client_secret=client_secret, 
        user_agent=user_agent)

def _save_posts(posts):
    # Create table columns that we will fill
    columns = ['created_utc', 'Title','score','num_comments', 
                'Upvote_ratio','NSFW', 'selftext', 'link_flair_css_class']
    df = pd.DataFrame(columns=columns)

    for post in posts:
        print(post.title)
        row_to_add = {'created_utc': post.created_utc, 
                    'Title' : post.title, 
                    'score': post.score,
                    'num_comments': post.num_comments,
                    'upvote_ratio': post.upvote_ratio, 
                    'NSFW' :post.over_18, 
                    'selftext': post.selftext,
                    'link_flair_css_class:': post.link_flair_css_class}
        df = pd.concat([df, pd.DataFrame(row_to_add, index=[0])])
    
    df.to_csv('hotpost_Muslim_data.csv')
    return df


def save_posts(subreddit, 
                post_type, 
                limit=50, 
                reddit_subreddit=reddit.subreddit):

    if post_type == 'hot':
        posts = reddit_subreddit(subreddit).hot(limit=limit)
        df = _save_posts(posts)
        
    elif post_type == 'new':
        posts = reddit_subreddit(subreddit).new(limit=limit)
        df = _save_posts(posts)

    return df, posts

df, posts = save_posts("exmuslim", post_type='hot', limit=1)


