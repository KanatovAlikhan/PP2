def solve(numheads, numlegs):
    print("The Chickens= ", numheads-(numlegs-numheads*2)//2,'\n' , "The Rabbits= ", (numlegs-numheads*2)//2)
if __name__ == "__main__": #i used to import this file for ex14
    solve(int(input("Write heads ")) , int(input("Write legs ")))
