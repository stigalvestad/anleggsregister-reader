import json
import pandas as pd
from pprint import pprint


def get_data_frame_from_json_file(rel_file_path):
    with open(rel_file_path) as f:
        data = json.load(f)

    # pprint(data)

    print 'Number of elements: ' + `data['numberOfElements']`
    print 'Includes all items in search? ' + `data['last']`

    search_results = data['content']
    # pprint(search_results)

    res = json.dumps(search_results, ensure_ascii=False)
    print res

    return pd.read_json(res, orient='records')


df = get_data_frame_from_json_file('../data/anlegg.json')
print df