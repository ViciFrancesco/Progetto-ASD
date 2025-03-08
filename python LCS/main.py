from performance_test import LCSTester

def main():
    tester = LCSTester(sizes=[5, 10, 15, 20, 25, 30, 40, 50])
    tester.run_test()
    tester.plot_results()

if __name__ == "__main__":
    main()