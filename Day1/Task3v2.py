#Script that will find a specific string by phrase
import io

kek = 'My super text'
with io.open('Index.html') as file:
    for line in file:
        if kek in line:
            print(line, end='')