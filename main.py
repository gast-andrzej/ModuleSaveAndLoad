def ModuleSaveAndLoad(index = int(input('If you want to load data select 1\nif you want to save data select 2\n'))):
    '''
    This module of saving and loading a data element is based on the binary system and conversion of individual elements
    of the dictionary entry to the values corresponding to it in the ASCII table. These values are then converted to a
    physical binary value in the form of a variable in a file (.py). A separate file (.py) is created for each dictionary
    saved in this way, which allows you to store the save data on the local side of the user.

    If you want to rebuild the save elements, just rebuild the save function according to the parameters indicated
    in the comment below it. Don't forget to add only your dict as a variable to the function when writing, or
    the path to it. ;-)

    '''
    save = lambda n: open(f"save{n}.py","w").write(f"save = {str(list(bin(ord(i)) for i in str(dict(zip(list(range(100)), list(__import__('string').ascii_letters))))))}")
    # save = lambda n: open(f"save{n}.py","w").write(f"save = {str(list(bin(ord(i)) for i in Your_dict_here_or_path_to_your_dict))}")

    '''
    The load function loads the saved dict using encapsulation conversions from the physical layer to 
    the finished dictionary layer. It can also be used as the final variable of the function and passed 
    on for further processing.
    '''

    load = lambda n : print(__import__("ast").literal_eval(str(''.join(i for i in list(chr(int(i,2)) for i in __import__(f"save{n}").save)))))
    # if you want to use load as a var look at the commented out code below and in the case for it ;)
    # load = lambda n : __import__("ast").literal_eval(str(''.join(i for i in list(chr(int(i,2)) for i in __import__(f"save{n}").save))))


    match index:
        case 1:
            load(int(input('Which save you want to load? ')))
            # Never Fear, case for load is here :D

            # here is your out var ;)
            # out_var = load(int(input('Which save you want to load? ')))
            # return out_var
        case 2:
            save(int(input('Select save number: ')))

if __name__ == "__main__":
    ModuleSaveAndLoad()
    # Example using ModuleSaveAndLoad as a variable load data print(ModuleSaveAndLoad().items())