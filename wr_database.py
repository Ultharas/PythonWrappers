from config import *
from sqlalchemy import create_engine, event
from sqlalchemy.sql import select, and_, or_, not_, text, update
from sqlalchemy import Table, MetaData, Column

# -- Ping DB / START -- #
from sqlalchemy.exc import DisconnectionError
def checkout_listener(dbapi_con, con_record, con_proxy):
    try:
        try:
            dbapi_con.ping(False)
        except TypeError:
            dbapi_con.ping()
    except dbapi_con.OperationalError as exc:
        if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
            raise DisconnectionError()
        else:
            raise
# -- Ping DB / END -- #


def get_one(table, where_dict):
    where_list = [table.name + '.' + key + ' = "' + value + '"' for key, value in where_dict.items()]
    where_string = ' AND '.join(where_list)
    # Print('where_string', where_string)

    result = e.execute(table.select().where(text(where_string))).first()
    if result:
        return result
    else:
        return False

def get_all(table, where_dict={}):

    if not where_dict:
        return e.execute(table.select()).fetchall()

    where_list = [table.name + '.' + key + ' = "' + value + '"' for key, value in where_dict.items()]
    where_string = ' AND '.join(where_list)
    # Print('where_string', where_string)

    result = e.execute(table.select().where(text(where_string))).fetchall()
    if result:
        return result
    else:
        return []

def db_connect(db_name, login='root', passw='', host='localhost'):
    e = create_engine('mysql://' + login + ':' + passw + '@' + host + '/' + db_name + '?charset=utf8', pool_recycle=1440)
    # e = create_engine('mysql://root:@localhost/dev1?charset=utf8', pool_recycle=1440)
    # e = create_engine('mysql://uzlime:vL9Vt63t@localhost/uzlime?charset=utf8', pool_recycle=1440)
    event.listen(e, 'checkout', checkout_listener)
    conn = e.connect()
    meta = MetaData()

    return e, meta, conn

def get_table(name):
    return Table(name, meta, autoload_with=e)

e, meta, conn = db_connect(config['db_name'], config['login'], config['passw'], config['host'])