import os

LOG_FORMAT = "{level: <8} {time:YYYY-MM-DD HH:mm:ss} request id:{extra[request_id]} - {name}:{function} - {message}"


class EnvConfig:  # 部署远程时候使用
    def __init__(self):
        print("global logger config 从环境变量中读取")
        self.log_level = os.environ.get("LOGGING_LEVEL", "INFO")
        self.log_path = os.environ.get("LOGGING_LOCATION", "/tmp")
        self.log_rotation = os.environ.get("LOGGING_RETENTION", "480h")
        self.log_retention = os.environ.get("LOGGING_ROTATION", "720h")
        self.log_format = LOG_FORMAT

    @property
    def LOG_LEVEL(self):
        return self.log_level

    @property
    def LOG_PATH(self):
        return self.log_path

    #
    @property
    def LOG_RETENTION(self):
        return self.log_retention

    #
    @property
    def LOG_ROTATION(self):
        return self.log_rotation

    @property
    def LOG_FORMAT(self):
        return self.log_format


global_config = EnvConfig()
