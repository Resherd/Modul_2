from colorama import init, Fore, Style

init(autoreset=True)

array = [5, 3, -6, -8, 5, 0, 3, 1, -4, 1, 3, -7, 9, 0, 6, 1, 8, 4, 4, -1, 1, 12, 10, 16, 9, 1, 8, 9, 5, -5]

p = 20  
print(f"Ви ввели число {Fore.BLACK}p{Style.RESET_ALL}: {Fore.BLUE}{p}{Style.RESET_ALL}\n")

p = min(p, 30)

print(f"\nМасив {Fore.BLUE}{p}{Style.RESET_ALL} елементів:")
min_value = min(array[:p])
second_min_value = sorted(set(array[:p]))[1]

for i in range(p):
    if array[i] == min_value or array[i] == second_min_value:
        print(f"{Fore.BLACK}{array[i]}*{Style.RESET_ALL}", end=" ")
    else:
        print(f"{Fore.RED}{array[i]}{Style.RESET_ALL}", end=" ")
print()

min_index_1 = array.index(min_value)
min_index_2 = array.index(second_min_value)

start_index = min(min_index_1, min_index_2) + 1
end_index = max(min_index_1, min_index_2)
elements_between = array[start_index:end_index]


print(f"\n{Fore.BLUE}{len(elements_between)}{Style.RESET_ALL} елементів між мінімальними")
print(f"{Fore.RED}{' '.join(map(str, elements_between))}{Style.RESET_ALL}")
