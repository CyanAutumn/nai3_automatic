import random
import time
from utils import flogger

log = flogger.Flogger().get_logger(__name__)


def random_sleep(min_sleep: int, max_sleep: int):
    sleep_time = (random.randint(min_sleep * 1000, max_sleep * 1000)) / 1000.0
    time.sleep(sleep_time)
    log.info(f"开始休眠{sleep_time}秒")
