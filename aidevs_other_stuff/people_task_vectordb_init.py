from aidevs_other_stuff.jsonReader import JsonReader
from qdrantHelper import QdrantHelper


# https://qdrant.tech/documentation/quick-start/
# This code initializes Qdrant collection ai_devs_search_task, and adds vectors from local documents to it
# then it searches the collection for the most similar vector to the query vector
# vectors for documents and the query are generated using OpenAI API ada / creating embeddings
# takes some time 3-5mins approx
if __name__ == '__main__':
    MEMORY_PATH = "people_task_vectordb_init.json"
    COLLECTION_NAME = "ai_devs_people_task"

    QdrantHelper.init_collection(persistent_memory = JsonReader.read(MEMORY_PATH, limit = 1500), collection_name=COLLECTION_NAME, limit=1500)