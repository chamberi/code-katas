# code-katas
This is the Code Wars work for the Snow Day assignment, day 5 of Python 401.

Fizz Buzz
- Module: fizz_buzz.py
- Tests: test_fizz_buzz.py
- Link: https://www.codewars.com/kata/fizz-buzz-cuckoo-clock/train/python


```python
def fizz_buzz_cuckoo_clock(time):
    hour = int(time[0:2])
    min = int(time[3:])
    if hour > 12: hour -= 12
    
    if min == 30: return "Cuckoo"
    elif min == 0: return ("Cuckoo " * hour).strip()
    elif min % 3 > 0 and min % 5 > 0: return "tick"
    elif min % 3 == 0 and min % 5 == 0: return "Fizz Buzz"
    elif min % 3 == 0: return "Fizz"
    elif min % 5 == 0: return "Buzz"

"""by user Dana."""
# Much more elegant than mine, but similar. I don't know the strip() function. 
```



Flatten Me
- Module: flatten_me.py
- Tests: test_flatten_me.py
- Link: https://www.codewars.com/kata/flatten-me/train/python

```python
def flatten_me(lst):
    s = []
    for i in lst:
        if isinstance(i, list):
            s.extend(i)
        else:
            s.append(i)
    return s

"""By user 文刀七禾页."""
# Really interesting use of isinstance and extend. Impressive.
```



String Reversing
- Module: string_reversing.py
- Tests: test_string_reversing.py
- Link: https://www.codewars.com/kata/string-reversing-changing-case-etc/train/python

```python
def reverseAndMirror(s1,s2):
    return (s2[::-1] + "@@@" + s1[::-1] + s1).swapcase()

"""By user AveryPratt."""
# Simple, elegant, classmate since 201. A lot simpler than my code.
```



Sum Up
- Module: sum_up.py
- Tests: test_sum_up.py
- Link: https://www.codewars.com/kata/sum-up-the-random-string/train/python

```python
import re
def sum_from_string(string):
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)

"""By User JustyFY, ChingChangChong."""
# Similar to mine, but simpler in getting to the return statement.
```


Sea Sick
- Module: seasick_snorkelling.py
- Tests: test_seasick_snorkelling.py
- Link: https://www.codewars.com/kata/holiday-v-seasick-snorkelling/train/python

```python
def sea_sick(sea):
    if (sea.count('~_') + sea.count('_~')) / len(sea) > 0.2:
        return "Throw Up"
    return "No Problem"

"""By user RudiCatela."""
#I should've thought of this method of just noting the instances of change. Again, simpler.
```



Show Muliples
- Module:
- Tests:
- Link: https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range/train/python

```python
def multiples(s1,s2,s3):
    return list(filter(lambda x: x%s1==0 and x%s2==0, list(range(1,s3))))

"""By User sdewitt."""
# I like their use of filter with lambda. Simplicity wins the day, once again.
```


Friend or Foe
- Module: friend_foe.py
- Tests: test_friend_foe.py
- Link: https://www.codewars.com/kata/friend-or-foe/train/python

```python
def friend(x):
    return filter(lambda name: len(name) == 4, x)

""" By User ISO-B and 50 others."""
# Liking the filter/lambda usage.
```


Rake Garden
- Module: rake_garden.py
- Tests: test_rake_garden.py
- Link: https://www.codewars.com/kata/help-suzuki-rake-his-garden/train/python

```python
def rake_garden(garden):
    return " ".join(i if i in "gravelrock" else "gravel" for i in garden.split())

""" By User bdarksider."""
# Not sure I understand this one, thus I'm picking this one to look at more.
```
