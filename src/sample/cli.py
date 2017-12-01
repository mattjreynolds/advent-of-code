import time
import click
import click_log
import logging
from functools import wraps

import days

logger = logging.getLogger(f'{__name__}.cli')
click_log.basic_config(logger)

def log_it():  
    def wrap(f):  
        @wraps(f)  
        def decorator(*args, **kwargs):  
            logger.debug(f'>>> {f.__name__}')
            start_time = time.time()
            value = f(*args, **kwargs)
            logger.debug(f'<<< {f.__name__} (took {time.time()-start_time})')
            return value
        return decorator  
    return wrap  


def write_results(data, stream, sort=True):
    import json

    class Encoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, set):
                return list(o)
            if isinstance(o, defaultdict):
                return dict(o)
            return super().default(o)

    json.dump(
        data,
        stream,
        cls=Encoder,
        separators=(',', ': '),
        indent=2,
        ensure_ascii=False,
        sort_keys=sort,
    )


@click.command()
@click.version_option()
@click_log.simple_verbosity_option(logger)
@click.argument('day')
@click.option('--stats/--no-stats', help='Show stats on run', default=False)
def cli(day, stats):
    '''Sample: sample'''
    stat = {}
    stat['StartTime'] = time.time()

    fn = getattr(days, f'day_{day}')
    resp = fn()
    print(resp['result'])

    stat['EndTime'] = time.time()
    stat['TotalRunTime'] = stat['EndTime'] - stat['StartTime']
    stat['stats'] = resp['stats']

    if stats:
        click.echo('\n--- stats ---\n')
        stdout = click.get_text_stream('stdout')
        write_results(stat, stdout, sort=False)
