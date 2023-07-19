import time 

import openai
from credentials import openai_key

from config import (
    model,
    system_prompt,
    question,
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

    responses = []

    for id, row in tqdm(df.iterrows()):
        time.sleep(1)

        title_reddit_post = row.title
        body_reddit_post = row.selftext

        user_question = f"{question} title: {title_reddit_post}\n body: {body_reddit_post}"

        response = openai.ChatCompletion.create(
          model=model,
          messages=[
                {"role": "system", "content":  system_prompt},
                {"role": "user", "content": user_question},
            ]
        )
        responses.append(response['choices'][0]['message']['content'])

        df_checkpoint = df.iloc[: id].copy()
        df_checkpoint["gpt_comment"] = responses
        df_checkpoint.to_excel(file_name_gpt)

    df["gpt_comment"] = responses

    df.to_excel(file_name_gpt)