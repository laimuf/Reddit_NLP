import praw
import os
from datetime import datetime
import pandas as pd
from credentials import praw_client_id, praw_client_secret, praw_user_agent
from config import SUBREDDIT, POST_TYPES, LIMIT
from praw.models import MoreComments
from tqdm import tqdm

reddit = praw.Reddit(client_id=praw_client_id, 
        client_secret=praw_client_secret, 
        user_agent=praw_user_agent)

def _posts_to_df(posts, fetch_comments):
    # Create table columns to fill
    posts_data = {
                    'created_utc': [], 
                    'title' : [], 
                    'score': [],
                    'num_comments': [],
                    'upvote_ratio': [], 
                    'nsfw' : [], 
                    'selftext': [],
                    'author': [],
                    'url': [],
                    'top_level_coments': [],
                    
    }

    for post in tqdm(posts):
        if fetch_comments:
            top_level_coments = [(comment.author, comment.body) for comment in post.comments  if not isinstance(comment, MoreComments)]
        else:
            top_level_coments = []
        posts_data['created_utc'].append(post.created_utc)
        posts_data['title'].append(post.title)
        posts_data['score'].append(post.score)
        posts_data['num_comments'].append(post.num_comments)
        posts_data['upvote_ratio'].append(post.upvote_ratio)
        posts_data['nsfw'].append(post.over_18)
        posts_data['selftext'].append(post.selftext)
        posts_data['author'].append(post.author)
        posts_data['url'].append(post.url)
        posts_data['top_level_coments'].append(top_level_coments)
        

    df = pd.DataFrame(posts_data)
    
    return df


def save_posts(subreddit, 
                post_type, 
                limit, 
                reddit_subreddit=reddit.subreddit,
                timestamp=True,
                save_dir = "data/",
                fetch_comments=False):

    # Get the posts
    if post_type == 'hot':
        posts = reddit_subreddit(subreddit).hot(limit=limit)
    elif post_type == 'new':
        posts = reddit_subreddit(subreddit).new(limit=limit)
    elif post_type == 'top':
        posts = reddit_subreddit(subreddit).top(limit=limit)

    # Parse the posts into a dataframe
    df = _posts_to_df(posts, fetch_comments=fetch_comments)

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
    if limit is None:
        limit = "all"
    save_reddit_data_to = f'{save_dir}{subreddit}_{post_type}_{limit}_posts{timestamp_str}.xlsx'
    print(f"{save_reddit_data_to = }")
    df.to_excel(save_reddit_data_to)

    return df, posts


if __name__ == "__main__":

    for post_type in POST_TYPES:

        df, all_posts = save_posts(subreddit=SUBREDDIT, 
                                    post_type=post_type, 
                                    limit=LIMIT,
                                    fetch_comments=False)
