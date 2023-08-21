import tiktoken
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
    input_price_1k_tokens,
    output_price_1k_tokens,
)

from tqdm import tqdm

import pandas as  pd

openai.api_key = openai_key


def cost_estimate(df, model, system_prompt, question, 
    input_price_1k_tokens=input_price_1k_tokens, 
    output_price_1k_tokens=output_price_1k_tokens):

    n_queries = df.shape[0]

    expected_num_response_tokens = 100
    responses_cost = output_price_1k_tokens * (expected_num_response_tokens / 1_000) * n_queries

    full_text = (" ".join(df["title"].tolist()) 
                + " ".join([ txt for txt in df["selftext"].tolist() if isinstance(txt, str)])
                + (system_prompt + question) * n_queries
    )

    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model(model)
    
    n_input_tokens = len(enc.encode(full_text))

    query_cost = input_price_1k_tokens * (n_input_tokens / 1_000) 

    resp = input(f"Estimated cost ${query_cost + responses_cost :0.4f}. Enter `yes` to continue:\n")

    assert resp == "yes", "Do not proceed with GPT queries"



if __name__ == "__main__":

    df = pd.read_excel(file_name)

    df = df.iloc[1:n_posts+1]

    cost_estimate(df, model, system_prompt, question)

    responses_topics = {}
    for topic in topics_list:
        responses_topics[topic] = []
    responses_comments = []

    n_input_tokens = 0
    n_output_tokens = 0

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

        n_input_tokens += response["usage"]["prompt_tokens"]
        n_output_tokens += response["usage"]["completion_tokens"]
        gpt_response = response['choices'][0]['message']['content']

        try:
            gpt_response_dict = json.loads(gpt_response)
        except:
            print(f"\n{id = }: bad response:\n{gpt_response}\n\n")
            gpt_response_dict = {}
            for topic in topics_list:
                gpt_response_dict[topic] = None
            gpt_response_dict["comment"] = None


        df_checkpoint = df.iloc[: id].copy()
        
        for topic in topics_list:
            topic_found = False
            if topic in gpt_response_dict["topic"]:
                topic_found = True
            responses_topics[topic].append(topic_found)
            df_checkpoint[topic] = responses_topics[topic]

        responses_comments.append(gpt_response_dict["comment"])
        df_checkpoint["gpt_comment"] = responses_comments

        # Save progress
        df_checkpoint.to_excel(file_name_gpt)
    tot_cost = output_price_1k_tokens * (n_output_tokens/1_000) + input_price_1k_tokens * (n_input_tokens/1_000)
    print(f"Total cost: ${tot_cost :.5f}")
    print(f"Data saved at {file_name_gpt}")


