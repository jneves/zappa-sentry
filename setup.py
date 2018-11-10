from setuptools import setup

setup(
  name = 'zappa_sentry',
  packages = ['zappa_sentry'],
  version = '0.3.0',
  description = 'Easy integration with sentry for zappa apps',
  author = 'João Miguel Neves',
  author_email = 'joao@silvaneves.org',
  url = 'https://github.com/jneves/zappa-sentry',
  download_url = 'https://github.com/jneves/zappa-sentry/archive/0.2.3.tar.gz',
  keywords = 'logging zappa sentry',
  install_requires=[
    'sentry-sdk'
  ],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
  ]
)
