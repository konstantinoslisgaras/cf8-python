from collections import Counter

def count_with_dict_compr(my_list):
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print("Dictionary comprehension:", frequency_dict)

def count_with_manual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    print("Manual loop:", frequency_dict)

def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    print("Get method:", frequency_dict)

def count_with_count(my_list):
    frequency_dict = Counter(my_list)
    print("Using counter:", frequency_dict)
    sorted_by_frequency = frequency_dict.most_common()[:2]
    print(sorted_by_frequency)

def main():
    my_list = ["Mango", "Kiwi", "Peach", "Melon", "Watermelon", "Apricot", "Mango", "Cherries", "Peach"]
    count_with_dict_compr(my_list)
    count_with_manual_loop(my_list)
    count_with_get_method(my_list)
    count_with_count(my_list)

if __name__ == "__main__":
    main()