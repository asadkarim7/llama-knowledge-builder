import openai
import os


def generate_embeddings(papers_list):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key

    embeddings = []
    for paper in papers_list:
        response = openai.Embedding.create(input=paper, engine="text-similarity-babbage-001")
        embeddings.append(response['data'][0]['embedding'])

    return embeddings