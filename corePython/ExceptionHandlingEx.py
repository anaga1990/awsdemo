# ZeroDivisionError: division by zero
# def division_of_two_numbers(n1, n2):
#     c = n1 / n2
#     print(str(c))
#
#
# division_of_two_numbers(10, 0)

################################
# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# def division_of_two_numbers(n1, n2):
#     c = n1 / n2
#     print(str(c))
#
#
# division_of_two_numbers(10, 'nana')
##############################################################
# handling exceptions
def division_of_two_numbers(n1, n2):
    try:
        c = n1 / n2
        print(str(c))
        c = c+1
    except:
        print("exception with your code")
        raise Exception
    else:
        print("has no error else block executed")
    finally:
        print("finally block run always")

division_of_two_numbers(10, 0)