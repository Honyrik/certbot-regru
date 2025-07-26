from setuptools import setup
from setuptools import find_packages

from certbot_regru import __version__

install_requires = [
    'acme>=4.1.1',
    'certbot>=4.1.1',
    'requests>=2.32.4',
    'mock',
    'setuptools',
    'zope.interface',
]

data_files = [
    ('/usr/local/etc/letsencrypt', ['regru.ini'])
]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='certbot-regru-freebsd',
    version=__version__,
    description="Reg.ru DNS authenticator plugin for Certbot",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Honyrik/certbot-regru',
    author="Honyrik",
    author_email='honyrik@gmail.com',
    license='MIT',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    install_requires=install_requires,
    data_files=data_files,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'certbot.plugins': [
            'dns-regru = certbot_regru_freebsd.dns:Authenticator',
        ],
    },
    test_suite='certbot_regru_freebsd',
)
