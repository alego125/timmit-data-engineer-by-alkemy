import main
import logging
import logging.config

logging.config.fileConfig('log_config_file.conf',
                          disable_existing_loggers=False)

loggerMain = logging.getLogger("loggerMain")
loggerFunction = logging.getLogger("loggerFunction")


def extract_information(file, opened_file):
    """
        function that Call obtain_stoy function and open
        txt file and extract information, then log l
    """

    loggerFunction.info(f"""{str(file)}
                            Cantidad de renglones: {len(opened_file)}""")

    for line, content in enumerate(opened_file):
        palabras = content.split(" ")
        loggerFunction.info(f"Renglón {line}: {len(palabras)} palabras")


if __name__ == '__main__':
    main.main("cuento.txt")
