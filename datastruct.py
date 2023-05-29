import pprint
cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})
print(allCats)

# Compare this snippet from tic_tac_toe.py:
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)
print(theBoard['top-L'])

theBoard['mid-M'] = 'X'
theBoard['top-L'] = 'O'
theBoard['top-R'] = 'O'
theBoard['top-M'] = 'X'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'O'
theBoard['low-L'] = 'X'
theBoard['low-M'] = 'O'
theBoard['mid-R'] = 'X'

pprint.pprint(theBoard)


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)

type(42)
print(type(42))
type('hello')
print(type('hello'))
type(theBoard)
print(type(theBoard))
print(type(theBoard['top-L']))
