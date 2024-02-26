import sys
from bjud.bjud import Bjud

bjud = Bjud()
event = bjud.get_event(sys.argv[1])

print("---")
print(f"title: {event.title}")
print(f"date:")
print(f"enddate:")
print(f"locations:")
print(f"forms:")
print(f"organizer: {event.organiser}")
print(f"source: {sys.argv[1]}")
print("---")
print(f"{event.description}")
