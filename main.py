import json

from task_1 import full_name
from task_2 import thirty_and_above

with open("assets/user.json") as f:
    data = json.load(f)

# task 1
# full_name(data)

# task 2
thirty_and_above(data)
