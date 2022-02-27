
<h1 align="center">pyChatteringy</h3>

<p align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/CWKevo/pychatteringy.svg)](https://github.com/CWKevo/pychatteringy/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/CWKevo/pychatteringy.svg)](https://github.com/CWKevo/pychatteringy/pulls)
  [![License](https://img.shields.io/badge/license-GPL%203.0-blue.svg)](https://github.com/CWKevo/pychatteringy/LICENSE)

</p>

<p align="center"> Create simple chatbots by using JSON. Built with ♥ and Python
    <br/> 
</p>

## Note:

This project is unmaintained, and is planned to be replaced with [MoZog](https://github.com/CWKevo/MoZog). I made this back when I knew very little about Python
and chatbots & AI in general. But it's a working concept, so you can look around to see how I handled things.

## 📝 Table of Contents
- [📝 Table of Contents](#-table-of-contents)
- [🧐 About <a id="about"></a>](#-about-)
- [🏁 Installation <a id="installation"></a>](#-installation-)
  - [🚦 Prerequisites](#-prerequisites)
  - [🩹 Updating](#-updating)
- [🚀 Quickstart <a id="quickstart"></a>](#-quickstart-)
- [⛏️ Built Using <a id="built_using"></a>](#️-built-using-)
- [✍️ Authors <a id="authors"></a>](#️-authors-)

## 🧐 About <a id="about"></a>
This package aims to provide users a simple way to create simple chatbots by using JSON.

## 🏁 Installation <a id="installation"></a>
It is very easy to get the basic chatbot running or integrate it in your application.

<br/>

### 🚦 Prerequisites
This project is in alpha/testing stage, but the bare minimum works.

See [TODO.md](https://github.com/CWKevo/pyChatteringy/tree/main/TODO.md) for a to-do list.

<br/>

> ---
> ### Note:
> This project was tested against Python 3.9 only.
> Python 3.6+ should work, but wasn't tested (yet - perhaps you'd like to give it a go?)
> 
> ---

```s
$ pip install pychatteringy
```

### ⬆️ Updating

```s
$ pip install pychatteringy --update
```

## 🚀 Quickstart <a id="quickstart"></a>

To create a basic & minimal chatbot with included example intents, use:

```python
# Import the ChatBot class:
from pychatteringy.classes.chatbot import ChatBot

# Initialize chatbot:
chatbot = ChatBot()


# Store response to query "Hi!" in a variable:
response = chatbot.chat("Hi!")
# Print the response:
print(response)
```

The code above is very simple. It obtains a response from a chatbot and then returns it.

TODO: More documentation

## ⛏️ Built Using <a id="built_using"></a>
- [Python](https://www.python.org/) - Programming language

## ✍️ Authors <a id="authors"></a>
- [@CWKevo](https://github.com/CWKevo) - Main owner & maintainer

See also the list of [contributors](https://github.com/CWKevo/pyChatteringy/contributors) who participated in this project.

## 🎁 Support me

I create free software to benefit people.
If this project helps you and you like it, consider supporting me by donating via cryptocurrency:

<!------------------!------------------------------------------------------------------------------------------------!-->
| Crypto:           | Address:                                                                                          |
|-------------------|---------------------------------------------------------------------------------------------------|
| Bitcoin           | [E-mail me](mailto:me@kevo.link)                                                                  |
| Ethereum          | `0x12C598b3bC084710507c9d6d19C9434fD26864Cc`                                                      |
| Litecoin          | `LgHQK1NQrRQ56AKvVtSxMubqbjSWh7DTD2`                                                              |
| Dash              | `Xe7TYoRCYPdZyiQYDjgzCGxR5juPWV8PgZ`                                                              |
| Zcash:            | `t1Pesobv3SShMHGfrZWe926nsnBo2pyqN3f`                                                             |
| Dogecoin:         | `DALxrKSbcCXz619QqLj9qKXFnTp8u2cS12`                                                              |
| Ripple:           | `rNQsgQvMbbBAd957XyDeNudA4jLH1ANERL`                                                              |
| Monero:           | `48TfTddnpgnKBn13MdJNJwHfxDwwGngPgL3v6bNSTwGaXveeaUWzJcMUVrbWUyDSyPDwEJVoup2gmDuskkcFuNG99zatYFS` |
| Bitcoin Cash:     | `qzx6pqzcltm7ely24wnhpzp65r8ltrqgeuevtrsj9n`                                                      |
| Ethereum Classic: | `0x383Dc3B83afBD66b4a5e64511525FbFeb2C023Db`                                                      |
<!------------------!------------------------------------------------------------------------------------------------!-->

More cryptocurrencies are supported. If you are interested in donating with a different one, please [E-mail me](mailto:me@kevo.link).
No other forms of donation are currently supported.
