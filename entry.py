""" Здесь создаётся объект application. Данный файл используется в качестве загрузочного """

from aiohttp import web

from demo import create_app


app = create_app()

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=8000)