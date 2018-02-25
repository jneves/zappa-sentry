import json
import os

from raven import Client

raven_client = Client(os.environ['SENTRY_DSN'])


def unhandled_exceptions(e, event, context):
    package_info_file = open('package_info.json', 'r')
    package_info = json.load(package_info_file)
    package_info_file.close()

    raven_client.context.merge({'tags': package_info})

    raven_client.setExtraContext({
        'event': event,
        'context': context
    })

    raven_client.captureException(e)
    return True
