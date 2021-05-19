from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name = 'pyChatteringy',
    packages = ['pychatteringy', 'pychatteringy.classes', 'pychatteringy.functions', 'pychatteringy.tools'],
    include_package_data=True,

    description = "Create very simple, minimalistic Python chatbots by using JSON",
    long_description=long_description,
    long_description_content_type='text/markdown',

    version = 'v0.0.1_alpha',
    license='GPLv3',
    description = 'Create simple chatbots by using JSON & Python 3 only.',
    keywords = ['python', 'python3', 'chatbot', 'bot', 'framework', 'ai', 'json', 'intents', 'conversation'],

    author = 'Kevo',
    author_email = 'me@kevo.link',

    url = 'https://github.com/CWKevo/pyChatteringy',

    install_requires=[
        'fuzzywuzzy'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
