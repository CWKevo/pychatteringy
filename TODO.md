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

### Hardest of them all - entities:

- [x] Ability to extract variables from user query, e. g.:

```
"user": ["I want {{thing}} for {{price}}."]
```

The problem is with jaro distance - if we compare similar strings, there is no way for
the bot to know where the variable is located.

Things I have considered:
- Exact matching - user query must be same as intent defined one for us to extract variables (using the `parse` module).
- "Overlay" all words and pick those that are at the position of the variable - inacurrate when number of words and word order changes.
- Use named entity recognition library (e. g.: spaCy) - limited to English language only
- Somewhat transform the user message to intent template while preserving the user query, then extract with `parse` - impossible?
- Make user type the variables in quotes, so we can do regEx matching to find the variable - not very pleasant for users
- Parse query by finding all patterns from 2 words offset around template

- Make TODO that actually makes sense. Makes sense to me ATM, so no need to change it

**Update:** It kind of works, the only problem is that the string similarity has lower ratio with all the different stuff that user can specify now.
We can either lower the threshold or pre-evaluate the entities and them replace them in the template (this one seems like an alright solution to me).

TODO:
- [ ] Optimize for speed & make code clean (uhh...)
- [ ] Remove punctuation from entities at end ("Can I have a boat for 1 €?" will make `price` = "1 €?")

### Documentation
- [ ] Documentation
