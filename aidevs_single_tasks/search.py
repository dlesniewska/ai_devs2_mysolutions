from langchain.embeddings import OpenAIEmbeddings

from helper import Helper
import openai
from qdrant_client import QdrantClient  # pip install qdrant-client
from qdrant_client.http.models import Distance, VectorParams


# c0104.blogger - use OpenAPI chat create blog paragraphs from given titles
class Search:
    @staticmethod
    def generate_answer(test_data):
        COLLECTION_NAME = "ai_devs_search_task"
        question = str(test_data.json()["question"])

        # create embeddings for sample text query
        embeddings = OpenAIEmbeddings()
        question_embedding = embeddings.embed_query(question)

        qdrant = QdrantClient("http://localhost:6333")
        search = qdrant.search(COLLECTION_NAME, query_vector=question_embedding, limit=1, query_filter={
            'must': [
                {
                    'key': 'source',
                    'match': {
                        'value': COLLECTION_NAME
                    }
                }
            ]
        })

        print("Search",search)
        print("Search content", search.result[0].payload.content)
        return search.result[0].payload.content

        # openai.api_key = Helper().get_openapi_key()
        #
        # ai_resp = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system",
        #          # "content": "pizza margherita  blog entry 4 titles from given words, no deviation"},
        #          # "content": "pizza margherita  blog 4 short paragraphs  (to 50 words) containing exact given titles"},
        #          "content": "write separate paragraphs for each title, one short paragraph for each title"},
        #         {"role": "user",
        #          "content": words_for_titles}
        #     ])
        # json_result = ai_resp.choices[0].message.content




if __name__ == '__main__':
    test_data = Helper.create_simulated_response(
        b'{"question":"Ala ma kota?"}')

    ans = Search().generate_answer(test_data)
    print(ans)


# """blogger here
# ###
# rules:
# ###
# -i create a blog entry about pizza margherita containing 4 titles
# -list titles no deviation"""
