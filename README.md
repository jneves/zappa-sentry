# zappa-sentry

Sentry handler configuration with defaults for zappa lambdas.

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

If you want the exception handler to capture the exception and capture it, just replace `zappa_sentry.unhandled_exceptions` by `zappa_sentry.capture_exceptions`. This version won't let the exceptions propagate.

# Adding extra information

Just add it to the scope as normal for the new sentry-sdk: https://docs.sentry.io/enriching-error-data/context/?platform=python
