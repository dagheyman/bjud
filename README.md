# bjud

bjud is a small python library for scraping facebook events

## Example usage

```
from bjud.scraper import Bjud

bjud = Bjud()
event = bjud.get_event('https://www.facebook.com/events/358899250393724')
print(event.title)
```
