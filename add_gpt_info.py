import time 

import openai
from praw_credentials import openai_key

from tqdm import tqdm

import pandas as  pd

openai.api_key = openai_key

model = "gpt-3.5-turbo"
question = ("Determine if the following post contains themes of de-conversion or doubts about islam. If it does, then comment about them. "
          "If it doesn't, then only return the python boolean False and nothing else:\n"
)
n_posts = 15
system_prompt = "You are a qualitative researcher"
file_name = "data/exmuslim_hot_Noneposts_2023_06_18_18_25_48.xlsx"
file_name_gpt = f"data/exmuslim_hot_Noneposts_2023_06_18_18_25_48_gpt_{n_posts}.xlsx"



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