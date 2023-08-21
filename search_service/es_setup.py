import json
import zipfile
import os
from elasticsearch import Elasticsearch

elasticsearch_hosts = os.environ.get("ELASTICSEARCH_HOSTS")
es = Elasticsearch(hosts=[elasticsearch_hosts])

index_name = 'patents'
if __name__ == "__main__":
    index_exist = es.indices.exists(index=index_name)
    if index_exist:
        print(f'Index {index_name} exists')
    else:
        with zipfile.ZipFile('patent_jsons.zip') as z:
          for filename in z.namelist():
            with z.open(filename) as f:
              patent_data = json.load(f)

              doc_id = patent_data['patent_number']

              es.index(index=index_name, body=patent_data, id=doc_id)

        print(f"Indexed {len(z.namelist())} patents")