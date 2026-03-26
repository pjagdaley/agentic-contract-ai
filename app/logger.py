import logging

def setup_logger():

    logger = logging.getLogger("agentic_ai")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("app.log")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger