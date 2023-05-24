from statistics import mean, stdev
import matplotlib.pyplot as plt


def prime_list(limit):
    if limit < 2:
        return []
    else:
        primes = [2]
        for test_number in range(3, limit + 1, 2):
            is_prime = True
            for prime in primes:
                if test_number % prime == 0:
                    is_prime = False
                    break
                if prime * prime > test_number:
                    break
            if is_prime:
                primes.append(test_number)
    return primes


def diff_list(numbers):
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]


if __name__ == "__main__":
    diff_lists = [prime_list(5000)]
    for index in range(len(diff_lists[0])):
        diff_lists.append(diff_list(diff_lists[index]))
    mean_list = []
    stdev_list = []
    first_list = []
    for dl in diff_lists:
        print(dl)
        if len(dl) > 0:
            first_list.append(dl[0])
            mean_list.append(mean(dl))
            print(f'Mean: {mean_list[-1]}')
        if len(dl) > 1:
            stdev_list.append(stdev(dl))
            print(f'Standard Deviation: {stdev_list[-1]}')
        print()
    print(f'First List:')
    print(first_list)
    print(mean(first_list))
    print(stdev(first_list))
    print()
    print(f'Mean List:')
    print(mean_list)
    print(mean(mean_list))
    print(stdev(mean_list))
    print()
    print(f'Standard Deviation List:')
    print(stdev_list)
    print(mean(stdev_list))
    print(stdev(stdev_list))
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.title(f'First')
    plt.plot(first_list)
    plt.subplot(3, 1, 2)
    plt.title(f'Mean')
    plt.plot(mean_list)
    plt.subplot(3, 1, 3)
    plt.title(f'Standard Deviation')
    plt.plot(stdev_list)
    plt.show()
