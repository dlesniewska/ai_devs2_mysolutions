from helper import Helper
import openai


# Korzystając z modelu text-embedding-ada-002 wygeneruj embedding dla frazy Hawaiian pizza
# — upewnij się, że to dokładnie to zdanie. Następnie prześlij wygenerowany embedding na endpoint /answer.
# Konkretnie musi być to format {"answer": [0.003750941, 0.0038711438, 0.0082909055, -0.008753223, -0.02073651, -0.018862579, -0.010596331, -0.022425512, ..., -0.026950065]}.
# Lista musi zawierać dokładnie 1536 elementów.

# https://platform.openai.com/docs/guides/embeddings
# >>pip install openai[datalib]
class Embeddings:
    @staticmethod
    def generate_answer(test_data):
        # call openai embeddings ada api
        openai.api_key = Helper().get_openapi_key()
        ai_response = openai.Embedding.create(
            model = "text-embedding-ada-002",
            input = "Hawaiian pizza"
        )
        result = ai_response["data"][0]["embedding"]

        print(result)
        print(len(result))
        return result


if __name__ == '__main__':
    Embeddings().generate_answer("test")
