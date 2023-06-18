# Reddit scrapper

This simple app allows to scrap and save in excel format posts from desired subreddits

## Praw setup

[Praw](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) is an api that allows you to scrap data from reddit.

To use it in this project, create a file in the root directory called `praw_credentials.py` with the following content
```python
client_id ='<your client_id>'
client_secret ='your client_secret' 
user_agent ='<your user_agent>'
```

If you do not have these credentials, you can create them [following this tutorial](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps). 

## Environment setup

You first need `python >= 3.7`, then you can pip-install the packages in `requirements.txt`. You can do this by running the following commands in your bash terminal (`cd` into the project root):
```bash
pip3 install virtualenv
virtualenv .venv 
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the app

Set the desired subreddit, post type and limit (number of results) in `config.py`, then run this script with
```bash
python app.py
```