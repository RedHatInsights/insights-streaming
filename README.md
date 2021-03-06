# insights-streaming
Experimental repository for processing of stream data using insights.

Dependencies are declared like with other insights components, and core wires
everything together. We then run all of the streams, and data flows out through
``emit`` calls and into the ``update`` functions of dependents. If ``update``
returns anything but ``None``, the value is emitted to downstream dependents.
``update`` can also call ``emit`` directly.
 
```python
#!/usr/bin/env python
from __future__ import print_function
import random
import time

from insights_streaming import run_streams, stream, Stream


class BaseFeed(Stream):
    def __init__(self):
        self.counter = 0
        super(BaseFeed, self).__init__()

    def go(self):
        # while True:
        for _ in range(5):
            time.sleep(random.random() * 2)
            self.emit(self.counter)
            self.counter += 1


@stream()
class FeedOne(BaseFeed):
    pass


@stream()
class FeedTwo(BaseFeed):
    pass


@stream(FeedOne)
class FeedOneModel(Stream):
    def update(self, src, evt):
        return evt * 2


@stream(FeedTwo)
class FeedTwoModel(Stream):
    def update(self, src, evt):
        return evt * 3


@stream(FeedOneModel, FeedTwoModel)
class Watcher(Stream):
    def update(self, src, data):
        print("{src}: {data}".format(src=src, data=data))


if __name__ == "__main__":
    run_streams()
```
