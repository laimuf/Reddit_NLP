
import praw
import pandas as pd
from praw_credentials import client_id, client_secret, user_agent

reddit = praw.Reddit(client_id=client_id, 
        client_secret=client_secret, 
        user_agent=user_agent)

def _save_posts(posts):
    # Create table columns that we will fill
    posts_data = {
                    'created_utc': [], 
                    'title' : [], 
                    'score': [],
                    'num_comments': [],
                    'upvote_ratio': [], 
                    'nsfw' : [], 
                    'selftext': [],
    }

    for post in posts:
        posts_data['created_utc'].append(post.created_utc)
        posts_data['title'].append(post.title)
        posts_data['score'].append(post.score)
        posts_data['num_comments'].append(post.num_comments)
        posts_data['upvote_ratio'].append(post.upvote_ratio)
        posts_data['nsfw'].append(post.over_18)
        posts_data['selftext'].append(post.selftext)

    df = pd.DataFrame(posts_data)
    
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

    df.to_excel(f'{post_type}_{subreddit}_{limit}.xlsx')

    return df, posts


if __name__ == "__main__":

    subreddit = "mademesmile"
    post_type = 'hot'
    limit = 51

    df, posts = save_posts(subreddit=subreddit, post_type=post_type, limit=limit)
