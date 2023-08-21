"""
Keyword searching feature
"""
import os

from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify

elasticsearch_hosts = os.environ.get("ELASTICSEARCH_HOSTS")
es = Elasticsearch(hosts=[elasticsearch_hosts])
app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    """
    API to search the keyword
    """
    keyword = request.args.get('keyword')
    size = request.args.get('limit', 10)
    if not keyword:
        return jsonify({"error": "Keyword parameter 'keyword' is required."}), 400

    results = perform_search(keyword, size)
    if not len(results):
        return jsonify({"message": "Keyword not found in the records!!!"}), 200
    return jsonify({"message": "Documents fetched successfully.", "data": results})


def perform_search(keyword, size):
    """
    Method to perform search operation
    """
    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": [
                    "titles.text",
                    "abstracts.paragraph_markup",
                    "claims.paragraph_markup",
                    "descriptions.paragraph_markup",
                    "inventors.first_name",
                    "inventors.last_name",
                    "inventors.name",
                    "assignees.first_name",
                    "assignees.last_name",
                    "assignees.name",
                    'ipc_classes.label',
                    'locarno_classes.label', 'ipcr_classes.label', 'national_classes.label',
                    'ecla_classes.label', 'cpc_classes.label', 'f_term_classes.label', 'legal_status',
                    'family_members.ucid', 'family_members.titles'
                ]
            }
        },
        "size": size,
        "sort": "_score"
    }
    response = es.search(index='patents', body=body)
    result = response['hits']['hits']
    names = list()
    for res in result:
        names.append(res['_id'])
    return names


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
