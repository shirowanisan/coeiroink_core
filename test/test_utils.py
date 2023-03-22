import json
from pathlib import Path

from coeirocore.coeiro_manager import EspnetModel
from coeirocore.model import AudioQuery

from coeirocore.query_manager import query2tokens_prosody


def test_query_to_model():
    with open(Path(__file__).parent / 'resources/test_query.json') as f:
        data = json.load(f)
    query = AudioQuery.parse_obj(data)
    tokens_from_query = query2tokens_prosody(query)
    print('\n')
    print(tokens_from_query)
    tokens_from_text = EspnetModel.text2tokens('どういうわけか説明してみましょう')
    print(tokens_from_text)
    assert tokens_from_query == tokens_from_text
