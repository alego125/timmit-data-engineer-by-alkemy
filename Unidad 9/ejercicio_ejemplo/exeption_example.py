import sys


def windows_interaction():
    """Function that assert with type of our operating system

       :typw: string
    """
    assert ('win32' in sys.platform), """Esta función funciona
                                         solamente en Windows"""
    print("'Sistema operativo Win32...")


try:
    windows_interaction()

except AssertionError as error:
    print(error)

else:

    try:
        with open('file.log') as file:
            read_data = file.read()
            print(read_data)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
