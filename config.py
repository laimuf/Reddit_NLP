# Praw params
SUBREDDIT = "nextfuckinglevel"
POST_TYPES = ['top', 'hot', 'new']
LIMIT = 100  # None for all posts

# OpenAI params
model = "gpt-3.5-turbo"
n_posts = 100
system_prompt = """
You are a qualitative researcher. You answer by returning a json file 
(absolutely never return any text outside this json file) with the format
 `{"topic": list[str], "comment": str}`
"""
file_name = "data/exmuslim_hot_Noneposts_2023_06_18_18_25_48.xlsx"
file_name_gpt = f"data/exmuslim_hot_Noneposts_2023_06_18_18_25_48_gpt_{n_posts}.xlsx"
question = """
I'll show you a reddit post at the bottom. 
Return a json file (absolutely never return any text outside this json file) with the format
 `{"topic": list[str], "comment": str}` 
where `topic` key list contains any of "Intellectual", "Seeking support" and "Negotiating apostasy" as values 
if you think the reddit post contains any of these topics (leave list empty if no topic is found). 
The value of the "comment" key is any explanation you have for these topic being in the reddit post. 
This is a definition of the three topics
topics_definition = {
    "Intellectual": [
        {
            "Morality issues and concerns": [
                "Rants",
                "Humour and satire/memes/multimedia",
                "Subreddit’s role",
                "Ritualised routine meme’s on Friday (humour and satire)",
                "Hadits of The Day (HOTD)"
            ]
        },
        {
            "Doubts and revelation": [
                "Questions about Islam",
                "Users confession on subreddit’s part to their apostasy"
            ]
        },
        {
            "Subreddit’s role": [
                "Annual demographic questionnaires (Numbers keep growing)",
                "Tagline header",
                "Source of info"
            ]
        }
    ],
    "Seeking support": [
        {
            "Advice and help": [
                "Marriage/forced marriage",
                "Running away",
                "Relationships",
                "Coming out/disown",
                "Safety concerns"
            ]
        },
        {
            "Public declaration of apostasy": None
        },
        {
            "Making connections": None
        },
        {
            "Mental health": None
        }
    ],
    "Negotiating apostasy": [
        {
            "Leaving Islam Journey": None
        },
        {
            "Between secularity and piety": [
                "Rituals abandonment and maintenance",
                "Embodiment rituals",
                "Double life"
            ]
        },
        {
            "Kinship": [
                "Coming out, divorce and LGBTQ coming out",
                "The self and the other"
            ]
        },
        {
            "Marriage": None
        },
        {
            "Disowning": None
        },
        {
            "Moving abroad": None
        }
    ]
}
"""

