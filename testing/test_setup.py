# 开发人员： 曾祥茂
# 日期： 2021/03/31
# 模块级别
def setup_mdule():
    print("资源准备： setup mdule")


def tearsdown_mdule():
    print("资源销毁： tesrdown mdule")


def test_case1():
    print("case1")


def setup_function():
    print("资源准备： setup function")


def teardown_function():
    print("资源销毁： teardown function")


class TestDemo:
    # 执行类 前后分别执行setup_class teardowan_calss
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")


class TestDemo1:
    # 执行类 前后分别执行setup_class teardowan_calss
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
