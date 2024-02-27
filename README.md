# bjud

bjud is a small python library for scraping facebook events

## Example usage

```
from bjud.bjud import Bjud

bjud = Bjud()
event = bjud.get_event('https://www.facebook.com/events/358899250393724')
print(event.title)
```

## Installation

```
python3 -m venv venv
source venv/bin/activate
pip3 install .
```

### Run tests

```
pip3 install pytest
pytest tests
```
