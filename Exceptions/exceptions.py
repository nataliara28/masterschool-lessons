# Exceptions
# Errors that occur during runtime
#
# print('start')
# if True:
#     print("Hello, World!")
#
# try:
#     result = '2' + 2 # typeError
# except TypeError as e:
#     print('Error here!', e)
# except ValueError as e:
#     print(e)

# except (TypeError, ValueError):
#     print('Invalid input')

# except Exception:
#     print('Error')

#num = int("abc") # ValueError



# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(e)


# def add_two(num):
#     return num + 2

# try:
#     number = int(input('Enter a number: '))
#     result = add_two(number)
#
#     print(result)
#
# except ValueError as e:
#     print('Error: ', e)
#
# else:
#     print('Else block: If not exceptions, this print will run')
#
# finally:
#     print('Finally block: This always run')
#
#
# print('end')

# def check_positive(number):
#     if number <= 0:
#         raise Exception("The number must be positive. ")
#     else:
#         return f"The number {number} is positive"
#
# try:
#     print(check_positive(12))
#     print(check_positive(-12))
# except Exception as e:
#     print(e)


# my_list = [1, 2, 3]
#
# try:
#     print(my_list[5])
# except IndexError:
#     print("Error indexerror")

# Conditions
# def to_uppercase(text):
#     #if type(text) == str:
#     if isinstance(text, str):
#         return text.upper()
#     else:
#         return 'Please enter a correct value'


# Handling Exceptions
def to_uppercase(text):
    try:
        result = text.upper()
    except AttributeError as e:
        return "Error: Input must be string"
    else:
        # If not error raised, return result
        return result
    finally:
        print("Operation complete")



print(to_uppercase("hello"))
print(to_uppercase(34))
