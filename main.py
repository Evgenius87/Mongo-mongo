from reed import *
from conect import connect
from pprint import pprint



class InputError(Exception):
   pass

def input_error(func):
    def inner(*args):
        try:
            result  = func(*args)
            return result

        except InputError as err:
             print(f'{err}: Unknwn comand! Please try again')
    return inner




STARTTEXT = """Hello"""

@input_error
def help(args):
    return "please, donate 100$ to my card: 4149 4993 9533 8047"

@input_error
def exit(args):
    return "Good Buy!"

@input_error
def name(args):
    return find_qoutes_by_name(args)

@input_error
def tag(args):
    return find_quotes_by_tags(args)

@input_error
def tags(args):
    split_args = args[0].split(",")
    return find_quotes_by_tags(split_args)
   

@input_error
def quotes(*args):
    pass

COMMANDS = {
    "help":help,
    "exit":exit,
    "name":name,
    "tag":tag,
    "tags":tags,
    "quotes":quotes
    }

def input_parser(text: str):
    arg_list = text.split(":")
    if len(arg_list) > 1:
        command = arg_list[0]
        args = arg_list[1].strip().split(" ")
        return command, args
    else:
        command = arg_list[0]
        args = None
        return command, args

def main():
    print(STARTTEXT)
    while True:
        command, args = input_parser(input("add yuor command>>> "))
        if args:
            handler = (COMMANDS[command])
            if handler(args) != None:
                pprint(handler(args))                    
        else:
            handler = (COMMANDS[command])
            pprint(handler(args))        
            if handler(args) == "Good Buy!":
                break


if __name__ == "__main__":
    main()