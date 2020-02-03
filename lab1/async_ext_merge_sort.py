# 
# import glob

# PATH = "lab1/"
# COUNT = 1

# def readInput(name):
#     global COUNT
    
#     with open(name) as f:
#         data = [int(x) for x in f.read().split()]
#     data.sort()

#     with open(PATH + 'output/sorted_' + str(COUNT) + '.txt', 'w') as filehandle:
#         for listitem in data:
#             filehandle.write('%s\n' % listitem)
#     COUNT += 1
#     # await asyncio.sleep(0.1)

# def sort():

#     data = []
#     for name in glob.glob(PATH + 'output/sorted_*.txt'):
#         with open(name) as f:
#             data.append([int(x) for x in f.read().split()])

#     data.sort()
#     with open(PATH + 'output/async_sorted.txt', 'w') as filehandle:
#         for listitem in data:
#             filehandle.write('%s\n' % listitem)
#     print("async_sorted.txt saved")

# def main():

#     for name in glob.glob(PATH + 'input/unsorted_*.txt'):
#         # loop.create_task(readInput(name)) 
#         readInput(name)

#     sort()

# if __name__== "__main__" :
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
#     main()

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
    
    # await asyncio.gather(
    #     readInput("lab1/input/unsorted_1.txt"),
    #     readInput("lab1/input/unsorted_2.txt"),
    #     readInput("lab1/input/unsorted_3.txt"),
    #     readInput("lab1/input/unsorted_4.txt"),
    #     readInput("lab1/input/unsorted_5.txt"),
    #     readInput("lab1/input/unsorted_6.txt"),
    #     readInput("lab1/input/unsorted_7.txt"),
    #     readInput("lab1/input/unsorted_8.txt"),
    #     readInput("lab1/input/unsorted_9.txt"),
    #     readInput("lab1/input/unsorted_10.txt"),
    # )
    for name in glob.glob(PATH + 'input/unsorted_*.txt'):
        await loop.create_task(readInput(name)) 

    # await tasks
    sort()

if __name__== "__main__" :
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
