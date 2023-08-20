import time 
import json
import openai
from credentials import openai_key

from config import (
    model,
    system_prompt,
    question,
    topics_list,
    n_posts,
    file_name,
    file_name_gpt,
)

from tqdm import tqdm

import pandas as  pd

openai.api_key = openai_key


if __name__ == "__main__":

    df = pd.read_excel(file_name)

    df = df.iloc[1:n_posts+1]

    responses_topics = {}
    for topic in topics_list:
        responses_topics[topic] = []
    responses_comments = []

    for id, row in tqdm(df.iterrows()):
        time.sleep(1)

        title_reddit_post = row.title
        body_reddit_post = row.selftext

        user_question = f"{question}\n\n Reddit post title: {title_reddit_post}\n body: {body_reddit_post}"

        response = openai.ChatCompletion.create(
          model=model,
          messages=[
                {"role": "system", "content":  system_prompt},
                {"role": "user", "content": user_question},
            ]
        )
        gpt_response = response['choices'][0]['message']['content']
        gpt_response_dict = json.loads(gpt_response)

        # Add try-except to filter bad responses
        
        for topic in topics_list:
            topic_found = False
            if topic in gpt_response_dict["topic"]:
                topic_found = True
            responses_topics[topic].append(topic_found)
            df_checkpoint[topic] = responses_topics[topic]

        df_checkpoint = df.iloc[: id].copy()
        responses_comments.append(gpt_response_dict["comment"])
        df_checkpoint["gpt_comment"] = responses_comments

        # Save progress
        df_checkpoint.to_excel(file_name_gpt)


