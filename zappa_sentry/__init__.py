import json
import os

from raven import Client
from raven.transport.http import HTTPTransport

raven_client = Client(os.environ['SENTRY_DSN'], transport=HTTPTransport)


def unhandled_exceptions(e, event, context):
    try:
        package_info_file = open('package_info.json', 'r')
        package_info = json.load(package_info_file)
        package_info_file.close()

        raven_client.context.merge({'tags': package_info})
    except:
        # not deployed, probably a test
        pass

    print(event)
    print(context)
    raven_client.context.merge({'extra': {
        'event': event,
        'context': context
    }})

    raven_client.captureException()
    return True
