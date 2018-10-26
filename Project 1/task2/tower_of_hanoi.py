import time

def main():
    size = int(input("Enter the height for tower of hanoi: "))
    start_time = time.clock()
    tower_of_hanoi(size, "First Pole", "Third Pole", "Second Pole")
    end_time = time.clock()
    print("Tower of Hanoi with height = {} took {} seconds".format(size, end_time - start_time))

def tower_of_hanoi(height, from_rod, to_rod, aux_rod):
    # If the height of the tower is 1, do nothing
    if height == 1:
        #print("Move disk 1 from {} to {}".format(from_rod, to_rod))
        return
    # Start the recurrence relation of the tower by moving the disk from the origin to the target rod
    tower_of_hanoi(height - 1, from_rod, aux_rod, to_rod)
    #print("Move disk {} from {} to {}".format(height, from_rod, to_rod))
    tower_of_hanoi(height - 1, aux_rod, to_rod, from_rod)

if __name__ == '__main__':
    main()
