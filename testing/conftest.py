import pytest


@pytest.fixture(scope="session")
def login():
    # setup 操作
    print("登录操作")
    # yield相当于 return操作
    yield ("jack", "123456")
    # teardown 操作
    print("登出操作")


@pytest.fixture(scope="session", autouse=True)
def conn_db():
    print("完成 数据库连接")
    yield "qqqq"
    print("关闭 数据连接")
