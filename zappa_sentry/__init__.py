from configparser import ConfigParser
import json
import os

from raven import Client
from raven.transport.http import HTTPTransport


raven_config = ConfigParser(os.environ)
_raven_client = None


def get_raven_client():
    if not _raven_client:
        _raven_client = Client(raven_config.get('DEFAULT', 'SENTRY_DSN'), transport=HTTPTransport)
    return _raven_client


def unhandled_exceptions(e, event, context):
    """Exception handler reports exceptions to sentry but does not capture them."""
    raven_client = get_raven_client()

    try:
        package_info_file = open('package_info.json', 'r')
        package_info = json.load(package_info_file)
        package_info_file.close()

        raven_client.context.merge({'tags': package_info})
    except:
        # not deployed, probably a test
        pass

    if 'httpMethod' in event:
        extra_tags = {
            'http_method': event['httpMethod'],
            'path': event['path']
        }
        if 'Host' in event['headers']:
            extra_tags['host'] = event['headers']['Host']
        if 'User-Agent' in event['headers']:
            extra_tags['user_agent'] = event['headers']['User-Agent']
        if 'requestContext' in event and 'stage' in event['requestContext']:
            extra_tags['stage'] = event['requestContext']['stage']
        raven_client.context.merge({'tags': extra_tags})

    raven_client.context.merge({'extra': {
        'event': event
    }})

    raven_client.captureException()
    return False


def capture_exceptions(e, event, context):
    """Exception handler that makes exceptions disappear after processing them."""

    unhandled_exceptions(e, event, context)
    return True
