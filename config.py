# Praw params
SUBREDDIT = "nextfuckinglevel"
POST_TYPES = ['top', 'hot', 'new']
LIMIT = 100  # None for all posts

# OpenAI params
model = "gpt-3.5-turbo"
input_price_1k_tokens = 0.0015
output_price_1k_tokens = 0.002

n_posts = 1_000
file_name = "data/exmuslim/exmuslim_hot_all_posts_2023_08_20_14_51_37.xlsx"
file_name_gpt = f"data/exmuslim/exmuslim_hot_all_posts_2023_08_20_14_51_37_gpt_{n_posts}.xlsx"

response_format = """`{"topic": list[str], "comment": str}`"""
topics_list = [
    "Intellectual questions", 
    "Sharing experience",
    "Seeking support", 
    "Subreddit’s role", 
    "Humor"
    ]

topics_definition = {
    "Intellectual questions": 
        ["Questions about Islam",
                "Questions about morality",
                "Questions about Islamic claims and science",
                "Questions about the Koran/Quran and Hadiths",
                "Question about God/Allah",
                "Question about prophet Muhammad",
                "Question about Islamic history and figures",
            "Doubts and revelation",
                "Doubts about the legitimacy of Islam",
                "Criticizing Islam",
                "Asking people about opinion of certain issue and Islam",
                "Asking people about opinion of Islam",
                "Asking people’s experience of leaving Islam",
                "Sharing their doubts and struggle",
            ],
    "Sharing experience": 
        [
                "Marriage/forced marriage",
                "Running away from family/home",
                "Relationships",
                "Coming out/disown",
                "Safety concerns"
                "Migration/immigration"
                "Family issues"
                "Marriage issue"
                "Ramadhan/fasting"
                "Conducting rituals: prayers/salat/reading Quran/hajj"
                "Body, food and Islam: Hijab, sex, shyness, modesty, alcohol, pork"
                "Faking Islamic identity"
                "Hiding ex-Muslim/gay/deconvert/apostate identity",
                "Sharing personal rants, anger and frustration"],
    "Seeking support": 
        [
                "Marriage/forced marriage",
                "Running away from family/home",
                "Relationships",
                "Coming out/disown",
                "Safety concerns"
                "Migration/immigration"
                "Family issues"
                "Marriage issue"
                "Ramadhan/fasting"
                "Conducting rituals: prayers/salat/reading Quran/hajj"
                "Body, food and Islam: Hijab, sex, shyness, modesty, alcohol, pork"
                "Faking Islamic identity"
                "Hiding ex-Muslim/gay/deconvert/apostate identity",
               ],
    "Subreddit’s role": 
            ["Address reddit",
                "Annual demographic questionnaires",
                "Comments on islamophobia or right wing agenda",
                "Sharing rants, anger and frustration can be personal",
            "Thank reddit",
                "Thanking/Comments on subreddit helps people leaving Islam"
                "Thanking/Comments on subreddit helps people’s struggling"
                "Thanking/Comments on subreddit helps people’s doubting",
            "Making connections with people on the subreddit",
    ],
    "Humor": 
        ["Jokes, satire and sarcasm"]
    ,
}



system_prompt = f"""
You are a qualitative researcher. You answer by returning a json file 
(absolutely never return any text outside this json file) with the format
 {response_format}
"""


question = f"""
I'll show you a reddit post at the bottom. 
Return a json file (absolutely never return any text outside this json file) with the format
 {response_format} 
where "topic" keys must be from this list {topics_list}. 
If you think the reddit post contains any of these topics (leave list empty if no topic is found). 
The value of the "comment" key is any explanation you have for these topic being in the reddit post. 
This is the definition of the three topics
{topics_definition}
"""

