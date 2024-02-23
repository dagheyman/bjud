from bjud.bjud import Bjud


def test_get_event():
    bjud = Bjud()
    e = bjud.get_event("https://www.facebook.com/events/415842204239647/")
    assert "Experimental" in e.description

    e = bjud.get_event("https://www.facebook.com/events/1828636217581951")
    assert "Take Concrete Action" in e.organiser
