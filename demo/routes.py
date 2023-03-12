"""Роуты для приложения"""
from .views import frontend


def set_routes(app):
    """Функция для инициализации роутеров"""
    app.router.add_route('GET', '/', frontend.index)
