import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt="%Y-%m-%dY%H:%M:%S%z")
logger = logging.getLogger(__name__)


def word_count(myfile):
    try:
        with open(myfile, "r") as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            logger.info("This file has %d words", final_word_count)
            return final_word_count
    except OSError:
        logger.critical("Imposible leer el archivo")
