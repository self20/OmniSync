import subprocess
import time

from tasks.task_queue import TaskQueue
from util import constants
from util.global_vars import GlobalAccessor
from workers.pool import Pool


def load_config():
    constants.OMNISYNC_DIR.mkdir(exist_ok=True)
    cfg_table = GlobalAccessor.get_db().get_table('config', primary_type='String')
    down_limit_cfg = cfg_table.find_one(id='down_limit_cfg').get('value')
    up_limit_cfg = cfg_table.find_one(id='up_limit_cfg').get('value')
    max_conn_cfg = cfg_table.find_one(id='max_conn_cfg').get('value')
    # writing default config if current doesn't exist or is incosistent
    if down_limit_cfg is None or up_limit_cfg is None or max_conn_cfg is None:
        down_limit_cfg = 0
        up_limit_cfg = 0
        max_conn_cfg = 4
        cfg_table.upsert(dict(id='down_limit_cfg', value=down_limit_cfg), ['id'])
        cfg_table.upsert(dict(id='up_limit_cfg', value=up_limit_cfg), ['id'])
        cfg_table.upsert(dict(id='max_conn_cfg', value=max_conn_cfg), ['id'])
    GlobalAccessor.set_max_conn(max_conn_cfg)
    GlobalAccessor.set_max_down(down_limit_cfg)
    GlobalAccessor.set_max_up(up_limit_cfg)


def load_database():
    db_path = constants.OMNISYNC_DIR / 'omnisync.db'
    if not db_path.is_file():
        subprocess.call(['sqlite3', str(db_path), '".databases"'])
    GlobalAccessor.set_db(dataset.connect('sqlite:///' + str(db_path)))


def initialize():
    GlobalAccessor.set_task_queue(TaskQueue())
    GlobalAccessor.set_pool(Pool(GlobalAccessor.get_task_queue()))
    GlobalAccessor.get_pool().set_worker_num(GlobalAccessor.get_max_conn())


if __name__ == "__main__":
    load_database()
    load_config()
    initialize()

    accounts_table = GlobalAccessor.get_db().get_table('accounts', primary_type='String', primary_id='ident')
    for account in accounts_table:
        account.connect()
        accounts_table.update(account, ['ident'])

    time.sleep(5)

    GlobalAccessor.get_pool().start()

    time.sleep(5)

    GlobalAccessor.get_task_queue().trigger()

    time.sleep(5)
