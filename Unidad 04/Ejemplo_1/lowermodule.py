import logging

# Logs Config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt="%Y-%m-%dY%H:%M:%S%z")

# logger = logging.getLogger(__name__)


def word_count(myfile) -> int:
    """Function that take file as a parameter and open to process it extract
    and count words that contain.

    :param myfile: file that will be process
    :type myfile: file
    :return: number of words that contain
    :rtype: int
    """
    try:
        with open(myfile, "r") as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            logging.info("This file has %d words", final_word_count)
            return final_word_count
    except OSError:
        logging.critical("File can´t be read")
