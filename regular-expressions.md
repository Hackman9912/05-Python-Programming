# Regular Expressions

Regular expressions, often referred to as REs or regexes, are bits of small and highly specialized programming language embedded inside Python. The PyDocs actually contains an entire page on how to use regex. We will be touching on some of it's functionality... it'll be up to you to utilize the PyDocs and take your knowledge to the next level.

**PyDocs HOWTO**

[https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html)

**PyDocs Re**

[https://docs.python.org/2/library/re.html](https://docs.python.org/2/library/re.html)

### Using Regular Expressions

**re.compile: **compiles regular expression into pattern objects which allows for repeated use

**re.match: **apply pattern to the start of string, return match or None

**re.search: **scan through string, return match or None

**Python re search and compile example:**

```py
import re

search_str = "This is a string to search"
re_search = re.compile("string")
matched_obj = re_search.search(search_str)

print matched_obj
```

```
<_sre.SRE_Match object at 0x02CBFA68>
```

**Practical Example**

```py
import re

patterns = ['Enterprise', 'Death Star']
pharse = "The Enterprise is the flagship of the Federation."

for pattern in patterns:
    print 'Looking for "{}" in "{}": '.format(pattern, pharse)

    if re.search(pattern, pharse):
        print "found a match!"
    else:
        print "no match!"
```

```
Looking for "Enterprise" in "The Enterprise is the flagship of the Federation.":
found a match!
Looking for "Death Star" in "The Enterprise is the flagship of the Federation.":
no match!
```

**Python re search start\(\) and end\(\):**

```py
import re

pattern = "Dave"
text = "I'm sorry Dave, I'm afarid I can't do that."

match = re.search(pattern, text)

start = match.start()
end = match.end()

print 'Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, start, end, text[start:end])
```

```
Found "Dave" in "I'm sorry Dave, I'm afarid I can't do that." from 10 to 14 ("Dave")
```


