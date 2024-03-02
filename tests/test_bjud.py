from datetime import datetime
from bjud.bjud import Bjud


def test_get_event_norberg_online():
    bjud = Bjud()
    e = bjud.get_event("https://www.facebook.com/events/415842204239647/")
    assert e.title == "Norbergfestival 2024"
    assert e.organiser == "Norbergfestival"
    assert e.street_address == "Gamla Banan 10"
    assert e.post_address == "SE-738 33 Norberg"
    assert e.country == "Sverige"
    assert e.start_time.year == 2024
    assert e.start_time.month == 7
    assert e.start_time.day == 4
    assert "Experimental" in e.description


def test_get_event_tca_online():
    bjud = Bjud()
    e = bjud.get_event("https://www.facebook.com/events/1828636217581951")
    assert "Take Concrete Action" in e.organiser
    assert e.street_address == "Tjärhovsgatan 46"


def test_get_event_no_address_online():
    bjud = Bjud()
    e = bjud.get_event("https://www.facebook.com/events/1510012029929672")
    assert e.title == "Manifestation: Stäng ner Elbit!"
