import main
import logging
import logging.config

logging.config.fileConfig('log_config_file.conf',
                          disable_existing_loggers=False)

loggerMain = logging.getLogger("loggerMain")
loggerFunction = logging.getLogger("loggerFunction")


def extract_information(file, opened_file):
    """Function that go throw the lines of opened file and extract information to be logged in logger object
    """

    loggerFunction.info(f"""{str(file)}
                            Cantidad de renglones: {len(opened_file)}""")

    # Read line by line and split text in line to obtain len of line and show it in a log
    for line, content in enumerate(opened_file):
        palabras = content.split(" ")
        loggerFunction.info(f"Renglón {line}: {len(palabras)} palabras")


if __name__ == '__main__':
    main.main("cuento.txt")
