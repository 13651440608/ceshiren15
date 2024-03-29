# 开发人员： 曾祥茂
# 日期： 2021/03/31
import pytest
import yaml
from Tools.demo.sortvisu import steps

from pythoncode.calculator import Calculator


# 解析测试数据文件
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    print(add_ids)
    return [add_datas, add_ids]


# 解析测试步骤文件
def setup(addsetupfile, calc, a, b, expect):
    with open(addsetupfile) as f:
        setup = yaml.safe_load(f)

    for step in setup:
        if 'add' == step:
            print("step: add")
            result = calc.add(a, b)
        elif 'add1' == step:
            print("step: add1")
            result = calc.add1(a, b)

        assert expect == result


# def test_a():
#     print("test case a")


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # def setup(self):
    #     self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # def test_add1(self):
    #   #  calc = Calculator()
    #     result = self.calc.add (100,100)
    #     assert result == 200
    #
    # def test_add2(self):
    #   #  calc = Calculator()
    #     result = self.calc.add (0.1,0.1)
    #     assert result == 0.2


class TestCalc1:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [0, 1, 0], [10, 1, 10], [-10, 1, -10], [10, -1, -10],
        [-10, -1, 10], [1, 2, 0.5], [1, 3, 0.3333333333333333], [1, 100, 0.01], [0.1, 0.1, 1],
        [0.1, 1, 0.1], [0.1, 0.001, 100]
    ], ids=['float1_case', 'float2_case', 'float3_case', 'float4_case',
            'float5_case', 'float6_case', 'float7_case'])
    def test_div(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b', [
        [0.1, 0], [10, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):  # 补货异常场景
            self.calc.div(a, b)

    # def test_div(self):
    #     with pytest.raises(ZeroDivisionError) :   #补货异常场景
    #         result = self.calc.div(1,0)

    # try:
    #     result = self.calc.div(1,0)
    # except ZeroDivisionError :
    #     print("错误")

    def test_add_setup(self):
        a = 1
        b = 1
        expect = 2
        setup("./setup/add_setup.yml", self.calc, a, b, expect)
        # assert 2 ==self.calc.add(1,1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)
