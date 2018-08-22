def factor_of(x):
    try:
        if (x.is_integer()):
            for factor in range(1, x+1):
                if(x % factor is 0):
                    print(factor)
    except TypeError:
        print("Not an integer value")



if __name__ == "__main__":
   factor_of(10.0)