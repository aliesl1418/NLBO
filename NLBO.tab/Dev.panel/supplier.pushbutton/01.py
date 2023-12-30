import multiprocessing

def test1():
    for i in range(100000):
        print("III")


def test2():
    for i in range(100000):
        print("---")


thrad1 = multiprocessing.Process(target = test1)
thrad2 = multiprocessing.Process(target = test2)


if __name__ == "__main__":
    thrad1.start()
    thrad2.start()