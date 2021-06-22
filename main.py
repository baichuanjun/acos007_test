import config.null as null
import test_api.test_all_method as test_all_method
from logger import Log


def main():
    all_test = []
    all_test += dir(test_all_method)
    all_test_func_name = set(all_test) - set(dir(null))
    for i in all_test_func_name:
        try:
            getattr(test_all_method, i)()
        except Exception as e:
            print(f"\033[1;33m error:详情见test日志 error_url_suffix--->{i}\033[0m")
            Log.test_error(str(e))


if __name__ == '__main__':
    main()

# TODO 注：1.如果本测试脚本出现错误会记录到xxxx_xx_xx_test.log
# TODO    2.如果是Acos007业务上面的错误则会记录到xxxx_xx_xx_business.log
# TODO    3.其他错误则会记录到xxxx_xx_xx_other.log
