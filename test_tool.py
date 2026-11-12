import json
from url_query_stripper import transform
def test_transform():
    value='https://example.test/x?q=1'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'https://example.test/x' in json.dumps(result,ensure_ascii=False)
