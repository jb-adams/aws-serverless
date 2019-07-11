import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello_func(event, context):
    logging.info("Hello World")
    logging.info("This was executed on AWS Lambda")
    logging.info("Great Work")
    return {
        "message": "AWS Lambda is Cool"
    }