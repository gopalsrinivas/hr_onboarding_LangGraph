import logging


def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # File handler
    fh = logging.FileHandler("app.log")
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)

    # Stream handler
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger
