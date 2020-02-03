import asyncio
import glob

PATH = "lab1/"
COUNT = 1

def readInput(name):
    global COUNT
    
    with open(name) as f:
        data = [int(x) for x in f.read().split()]
    data.sort()

    with open(PATH + 'output/sorted_' + str(COUNT) + '.txt', 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)
    COUNT += 1

def sort():

    data = []
    for name in glob.glob(PATH + 'output/sorted_*.txt'):
        with open(name) as f:
            data.append([int(x) for x in f.read().split()])

    data.sort()
    with open(PATH + 'output/sorted.txt', 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)
    print("sorted.txt saved")
    
def main():

    for name in glob.glob(PATH + 'input/unsorted_*.txt'):
        readInput(name)

    sort()

if __name__== "__main__" :
    main()
