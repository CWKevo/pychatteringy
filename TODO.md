- [x] Make chabot a class (with options to intent paths, etc...)
- [x] Organize code, move to folders, etc...
- [x] Variables
- [x] Better README
- [ ] `__init__.py` imports
- [ ] More conditions & comparsions (more, less than, not, etc.) - might result in duplicated code, find a way to organize it
- [x] Basic contextual engine - save users to another JSON file, then ability to use conditions like "hastalked", if bot has talked to that user yet, etc.
- [ ] Other improvements(?)
- [x] setup.py for PIP

"Harder-to-implement" - see the `contexts` branch.
- [x] Contexts - Ability to distinguish, what's being talked about (find same context intents in JSON)
- [x] -> Uses "goto" method.
- [x] Ability to understand user answers, prompt user with question


Contexts were the hardest thing to implement... But the result is worth it! I am happy!
I don't really plan to make machine learning or advanced contextual engine. Maybe in the future? But for now,
I feel like this is a proof of concept for something simple, that can eventually become very powerful.

Tools:
- [ ] Intent generator can understand contexts (goto methods) and multiresponses. This will be another hard thing to implement, because - how will the syntax even look like? I feel like this one is possible, but will be another hard thing to do.
