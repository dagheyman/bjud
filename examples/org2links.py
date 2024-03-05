import sys
from bjud.org import Org

org = Org()
events = org.get_events(sys.argv[1])

for e in events:
	print(e);
