from datetime import datetime
from bjud.bjud import Bjud


def test_get_event():
    bjud = Bjud()
    e = bjud.get_event("https://www.facebook.com/events/415842204239647/")
    assert e.title == "Norbergfestival 2024"
    assert e.organiser == "Norbergfestival"
    assert e.street_address == "Gamla Banan 10"
    assert e.post_address == "SE-738 33 Norberg"
    assert e.country == "Sverige"
    assert e.start_time.isoformat() == "2024-07-04T18:00:00"
    assert e.stop_time.isoformat() == "1970-01-01T01:00:00"

    assert "Experimental" in e.description

    e = bjud.get_event("https://www.facebook.com/events/1828636217581951")
    assert "Take Concrete Action" in e.organiser
    assert e.street_address == "Tjärhovsgatan 46"
