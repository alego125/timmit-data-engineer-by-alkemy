import functions


def main(file):

    functions.loggerMain.info("...Leyendo el archivo...")

    try:
        with open(file, "r") as f:
            open_file = f.readlines()
            functions.loggerMain.info("...Archivo procesado...")
            functions.extract_information(file, open_file)
    except Exception:
        functions.loggerMain.error("No se pudo abrir el archivo",
                                   exc_info=True)
    return open_file
