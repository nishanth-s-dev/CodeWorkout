def print_name_n_time(name, n):
    if n == 0:
        return
    print(name)
    print_name_n_time(name, n - 1)

def main():
    print_name_n_time('Nishanth S', 10)

if __name__ == '__main__':
    main()