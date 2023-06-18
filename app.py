import praw
import os
from datetime import datetime
import pandas as pd
from praw_credentials import client_id, client_secret, user_agent
from config import SUBREDDIT, POST_TYPES, LIMIT

reddit = praw.Reddit(client_id=client_id, 
        client_secret=client_secret, 
        user_agent=user_agent)

def _posts_to_df(posts):
    # Create table columns to fill
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
                reddit_subreddit=reddit.subreddit,
                timestamp=True,
                save_dir = "data/",):

    # Get the posts
    if post_type == 'hot':
        posts = reddit_subreddit(subreddit).hot(limit=limit)
    elif post_type == 'new':
        posts = reddit_subreddit(subreddit).new(limit=limit)
    elif post_type == 'top':
        posts = reddit_subreddit(subreddit).top(limit=limit)

    # Parse the posts into a dataframe
    df = _posts_to_df(posts)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if timestamp:
        # Get the current time
        now = datetime.now()
        # Format the datetime object as a string
        timestamp_str = now.strftime("_%Y_%m_%d_%H_%M_%S")
    else:
        timestamp_str = ""
    
    # Save the posts
    df.to_excel(f'{save_dir}{subreddit}_{post_type}_{limit}posts{timestamp_str}.xlsx')

    return df, posts


if __name__ == "__main__":

    for post_type in POST_TYPES:

        df, all_posts = save_posts(subreddit=SUBREDDIT, 
                                    post_type=post_type, 
                                    limit=LIMIT)
