from data import emojis
from emoji_model import Emoji
import requests
import json


emojis_bank = [ Emoji(item["emoji"]) for item in emojis ]
count = 0

def search_elasticsearch(emoji):
    url = "http://localhost:9200/perc_index/_search"
    query_body = {
        "query": {
            "bool": {
                "filter": [
                    {
                        "term": {
                            "_id": "1"
                        }
                    },
                    {
                        "percolate": {
                            "field": "query",
                            "documents": [
                                {
                                    "Body": f"{emoji}Принимать заявки"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "_source": "false",
        "highlight": {
            "fields": {
                "Body": {
                    "type": "fvhm",
                    "number_of_fragments": 0,
                    "phrase_limit": 500
                }
            }
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, data=json.dumps(query_body))
    if response.status_code == 200:
        hits = response.json()["hits"]["hits"]
        if bool(hits):
            return int(hits[0]["highlight"]["Body"][0].split(':')[0])
    else:
        return {
            "error": f"Request failed with status code {response.status_code}",
            "details": response.text
        }

for emoji in emojis_bank:
    result = search_elasticsearch(emoji.emoji)
    if (result is not None) and (emoji.emoji_len != result):
        count += 1
        print(f"{emoji.emoji}\tpy: {emoji.emoji_len}\tes: {result}")

print(f"Total count: {count}/{len(emojis_bank)}")

