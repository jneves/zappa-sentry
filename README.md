zappa-sentry

Sentry handler with defaults for zappa lambdas.

# Installation

`pip install zappa_sentry`

# Zappa configuration

Setup your sentry DSN as the value of environment variable `SENTRY_DSN`, either on the `zappa_setting.json` file or in any of the other methods on https://github.com/miserlou/zappa/#setting-environment-variables

Then you can setup the `zappa_sentry.unhandled_exceptions` handler.

Example:
```
{
    "dev": {
        ...
        "environment_variables": {
            "SENTRY_DSN": "https://*key*:*pass*@sentry.io/*project*",
            ...
        },
        "exception_handler": "zappa_sentry.unhandled_exceptions",
        ...
    },
    ...
}
```

And that's all. Deploy your zappa function and you should see any errors appearing on sentry.

# Sentry raven client

If you need sentry's client to add extra information just do:

`from zappa_sentry import raven_client`

And you'll get an already initialized raven_client. Feel free to use to add context, tags, etc.
