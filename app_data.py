from enum import Enum
import DB_App


class DBType(Enum):
    SQLite = "SQLite"
    MySQL = "MySQL"

class AppData:
    app_name = ""
    app_version = ""
    app_build_version = ""
    db_type = DBType.SQLite

    @staticmethod
    def get_app_version():
        return f"v{AppData.app_version} Build({AppData.app_build_version})"

    @staticmethod
    def set_db_type(db_type: DBType):
        AppData.db_type = db_type

    @staticmethod
    def get_db_type():
        AppData.db_type = DB_App.ParamData.get(DB_App.ParamData.param_name == "DBType.SQLite")
