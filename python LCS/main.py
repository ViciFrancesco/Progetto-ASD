from performance_test import LCSTester
import time

nr = 1400 + 1

def main():
    sizes =[]
    for i in range(nr):
        sizes.append(i)

    tester = LCSTester(sizes)
    tester.run_test()
    tester.plot_results()



if __name__ == "__main__":
    main()