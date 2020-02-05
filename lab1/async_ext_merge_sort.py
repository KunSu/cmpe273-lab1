import asyncio
import glob

PATH = "lab1/"
COUNT = 1

async def readInput(name):
    global COUNT
    
    with open(name) as f:
        data = [int(x) for x in f.read().split()]
    data.sort()

    
    with open(PATH + 'output/sorted_' + str(COUNT) + '.txt', 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)
    COUNT += 1
    await asyncio.sleep(0.001)
    

def sort():

    data = []
    for name in glob.glob(PATH + 'output/sorted_*.txt'):
        with open(name) as f:
            data.append([int(x) for x in f.read().split()])

    data.sort()
    with open(PATH + 'output/async_sorted.txt', 'w') as filehandle:
        for listitem in data:
            filehandle.write('%s\n' % listitem)
    print("async_sorted.txt saved")
    
async def main():
    
    for name in glob.glob(PATH + 'input/unsorted_*.txt'):
        await loop.create_task(readInput(name)) 

    sort()

if __name__== "__main__" :
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
