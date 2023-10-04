import sys

def get_int():
    while True:
        try:
            number = int(input("enter a number"))
            return number
        except ValueError:
            print('incorrect number enter new number')
        except EOFError:
            sys.exit(1)
        finally:
            print('this will always execute')
            # this would include closing db cursors

first_no = get_int()
second_no = get_int()

try:
    print("divide {} by {} to get {}".format(first_no,second_no,first_no/second_no))
except ZeroDivisionError:
    print("cant divide by zero")
    sys.exit(2)
else:
    print('divison performed successfully')
finally:
    print('will it still execute always, Yes')
