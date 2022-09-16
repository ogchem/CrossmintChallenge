# import requests library

import requests

# run requests GET function on goal endpoint to obtain goal list

r = requests.get('https://challenge.crossmint.io/api/map/b07235fd-d1a5-4b33-b646-7474a37182cd/goal')

# assigning variable "l" to goal map json to parse through and printing it

l = r.json()
print(l)

# assigning variables for each loop

auth_token = 'b07235fd-d1a5-4b33-b646-7474a37182cd'
apiurl = 'https://challenge.crossmint.io/api/'

# running the loop for list obtained from goal map endpoint
# using row as rows and index as columns, assigning auth token as authorization

#post all polyanets on map

for index, j in enumerate(l['goal']):
     for row, n in enumerate(j):
        payload = {'row': row, 'column': index, 'candidateId': auth_token}
        if n.lower() == 'polyanet':
            res = requests.post('https://challenge.crossmint.io/api/polyanets', data=payload)
            print("Posted Polyanets ", n)

#post all up_comeths, switched index location to row and not column

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'direction': 'up'}
        if n.lower() == 'up_cometh':
            res = requests.post('https://challenge.crossmint.io/api/comeths', data=payload)
            print("Posted Up Comeths ", n)

#post all down_comeths, switched index location to row and not column

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'direction': 'down'}
        if n.lower() == 'down_cometh':
            res = requests.post('https://challenge.crossmint.io/api/comeths', data=payload)
            print("Posted Down Comeths ", n)

#post all left_comeths, switched index location to row and not column

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'direction': 'left'}
        if n.lower() == 'left_cometh':
            res = requests.post('https://challenge.crossmint.io/api/comeths', data=payload)
            print("Posted Left Comeths ", n)

#post all right_comeths, switched index location to row and not column

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'direction': 'right'}
        if n.lower() == 'right_cometh':
            res = requests.post('https://challenge.crossmint.io/api/comeths', data=payload)
            print("Posted Right Comeths ", n)

#post blue soloons

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'color': 'blue'}
        if n.lower() == 'blue_soloon':
            res = requests.post('https://challenge.crossmint.io/api/soloons', data=payload)
            print("Posted Blue Soloons ", n)

#post red soloons

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'color': 'red'}
        if n.lower() == 'red_soloon':
            res = requests.post('https://challenge.crossmint.io/api/soloons', data=payload)
            print("Posted Red Soloons ", n)

#post purple soloons

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'color': 'purple'}
        if n.lower() == 'purple_soloon':
            res = requests.post('https://challenge.crossmint.io/api/soloons', data=payload)
            print("Posted Purple Soloons ", n)

#post white soloons

for index, j in enumerate(l['goal']):
     for column, n in enumerate(j):
        payload = {'row': index, 'column': column, 'candidateId': auth_token, 'color': 'white'}
        if n.lower() == 'white_soloon':
            res = requests.post('https://challenge.crossmint.io/api/soloons', data=payload)
            print("Posted White Soloons ", n)