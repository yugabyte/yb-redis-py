import logging

from redis.client.base import *

log = logging.getLogger("redis")
if log.isEnabledFor(logging.DEBUG):
    from redis.client.debug import DebugClient as Redis
    from redis.client.debug import DebugConnection as Connection
    from redis.client.debug import DebugPipline as Pipeline
