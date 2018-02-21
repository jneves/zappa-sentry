import json
import os

from raven import Client

zappa_client = Client(os.environ['SENTRY_DSN'])


def unhandled_exceptions(e, event, context):
    package_info_file = open('package_info.json', 'r')
    package_info = json.load(package_info_file)
    package_info_file.close()
    zappa_client.setTagsContext(package_info)

    zappa_client.setExtraContext({
        'event': event,
        'context': context
    })

    zappa_client.captureException()
    return True
