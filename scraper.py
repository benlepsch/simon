'''
    1. go to mountainproject.com/route-finder for <state id>
    2. check number of climbing routes
        if # < 1000: 
            export to csv
        if # > 1000:
            export each difficulty lvl to its own csv
            combine into one mega csv
    3. proceed to next state id
    
    export directly to csv:
    https://www.mountainproject.com/route-finder-export
    
    what about by difficulty?
    diffMinrock = 1000 = 5.0
    diffMaxrock = 1100 = 5.1
    2000 = 5.8-
    2100 = 5.8
    2200 = 5.8+

    setting both to the same value gives only routes with that exact grade
    this is good

    oh it gets weird though
    2600 = 5.10a
    2700 = 5.10-
    2800 = 5.10a/b
    2900 = 5.10b
    3000 = 5.10
    3400 = 5.10c
    3500 = 5.10d
    4600 = 5.11a
    4800 = 5.11a/b? or 5.11b?

    really this doesn't matter
    any number thats divisible by 100 seems to be fine
    i can just go one difficulty level at a time if the csv file has more than 1000 rows
'''

import json, requests

f = open('states-ids.json')
ids = json.load(f)

def get_url(id = 0, minD = 1000, maxD = 12400, preview = True):
    base_url = 'https://mountainproject.com/route-finder?selectedIds={}&diffMinrock={}&diffMaxrock={}'
    base_url = base_url.format(id, minD, maxD)

    if preview:
        return base_url
    return base_url.split('?')[0] + '-export?' + base_url.split('?')[1]


splitter = 'Sorted by Popularity then Difficulty. Results 1 to ' # 50 of 1000.

for state, id in ids.items():
    page = requests.get(get_url(id)).text
    temp = page.split(splitter)[1][6:10] 
    
    if temp == '1000':
        print('{} has more than 1000 routes'.format(state))

# csv = requests.get(get_url(ids['Virginia'], preview=False)).text
# with open('out.csv', 'w') as of:
#     of.write(csv)

