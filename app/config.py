import os


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = os.getenv("JWT_SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(BaseConfig):
    ENV_NAME = "development"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dev.db")


class TestingConfig(BaseConfig):
    ENV_NAME = "testing"
    TESTING = True


class ProductionConfig(BaseConfig):
    ENV_NAME = "production"


CONFIG_MAP = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
