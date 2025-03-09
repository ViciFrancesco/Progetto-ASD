from performance_test import LCSTester

def main():
    sizes =[]
    for i in range(501):
        sizes.append(i)

    tester = LCSTester(sizes)
    tester.run_test()
    tester.plot_results()

if __name__ == "__main__":
    main()