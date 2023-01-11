import os
from typing import Any


_DEBUG = os.environ.get("DEBUG", True)


def _get_env(key: str, default: Any) -> Any | None:
	# В случае продакшн окружения предпочитаю прямое обращение к ключам енвов
	if _DEBUG is True:
		return os.environ.get(key, default)
	return os.environ[key]


class ProjectConfig:
	DEBUG = _DEBUG

	APP_HOST = _get_env("APP_HOST", "127.0.0.1")
	APP_PORT = _get_env("APP_PORT", 8000)


class DatabaseConfig:
	DB_NAME = _get_env("DB_NAME", "vidita_systems")
	DB_USER = _get_env("DB_USER", "vidita_systems")
	DB_PASSWORD = _get_env("DB_PASSWORD", "vidita_systems")
	DB_HOST = _get_env("DB_HOST", "localhost")
	DB_PORT = _get_env("DB_PORT", 5432)

	DB_DSN = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
