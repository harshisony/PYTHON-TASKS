#'__name__'is a special built-in variable in Python that stores the name of the current module.
#When a Python script is executed, Python sets the __name__ variable of the script to '__main__' if it's the main module being run directly.
#If the script is imported as a module into another script, the __name__ variable is set to the name of the module.

def main():
    print("This code will only run if the script is executed directly.")

if __name__ == '__main__':
    main()


#In this example, the main() function will only be called when the script is run directly. If the script is imported as a module into another script, 
# the main() function will not be automatically called.