'''
    this file downloads all the route data for each state in the USA as .csv

    1. go to mountainproject.com/route-finder for <state id>
    2. check number of climbing routes
        if # < 1000: 
            export to csv
        if # > 1000:
            export each difficulty lvl to its own csv
            combine into one mega csv? or save for database
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

# failed: Connecticut, missouri, 

import json, requests, asyncio

f = open('states-ids.json')
ids = json.load(f)
csv_dir = 'csvs/'

def get_url(id = 0, minD = 1000, maxD = 12400, preview = True):
    base_url = 'https://mountainproject.com/route-finder?selectedIds={}&diffMinrock={}&diffMaxrock={}'
    base_url = base_url.format(id, minD, maxD)

    if preview:
        return base_url
    return base_url.split('?')[0] + '-export?' + base_url.split('?')[1]

async def get_csv(state, id, minD = 1000, maxD = 12400):
    csv = requests.get(get_url(id, minD, maxD, False)).text
    if not len(csv) == 112:
        fstr = csv_dir + state + (str(minD) if minD == maxD else '') + '.csv'
        with open(fstr, 'w') as outfile:
            outfile.write(csv)


splitter = 'Sorted by Popularity then Difficulty. Results 1 to ' # 50 of 1000.
tasks = []

async def go():
    for state, id in ids.items():
        # if (not state == "Connecticut") or (not state == "Missouri"):
        #     continue
        page = requests.get(get_url(id)).text
        temp = page.split(splitter)[1][6:10] 
        
        if temp == '1000':
            for i in range(1000, 12400, 100):
                task = asyncio.create_task(get_csv(state, id, i, i))
                tasks.append(task)
            # print('{} has more than 1000'.format(state))
        else:
            task = asyncio.create_task(get_csv(state, id))
            # pass

    await asyncio.gather(*tasks)

asyncio.run(go())

# csv = requests.get(get_url(ids['California'], 12400, 12400, preview=False)).text
# print(len(csv))

