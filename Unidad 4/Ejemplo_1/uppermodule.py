import logging
import lowermodule
from pathlib import Path

# Create paths files
txtPath = f"{Path(__file__).parent}/texto_prueba.txt"
# Extract file name that be into the txtPath
fileName = txtPath.split('/')[-1]

csvPath = f"{Path(__file__).parent}/wordcounter.csv"

# Logs config
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
                    datefmt="%Y-%m-%dY%H:%M:%S%z")
# logger = logging.getLogger(__name__)


def record_word_count(myfile) -> None:
    """Function that call word_count function that extract the number of words that
    contain and file and number of words into csv file.

    :param myfile: file that will be process
    :type myfile: file
    """

    logging.info("Starting the function")

    try:
        word_count = lowermodule.word_count(myfile)

        with open(csvPath, 'a') as file:
            row = str(fileName) + ',' + str(word_count)
            file.write(row + '\n')

    except Exception:
        logging.warning("Could not write file to destination")

    finally:
        logging.debug("Process finished")


def main():
    record_word_count(txtPath)


if __name__ == '__main__':
    main()
