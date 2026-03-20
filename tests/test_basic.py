from phishdetect.infer import predict

def test_url_prediction():
    r = predict(subject="", body="", urls=["http://example.com"])
    assert "label" in r and "probability" in r
