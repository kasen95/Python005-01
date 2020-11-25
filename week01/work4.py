import logging

import os.path
import time


def test():
    # log_path = os.path.join('/Users/shaojiacheng/python-' + time.strftime('%Y-%m-%d', time.localtime(time.time())),'test.log')
    log_path = os.path.join('/var/log/python-' + time.strftime('%Y-%m-%d', time.localtime(time.time())), 'test.log')
    parent_path = os.path.abspath(os.path.join(log_path, '..')) + '/'
    # 需先获取该目录下写入权限，这种方式还是获取不了。使用注释的目录正常
    if not os.access('/var/log/', os.W_OK):
        os.chmod('/var/log/', 0o755)
    if not os.path.isdir(parent_path):
        os.makedirs(parent_path)
    if not os.path.exists(log_path):
        f = open(file=log_path, mode='w+', encoding='utf-8')
        f.close()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename=log_path)
    logger = logging.getLogger("work4")
    logger.info('方法被调用')


if __name__ == "__main__":
    while True:
        time.sleep(2)
        test()
