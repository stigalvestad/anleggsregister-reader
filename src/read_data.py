import json
import pandas as pd
import sys
from pprint import pprint


def set_encoding():
    reload(sys) # just to be sure
    sys.setdefaultencoding('utf-8')


def get_data_frame_from_json_file(rel_file_path):
    with open(rel_file_path) as f:
        data = json.load(f)

    # pprint(data)

    print 'Number of elements: ' + `data['numberOfElements']`
    print 'Includes all items in search? ' + `data['last']`

    search_results = data['content']
    # pprint(search_results)

    res = json.dumps(search_results, ensure_ascii=False)
    # print res

    return pd.read_json(res, orient='records')


set_encoding()
df = get_data_frame_from_json_file('../data/anlegg2.json')
# print df

# list column names
print list(df)

# list unique owners
# print df.ownerName.unique()
df_grane = df[(df.ownerName == 'IK GRANE ARENDAL ORIENTERING') | (df.ownerName == 'GRANE IDRETTSLAG')]
print df_grane
# 'IK GRANE ARENDAL ORIENTERING' u'GRANE IDRETTSLAG'
# 'AUSTRE MOLAND IDRETTSLAG'

# print df.operatorName.unique()
df_grane_short = df_grane[['buildingYear', 'classDescription', 'facilityId', 'name', 'ownerName', 'ownerOrgno', 'status', 'totalGrants', 'totalPayments', 'totalRevoked', 'typeDescription']]
print df_grane_short