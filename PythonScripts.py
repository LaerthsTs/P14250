# 2
from pynput.keyboard import Key, Listener
    
path = "output1.txt"
content = open(path, "w")
counter = 0

def on_press(key):
    print(str(key))
    global counter
    if key in [Key.space, Key.delete, Key.backspace, Key.tab]:
        counter = counter + 1
    
def on_release(key):
    if key == Key.esc:
        return False

print('Input characters: (Press \'ESC\' to exit.)')
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

content.write("Illegal key buttons and whitespaces found: " + str(counter))
content.close()
print('Program ended')


# 3
import re

path = "cppcode.txt"
file = open(path, "r")
content = file.read()

matches = re.findall("(\/\*(.*|[\s\S]*)\*\/|\/\/(.*))", content)
for match in matches:
    print(match[0])
file.close()


# 5
import requests
from collections import Counter
from bs4 import BeautifulSoup

url = 'https://google.com/'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style'
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print("Text of url:")
print(output)
print()

character_popularities = Counter(x for x in output if not x.isspace()).most_common()
print("Most popular character: \'" + str(character_popularities[0][0]) + "\', with count: " + str(character_popularities[0][1]))


# 10

def checkBalancedParenthesis(line):  
    # input additional parentheses types if you want
    open_tup = tuple('(') # tuple('[(etc')
    close_tup = tuple(')') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
  
    for i in line: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return False
    return True
  
while True:
    inputString = input("Input line (enter \'Exit\' to stop):")
    if inputString.lower() == "exit":
        break
    result = checkBalancedParenthesis(inputString)
    if result == True:
        print("Line is balanced")
    else:
        print("Line is unbalanced")
