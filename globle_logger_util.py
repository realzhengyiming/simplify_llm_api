# Custom Logger Using Loguru
import logging
import os
import sys

from loguru import logger

from globle_logger_config import global_config


class InterceptHandler(logging.Handler):
    loglevel_mapping = {50: 'CRITICAL', 40: 'ERROR', 30: 'WARNING', 20: 'INFO', 10: 'DEBUG', 0: 'NOTSET', }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        log = logger.bind(request_id='app')
        log.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class CustomizeLogger:

    @classmethod
    def make_logger(cls):
        os.makedirs(global_config.LOG_PATH, exist_ok=True)
        file_full_path = os.path.join(global_config.LOG_PATH, "similar_plan_graph_{time}.log")
        logger = cls.customize_logging(filepath=file_full_path, level=global_config.LOG_LEVEL, retention=global_config.LOG_RETENTION,
                                       rotation=global_config.LOG_ROTATION, format=global_config.LOG_FORMAT)
        return logger

    @classmethod
    def customize_logging(cls, filepath: str, level: str, rotation: str, retention: str, format: str):
        logger.remove()
        logger.add(sys.stdout, enqueue=True, backtrace=True, level=level.upper(), format=format)
        logger.add(filepath, rotation=rotation, retention=retention, enqueue=True, backtrace=True,
                   level=level.upper(), format=format)
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ['uvicorn', 'uvicorn.error', 'fastapi']:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]
        return logger.bind(request_id=None, method=None)


global_logger = CustomizeLogger.make_logger()
