import os
import openai
from utils.fetch_arxiv import fetch_papers
from utils.data_preparation import clean_data
from utils.generate_embeddings import generate_embeddings


def ask_question(question, embeddings, papers_list):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key

    response = openai.Embedding.create(input=question, engine="text-similarity-babbage-001")
    question_embedding = response['data'][0]['embedding']

    # Find the most similar paper embedding
    most_similar_idx = None
    highest_similarity = -1
    for idx, embedding in enumerate(embeddings):
        similarity = openai.cosine_similarity(embedding, question_embedding)
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_idx = idx

    return papers_list[most_similar_idx]


def main():
    papers_list = fetch_papers()
    cleaned_papers = clean_data(papers_list)
    embeddings = generate_embeddings(cleaned_papers)

    while True:
        question = input("What is your question about Llama-2? ")
        if question.lower() in ['exit', 'quit']:
            break
        answer = ask_question(question, embeddings, cleaned_papers)
        print("The most relevant paper is:\n", answer)


if __name__ == "__main__":
    main()
