from langchain.embeddings import OpenAIEmbeddings

from helper import Helper
import openai
from qdrant_client import QdrantClient  # pip install qdrant-client
from qdrant_client.http.models import Distance, VectorParams


# c0304.search - zaimportuj do swojej bazy wektorowej, spis wszystkich linków z newslettera unknowNews z adresu:
# https://unknow.news/archiwum.json
# [jeśli zależy Ci na czasie, możesz dodać pierwsze 300 rekordów]
#
# Następnie wykonaj zadanie API o nazwie “search” — odpowiedz w nim na zwrócone przez API pytanie. Odpowiedź musi być adresem URL kierującym do jednego z linków unknowNews.
class Search:
    @staticmethod
    def generate_answer(test_data):
        collection_name = "ai_devs_search_task"
        question = str(test_data.json()["question"])

        # create embeddings for sample text query
        embeddings = OpenAIEmbeddings()
        question_embedding = embeddings.embed_query(question)

        qdrant = QdrantClient("http://localhost:6333")
        search = qdrant.search(collection_name, query_vector=question_embedding, limit=1, query_filter={
            'must': [
                {
                    'key': 'source',
                    'match': {
                        'value': collection_name
                    }
                }
            ]
        })

        print("Search", search)
        print("Search content", search)
        found_article = search[0].payload
        url = found_article['content']['url']
        print("Found article url", url)
        return url


if __name__ == '__main__':
    test_data = Helper.create_simulated_response(
        b'{"question":"Co rozni pseudonimizacje od anonimizowania danych?"}')

    ans = Search().generate_answer(test_data)
    print("Ans",ans)


# """blogger here
# ###
# rules:
# ###
# -i create a blog entry about pizza margherita containing 4 titles
# -list titles no deviation"""
