# This function performs the sift-down operation to maintain the heap property.
# It takes an array, an index 'i' of the node to be sifted down, and a list of swaps 'swaps'.
# It recursively swaps the node with its smallest child if necessary, and updates the swaps list.
def sift_down(arr, i, swaps):
    n = len(arr) # length of array
    min_index = i # initialize min_index to i
    left_child = 2*i + 1 # index of the left child
    right_child = 2*i + 2 # index of the right child

    # Check if the left child is smaller than the current node
    # and update min_index if necessary.
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child

    # Check if the right child is smaller than the current node
    # and update min_index if necessary.
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child

    # If the min_index has changed, swap the nodes, append the swap to swaps list,
    # and call sift_down on the new min_index.
    if i != min_index:
        swaps.append((i, min_index)) # append the swap to swaps list
        arr[i], arr[min_index] = arr[min_index], arr[i] # swap the nodes
        sift_down(arr, min_index, swaps) # recursively call sift_down on the new min_index

# This function builds a heap from an array by calling sift_down on each non-leaf node in reverse order.
# It returns the swaps made to build the heap.
def build_heap(arr):
    swaps = [] # initialize the swaps list
    n = len(arr) # length of array

    # Call sift_down on each non-leaf node in reverse order.
    for i in range(n//2, -1, -1):
        sift_down(arr, i, swaps)

    return swaps # return the swaps made to build the heap

# This is the main function that prompts the user for input and calls the build_heap function.
def main():

    input1 = input("Input I or F: ") # prompt the user for the input type
    if (input1 == "F"): # if input type is file
        inputF = "./tests/"+input("File name: ") 
        inputFile = open(inputF, "r") # open the file for reading
        lines = inputFile.readlines() # read the lines of the file

        n = int(lines[0]) # read the first line as the number of elements
        arr = list(map(int, lines[1].split())) # read the second line as the array

        swaps = build_heap(arr) # build the heap and get the swaps made

        print(len(swaps)) # print the number of swaps
        for swap in swaps:
            print(swap[0], swap[1]) # print each swap made

    elif (input1 == "I"): # if input type is interactive
        print("Input:")

        n = int(input()) # read the first line as the number of elements
        arr = list(map(int, input().split())) # read the second line as the array

        swaps = build_heap(arr) # build the heap and get the swaps made

        print(len(swaps)) # print the number of swaps
        for swap in swaps:
            print(swap[0], swap[1]) # print each swap made
    else:
        print("Incorrect input (must be I or F)") # if invalid
        return

##n = int(input()) ##Ievadīt par 'cik'?
##arr = list(map(int, input().split())) ##Ievadīt skaitļus, pēc 'cik'?

if __name__ == "__main__":
    main()
