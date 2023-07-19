# Praw params
SUBREDDIT = "nextfuckinglevel"
POST_TYPES = ['top', 'hot', 'new']
LIMIT = 100  # None for all posts

# OpenAI params
model = "gpt-3.5-turbo"
question = "<Question for chatGPT>"
n_posts = 15
system_prompt = "You are a qualitative researcher"
file_name = "data/exmuslim_hot_Noneposts_2023_06_18_18_25_48.xlsx"
file_name_gpt = f"data/exmuslim_hot_Noneposts_2023_06_18_18_25_48_gpt_{n_posts}.xlsx"
