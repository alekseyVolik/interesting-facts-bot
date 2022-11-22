from os import path


base_dir = path.abspath(path.dirname(__file__))


class AppConfig:
    SQL_ALCHEMY_DB_URL = f"sqlite:///{path.join(path.join(base_dir, 'app.db'))}"
