"""Файл конфигурации, в данном файле могут храниться CSRF токены или подключение к БД"""

from pathlib import Path
import yaml

__all__ = ('load_config', )


def load_config(config_file=None):
    """Функция для чтения конфигурационного файла"""
    # Определяем путь к конфигурационному файлу
    default_file = Path(__file__).parent / 'config.yaml'
    # Считываем файл при помощи модуля yaml и загружаем в словарь config
    with open(default_file, 'r') as f:
        config = yaml.safe_load(f)

    config_dict = {}
    if config_file:
        config_dict = yaml.safe_load(config_file)
    # Обновляем значение словаря на значения из config
    config.update(**config_dict)

    return config
