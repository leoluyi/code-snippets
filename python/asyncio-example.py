'''Asyncio - demo

https://www.youtube.com/watch?v=BI0asZuqFXM
https://www.youtube.com/watch?v=3mb9jFAHRfw
https://www.youtube.com/watch?v=tSLDcRkgTsY
https://xinhuang.github.io/posts/2017-07-31-common-mistakes-using-python3-asyncio.html
'''
import asyncio


async def find_divisibles(inrange, div_by):
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
        print(d1.result()[:5])
    except Exception as e:
        raise e
    finally:
        loop.close()
