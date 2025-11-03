from console_ui import ConsoleDbApp
from providers.raw_provider import RawSqlProvider
from providers.orm_provider import OrmProvider


def main():
    app = ConsoleDbApp(RawSqlProvider, OrmProvider)
    app.start_app()


if __name__ == '__main__':
    main()