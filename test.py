import pysnooper


@pysnooper.snoop()
def demo_func():
    profile = {"name": "写代码的明哥", "age": 27, "gender": "male"}

    return profile


def main():
    profile = demo_func()


main()
