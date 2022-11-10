import logging
import lowermodule

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt="%Y-%m-%dY%H:%M:%S%z")
logger = logging.getLogger(__name__)


def record_word_count(myfile):
    logger.info("Starting the function")
    try:
        word_count = lowermodule.word_count(myfile)
        with open('wordcounter.csv', 'a') as file:
            row = str(myfile) + ',' + str(word_count)
            file.write(row + '\n')
    except Exception:
        logger.warning("Could not write file %s to destination", myfile)
    finally:
        logger.debug("The function is done for the file %s", myfile)


def main():
    record_word_count("texto_prueba.txt")


if __name__ == '__main__':
    main()
