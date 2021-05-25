
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
