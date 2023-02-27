

def main():
    file = open("C:/Users/azn_g/Desktop/Advent of Code 2022/Day 1/input.txt")

    filelines = file.read().splitlines()
    master_list = []
    small_list = []
    counter = 0
    test_a = ['1', '2', '3']
    test_b = [['1'], ['1', '2'], ['1', '2', '3']]
    a = []



    for i in filelines:
        # Start grouping the lines together (seperated by an empty space).
        # Do this by either creating small lists, and appending them to master_list
        # or

        if (i != ''):
            small_list.append(int(i))
        
        # Make sure not to remove the reference to small_list (reference in master_list will
        # go back to small_list)
        else:
            master_list.append(small_list)
            small_list = []
        
        filelines = file.read().splitlines()
    
    # If the input ends on a non-newline character, there will be an existing
    # list in small_list that has not been inserted into master, check for it
    # by checking the last item in master_list (this is based off the assumption
    # that all lists will be unique and there are no copies, otherwise
    # use a dictionary/array for immutability and key/value indices)
    a = master_list[len(master_list)-1]
    if a != small_list:
        master_list.append(small_list)
    
    # Done with file, can close it
    file.close()

    # Iterate through the master_list. Keep track of who has the most
    # calories and keep track of its position in the list

    sorted_list = []
    max_calories = 0
    position = 0

    for i in range (0, len(master_list)):
        if (sum(master_list[i]) > max_calories):
            position = i
            max_calories = sum(master_list[i])
        sorted_list.append(sum(master_list[i]))
    
    sorted_list.sort(reverse=True)


    elf_sum = sum(sorted_list[:3:])
    

    print("The elf with the most calories occurs at position", str(position), "with a calorie count of",
    max_calories)
    print("The three top elves carried a net total of", elf_sum, "calories.")
main()