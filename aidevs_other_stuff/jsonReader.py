import json

# Reds up to 300 JSON documents from a file
#c an be parametrized to read more
class JsonReader:
    @staticmethod
    def read(file_name, limit=300):
        single_jsons_list = []
        nr = 0
        print("Started Reading JSON file which contains multiple JSON document")
        with open(file_name) as f:
            brace_count = 0
            json_str = ''
            for json_obj in f:

                if json_obj != '[\n' and json_obj != ']':
                    brace_count += json_obj.count('{')
                    brace_count -= json_obj.count('}')
                    if json_obj.count('},'):
                        # print('repairing')
                        json_obj = '}'
                    json_str += json_obj
                    # print(json_str)
                    if brace_count == 0:
                        single_json_dict = json.loads(json_str)
                        single_jsons_list.append(single_json_dict)
                        nr += 1
                        print("NR", nr)
                        if nr == limit+1: break
                        json_str = ''
        return single_jsons_list


if __name__ == '__main__':
    reader_result = JsonReader().read("sample.json")

    print("Printing each JSON Decoded Object")
    for entry in reader_result:
        print(entry["title"], entry["url"], entry["info"], entry["date"])
