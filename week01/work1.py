import logging
import subprocess


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("cmd")

def get_cmd_result(cmd_string):
    """
    subprocess.Popen:subprocess模块下的Popen方法，实现：
    在执行该程序的服务器上实现shell命令的执行；
    > subprocess.PIPE--->管道机制：一个程序与另一个程序实现通信，例如：cmd命令提示符与屏幕显示，又如：subprocess 与屏幕显示
    > subprocess.POPE,有stdout:标准输出内容扔到管道；
    > stdin：标准输入内容扔到管道；
    > stderr：标准错误输出内容扔到管道；
    通过read将管道里面的内容一部分一部分的获取读出；管道里面的内容，只可读一次，即：丢进管道的内容读一部分少一部分，直到读完；
    stdout, stdin, stderr 的内容扔进不同管道，read不冲突；
    例如：如果一个命令执行出错，那么，stderr扔进管道就有内容，stdout就read空；
    所以，这个就可以判断一个命令是否执行有错；

    Args:
        cmd_string: 执行的命令，例如：adb shell dumpsys meminfo com.midea.ai.appliances

    Returns: stdout, stderr;执行后的标准输出和标准错误
    """
    stdout = None
    stderr = None
    try:
        # 执行命令，得到命令结果cmd_res
        res = subprocess.Popen(cmd_string, shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        # res是一个对象，需要读取res对象的stderr\strout\stdin的属性，才可获取值
        # 或者用下面这个命令获取结果，(stdout, stderr) = res.communicate()
        stdout, stderr = res.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
    except Exception as e:
        print(e)

    return stdout, stderr



def log_cmd_result(cmd_string):
    """
    双通道输出，对于执行错误情况，约定为打印异常日志，并抛出异常中断任务
    :param cmd_string:cmd命令
    """
    logger.info("执行以下内容：" + cmd_string)
    stdout, stderr = get_cmd_result(cmd_string)
    if stdout:
        logger.info(stdout)
    if stderr:
        logger.error(stderr)


if __name__=="__main__":
    log_cmd_result('python3.7 -version')
    log_cmd_result('pip3.7 -V')