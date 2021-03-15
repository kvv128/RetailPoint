from peewee import *
import app_data

db = SqliteDatabase('app.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = AutoField(verbose_name="id")
    user_login = CharField(verbose_name="Логин")
    user_psswd = CharField(verbose_name="Пароль")
    user_name = CharField(verbose_name="ФИО")
    id_user_post = IntegerField(verbose_name="Должность")

    class Meta:
        table_name = 'user'


class Post(BaseModel):
    post_id = AutoField(verbose_name="id")
    post_name = CharField(verbose_name="Должность")

    class Meta:
        table_name = 'post'


class ParamData(BaseModel):
    param_id = AutoField(verbose_name="id")
    param_name = CharField(unique=True, verbose_name="Параметр")
    param_value = CharField(verbose_name="Значение")

    class Meta:
        table_name = "param_data"


def reset_app_db():
    db.drop_tables([User, Post, ParamData])
    db.create_tables([User, Post, ParamData])


def reset_to_default_param():
    query = ParamData.delete().execute()
    query = ParamData.create(param_name="app_name", param_value=app_data.AppData.app_name)
    query = ParamData.create(param_name="app_version", param_value=app_data.AppData.app_version)
    query = ParamData.create(param_name="db_type", param_value=app_data.DBType.SQLite)

def save_start_param():
    query = ParamData.update(param_value=app_data.AppData.app_version).where(ParamData.param_name == "app_version")
    query.execute()

# def check_sqlite_structure():
#     cursor = db.cursor()
#     # all_db_classes = {ParamData.Meta.table_name: ParamData, "user": User, "post": Post}
#     all_db_classes = [ParamData, User, Post]
#
#     all_classes_field = {}
#     for cur_class in all_db_classes:
#         # Получаем список полей класса
#         class_attributs = []
#         for attribute in cur_class.__dict__.keys():
#             if not attribute.startswith("_") and attribute != "DoesNotExist":
#                 print(attribute)
#                 class_attributs.append(attribute)
#         all_classes_field[cur_class] = class_attributs
#
#     # получаем список таблиц
#     cursor.execute("SELECT name FROM sqlite_master;")
#     table_list = cursor.fetchall()
#
#     # сравниваем количество таблиц
#     print(f"таблиц в бд: {len(table_list) - 1}")
#     print(f"таблиц в app: {len(all_db_classes)}")
#     if (len(table_list) - 1) != len(all_db_classes):
#         print("В БД не совпадает кол-во таблиц ")
#         return
#
#     # Проверяем поля
#     for curr_table in table_list:
#         print(f"Table - {curr_table[0]}")
#         # получаем список полей
#         cursor.execute(f'PRAGMA table_info(user);')
#         db_table_fields = cursor.fetchall()
#
#         # Проверяем совпадение по кол-ву полей
#         print(f"{len(db_table_fields)}:{len(all_classes_field.get(curr_table))}")
#         if len(db_table_fields) != len(all_classes_field.get(curr_table)):
#             print(f"В таблице {curr_table} не совпадает кол-во полей")
#             return
#
#         for curr_table in db_table_fields:
#             print(f"\t{curr_table[1]}")

    # список атрибутов класса БД
    # print(f"\n{User.__dict__.keys()}")
    #
    # for attribute in User.__dict__.keys():
    #     if not attribute.startswith("_") and attribute != "DoesNotExist":
    #         print(attribute)


# -----------------------------------------------------------------
def check_db_file():

        # Проверяем наличие файла app.db для SQLite
        if app_data.AppData.db_type == app_data.DBType.SQLite:
            import os
            if os.path.isfile("app.db"):
                return
        # create database
            try:
                db.create_tables([User, Post, ParamData])
                reset_to_default_param()
            except Exception as e:
                print(e)


# check_sqlite_structure()

# def test_def():
#     MA = Post.alias()
#     query = (User.select(User.user_name, User.id_user_post, MA.post_name)
#              .join(MA, JOIN.LEFT_OUTER, on=(User.id_user_post == MA.post_id)))
#     print("print data...\n", query)
#     for row in query:
#         print(row.user_fio, row.id_user_post, row.post.post_name)
