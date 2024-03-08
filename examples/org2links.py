import sys
from bjud.bjud import Bjud

bjud = Bjud()

events = bjud.get_event_links(sys.argv[1])

for e in events:
    print(e)
