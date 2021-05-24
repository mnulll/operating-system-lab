def file_location(name, strt, size):

    if strt >= 0 and strt < 50 and strt+size < 51:
        if arr[strt] == 0 and arr[strt+size-1] == 0:
            for i in range(strt, (strt+size), 1):
                arr[i] = name
            print(arr, "\n")
        else:
            print(
                "\nFile is not allocated because there is another file on the particular storage\n")
    else:
        print("\nFile is not allocated because exceeded the storage limit\n")


arr = [0]*50

file_location("OS1", 3, 5)
file_location("OS2", 3, 4)
file_location("OS3", -1, 4)
file_location("OS4", 10, 40)
file_location("OS5", 0, 2)
