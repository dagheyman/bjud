import sys
from bjud.bjud import Bjud

bjud = Bjud()
event = bjud.get_event(sys.argv[1])

print("---")
print(f"title: {event.title}")
print(f"date: {event.start_time}")
print(f"enddate: {event.stop_time}")
print(f"locations: []")
print(f"forms: []")
print(f"organizer: {event.organiser}")
print(f"addressName: ")
print(f"streetAddress: {event.street_address}")
print(f"postalCode: {event.post_address}")
print(f"addressRegion:")
print(f"addressCountry: {event.country}")
print(f"source: {sys.argv[1]}")
print("---")
print(f"{event.description}")
