# -*- coding: utf-8 -*-
from configparser import ConfigParser
import json
import os

import sentry_sdk
from sentry_sdk import capture_exception, configure_scope


def unhandled_exceptions(e, event, context):
    "Exception handler reports exceptions to sentry but does not capture them."
    sentry_config = ConfigParser(os.environ)
    sentry_sdk.init(sentry_config.get('DEFAULT', 'SENTRY_DSN'))

    with configure_scope() as scope:
        try:
            package_info_file = open('package_info.json', 'r')
            package_info = json.load(package_info_file)
            package_info_file.close()

            for key, value in package_info.items():
                scope.set_tag(key, value)
        except OSError:
            # not deployed, probably a test
            pass

        if 'httpMethod' in event:
            scope.set_tag('http_method', event['httpMethod'])
            scope.set_tag('path', event['path'])
        if 'Host' in event['headers']:
            scope.set_tag('host', event['headers']['Host'])
        if 'User-Agent' in event['headers']:
            scope.set_tag('user_agent', event['headers']['User-Agent'])
        if 'requestContext' in event and 'stage' in event['requestContext']:
            scope.set_tag('stage', event['requestContext']['stage'])

        scope.set_extra('event', event)

    capture_exception(e)
    return False


def capture_exceptions(e, event, context):
    "Exception handler that makes exceptions disappear after processing them."

    unhandled_exceptions(e, event, context)
    return True
