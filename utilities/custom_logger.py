import logging

def configure_logger(log_file, logger_name):

    logger = logging.getLogger(logger_name)
    # Set the logging level to INFO
    logger.setLevel(logging.INFO)
    # Sample output : 2023-10-13 11:48:48,386 - test_login - INFO - <message>
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # A file handler to write logs to a file with the specified filename
    file_handler = logging.FileHandler("automation.log", mode='w')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger