'''Asyncio - demo

- https://pythonprogramming.net/asyncio-basics-intermediate-python-tutorial/
- [Asyncio - Asynchronous programming with coroutines](https://www.youtube.com/watch?v=BI0asZuqFXM)
- [Gregory Saunders - A Really Gentle Introduction to Asyncio](https://www.youtube.com/watch?v=3mb9jFAHRfw)
- [Miguel Grinberg - Asynchronous Python for the Complete Beginner](https://www.youtube.com/watch?v=iG6fr81xHKA&feature=youtu.be&t=4m29s)
- [Python tricks: Demystifying async, await, and asyncio](https://www.youtube.com/watch?v=tSLDcRkgTsY)
- [Common Mistakes Using Python3 asyncio](https://xinhuang.github.io/posts/2017-07-31-common-mistakes-using-python3-asyncio.html)
'''
import asyncio


async def find_divisibles(inrange, div_by):
    """A time-comsuming job

    [description]
    """
    print(f'Finding nums in range {inrange} divisible by {div_by} ...')

    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            # the magic trick to make function really async:
            # hang over the processing time to the event loop
            await asyncio.sleep(0.000001)

    print(f'(Done with nums in range {inrange} divisible by {div_by})')
    return located


async def main():
    '''event loop'''

    div1 = loop.create_task(find_divisibles(5000000, 42713))
    div2 = loop.create_task(find_divisibles(1000000, 112))
    div3 = loop.create_task(find_divisibles(6000, 22))
    await asyncio.wait([div1, div2, div3])

    return div1, div2, div3


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(True)
        d1, d2, d3 = loop.run_until_complete(main())

        # d1, d2, d3 = asyncio.run(main())  # Python 3.7+
        '''asyncio Face Lift

        https://realpython.com/python37-new-features/#asyncio-face-lift

        Using asyncio.run(), you do not need to explicitly create the event loop.
        '''

        print(d1.result()[:5])
    except Exception as e:
        raise e
    finally:
        # You always want to close the loop.
        loop.close()
        pass
