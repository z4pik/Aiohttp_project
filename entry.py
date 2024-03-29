""" Здесь создаётся объект application. Данный файл используется в качестве загрузочного """
import argparse

import aiohttp.web_app
from aiohttp import web

from demo import create_app
from demo.settings import load_config


# Определяем и конфигурируем аргументы командной строки
parser = argparse.ArgumentParser(description="Demo Project")
parser.add_argument('--host', help="Host to listen", default="127.0.0.1")
parser.add_argument('--port', help="Port to accept connections", default="8000")
parser.add_argument('--reload', action="store_true", help="Autoreload code on change")

parser.add_argument("-c", "--config", type=argparse.FileType('r'),
                    help="Path to configuration file"
                    )

# Передаём аргументы для командной строки
args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print("Start with code reload")
    import aioreloader
    aioreloader.start()

if __name__ == '__main__':
    web.run_app(app, host=args.host, port=args.port)
