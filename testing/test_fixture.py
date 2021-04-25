# 开发人员： 曾祥茂
# 日期： 2021/03/31
import pytest


@pytest.fixture(autouse=True)
def login():
    # setup 操作
    print("登录操作")
    # yield相当于 return操作
    yield ("jack", "123456")
    # teardown 操作
    print("登出操作")


@pytest.fixture()
def conn_db():
    print("完成 数据库连接")


@pytest.mark.usefixtures("login")
def test_case1():
    print("用例1")

def test_case2():
    print("用例2")


def test_case3(conn_db):
    print(login)
    print("用例3")
