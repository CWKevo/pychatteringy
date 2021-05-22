### Global
- [x] Make chabot a class (with options for intent path, etc.)
- [x] Organize code, move to folders, etc...
- [x] Variables
- [x] Better README
- [x] `__init__.py` imports
- [x] Basic contextual engine - save users to another JSON file, then ability to use conditions with it.
- [x] setup.py for PIP
- [ ] Other improvements(?)

### Contexts
"Harder-to-implement" - see the `contexts` branch.
- [x] Contexts - Ability to distinguish, what's being talked about (find same context intents in JSON)
- [x] -> Uses "goto" method.
- [x] Ability to understand user answers, prompt user with question

Contexts were the hardest thing to implement... But the result is worth it! I am happy!
I don't really plan to make machine learning or advanced contextual engine. Maybe in the future? But for now,
I feel like this is a proof of concept for something simple, that can eventually become very powerful.

### Conditions & actions
- [ ] Create "IntentVariables" class to represent an action/condition pair (key, value).
- [ ] Evaluation - find a way to reduce duplicated code
- [ ] More conditions & comparsions (more, less than, not, etc.)

### Tools:
- [ ] Intent generator can understand contexts (goto methods) and multiresponses. This will be another hard thing to implement, because - how will the syntax even look like? I feel like this one is possible, but it will be another hard thing to do.


#### Example syntax (idea):

```ini
# Some intent
id      = 1

user    = Good morning! | Morning! | Rise and shine!
bot     = Morning!

if      = time==morning && some_other_condition
else    = goto=2:It is not morning


# Some goto_only intent:
id              = 2
goto_only       = true

user:yes        = Yes, it is. | Yes.
user:for_me     = It is morning for me | I have morning here.
user:no         = No, it is not. | No.

bot:yes         = goto=2:No, I am sure that it is not morning
bot:for_me      = Good for you.
bot:no          = See?

actions         = user_data=morning:{this.answer}
```
