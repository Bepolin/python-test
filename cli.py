import datetime
import sys


def date_type(date_str):
    # str -> date 型変換関数
    return datetime.date.fromisoformat(date_str)


if __name__ == '__main__':
    args = sys.argv

    