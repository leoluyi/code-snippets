import sys

if __name__ == '__main__':
    print(f'>> sys.argv={sys.argv}')

print(f'>> __file__="{__file__}"\n>> __name__="{__name__}"\n>> __package__="{__package__}"')
print('--------------------------------------------------------------------')

from ..my_module import say_hi
say_hi()
