#one.py

def func():
    print('func() in one.py')

print('top level in one.py')

if __name__ == '__main__':
    #Define functions above and use this script to run them
    #when the script is run directly.
    print('one.py is being run directly!')
else:
    print('one.py has been imported')
