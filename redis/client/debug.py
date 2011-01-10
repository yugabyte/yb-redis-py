import logging
from redis.client.base import Connection, ConnectionPool, Redis, Pipeline

log = logging.getLogger("redis")

def repr_command(args):
    "Represents a command as a string."
    command = [args[0]]
    if len(args) > 1:
        command.extend(repr(x) for x in args[1:])
    return ' '.join(command)

class DebugConnection(Connection):
    def _connect(self, redis_instance):
        log.debug("connecting to %s:%d/%d", self.host, self.port, self.db)
        super(DebugConnection, self)._connect(redis_instance)

    def _disconnect(self):
        log.debug("disconnecting from %s:%d/%d", self.host, self.port, self.db)
        super(DebugConnection, self)._disconnect()


class DebugClient(Redis):
    def __init__(self, *args, **kwargs):
        pool = kwargs.pop('connection_pool', None)
        if not pool:
            pool = ConnectionPool(connection_class=DebugConnection)
        kwargs['connection_pool'] = pool
        super(DebugClient, self).__init__(*args, **kwargs)

    def _execute_command(self, command_name, command, **options):
        log.debug(repr_command(command))
        return super(DebugClient, self)._execute_command(
            command_name, command, **options
            )

    def pipeline(self, transaction=True):
        """
        Return a new pipeline object that can queue multiple commands for
        later execution. ``transaction`` indicates whether all commands
        should be executed atomically. Apart from multiple atomic operations,
        pipelines are useful for batch loading of data as they reduce the
        number of back and forth network operations between client and server.
        """
        return DebugPipeline(
            self.connection,
            transaction,
            self.encoding,
            self.errors
            )


class DebugPipeline(Pipeline):
    def _execute_transaction(self, commands):
        log.debug("MULTI")
        for command in commands:
            log.debug("TRANSACTION> "+ repr_command(command[1]))
        log.debug("EXEC")
        return super(DebugPipeline, self)._execute_transaction(commands)

    def _execute_pipeline(self, commands):
        for command in commands:
            log.debug("PIPELINE> " + repr_command(command[1]))
        return super(DebugPipeline, self)._execute_pipeline(commands)
        
    