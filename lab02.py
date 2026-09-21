# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds)->str:
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    hours:int=int(total_seconds/3600)
    minutes:int=int((total_seconds%3600)/60)
    seconds:int=int((total_seconds%3600)%60)
    answer:str=f'{hours}:{minutes:02d}:{seconds:02d}'
    return answer


def admission_price(age)->float:
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    if age>=65:
        price:float=10
    elif age>=13:
        price:float=15
    elif age>=5:
        price:float=8
    else :
        price:float=0
    
    return price



def sum_multiples(limit)->int:
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    sum:int=0
    round:int=0
  
    while round<limit:
        if round%3==0:
             sum+=round
             round+=1
        elif round%5==0:
             sum+=round
             round+=1
       
        else:
            round+=1
    return sum


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    pass


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(3661))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
   


if __name__ == "__main__":
    main()
