import subprocess
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from accounts.mapping import Config, Account, Base
from tasks.task_queue import TaskQueue
from util import constants
from util.global_vars import GlobalAccessor
from workers.pool import Pool

Session = sessionmaker()


def load_config():
    constants.OMNISYNC_CFG_DIR.mkdir(exist_ok=True)
    session = GlobalAccessor.get_db_session()
    cfg_map = {item.name: item for item in session.query(Config)}
    # writing default config if current doesn't exist or is incosistent
    if cfg_map.get('down_limit') is None or cfg_map.get('up_limit') is None or cfg_map.get('max_conn') is None:
        down_limit_cfg = Config(name='down_limit', value=0)
        up_limit_cfg = Config(name='up_limit', value=0)
        max_conn_cfg = Config(name='max_conn', value=4)
        session.query(Config).delete()
        session.add_all([down_limit_cfg, up_limit_cfg, max_conn_cfg])
        session.commit()
    else:
        down_limit_cfg = cfg_map.get('down_limit')
        up_limit_cfg = cfg_map.get('up_limit')
        max_conn_cfg = cfg_map.get('max_conn')
    GlobalAccessor.set_max_conn(max_conn_cfg)
    GlobalAccessor.set_max_down(down_limit_cfg)
    GlobalAccessor.set_max_up(up_limit_cfg)


def load_database():
    db_path = constants.OMNISYNC_CFG_DIR / 'omnisync.db'
    if not db_path.is_file():
        subprocess.call(['sqlite3', str(db_path), '".databases"'])
    engine = create_engine('sqlite:///' + str(db_path), echo=True)
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)
    GlobalAccessor.set_db_session(Session())


def initialize():
    GlobalAccessor.set_task_queue(TaskQueue())
    GlobalAccessor.set_pool(Pool(GlobalAccessor.get_task_queue()))
    GlobalAccessor.get_pool().set_worker_num(GlobalAccessor.get_max_conn().value)


if __name__ == "__main__":
    load_database()
    load_config()
    initialize()

    session = accounts_table = GlobalAccessor.get_db_session()

    for account in session.query(Account):
        account.connect()

    session.commit()

    time.sleep(5)

    GlobalAccessor.get_pool().start()

    time.sleep(5)

    GlobalAccessor.get_task_queue().trigger()

    time.sleep(5)
