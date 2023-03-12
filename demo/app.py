"""Конструктор приложения, позволяет создать приложение со всеми вложенными частями"""
from aiohttp import web

import jinja2
import aiohttp_jinja2

from .routes import set_routes


async def create_app():
    """Создаём приложение"""
    app = web.Application()
    # Подключаем поддержку jinja шаблонов
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('demo', 'templates'))
    set_routes(app)
    return app
