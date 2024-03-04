def asc_desc(n_str):
    list = [int(x) for x in n_str]

    if(len(list)==3):
        list.append(0)

    elif(len(list)==2):
        list.append(0)
        list.append(0)
    
    elif(len(list)==1):
        list.append(0)
        list.append(0)
        list.append(0)
    
    # print(list)
    asc_list = sorted(list)
    dsc_list = sorted(list,reverse=True)
    # print(asc_list)
    # print(dsc_list)
    return asc_list,dsc_list


def num_list(list):
    num = list[0]*1000 + list[1]* 100 + list[2] * 10 + list[3]
    # print(num)
    return num

def main():
    n_str= input("Enter the number:- ")

    if(len(n_str)>4):
        print("Enter a smaller number")
        exit


    while(1):
        print(n_str)
        asc,desc=asc_desc(n_str)
        asc=num_list(asc)
        desc = num_list(desc)

        subtracted=desc-asc
        store_last=subtracted
        subtracted=str(subtracted)
        if(n_str==subtracted):
            break
        n_str=subtracted
if __name__ == "__main__":
    main()