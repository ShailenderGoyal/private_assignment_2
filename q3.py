
mon_day = {
    "01": "31",  
    "02": "28",   
    "03": "31",  
    "04": "30",  
    "05": "31",  
    "06": "30",  
    "07": "31",  
    "08": "31",  
    "09": "30",  
    "10": "31",  
    "11": "30",  
    "12": "31"   
}
# TODO: 3 digit year support
def check_leap(year):
    year=int(year)
    if((year%100 !=0 and year%4==0) or (year %100 ==0 and year%400 == 0)):
        return True
    else:
        return False

def extract_dd(year):
    if(int(year)>999):
        date = year[-1:-3:-1]
    # elif (int(year)>99):

        # print(date)
        return date
    
def extract_mm(year):
    if(int(year)>999):
        date = year[-3::-1]
        # print(date)
        return date
    
palindrone=0
year=input("Enter Year:- ")
req_dd=extract_dd(year)
# print(req_dd)
req_mm=extract_mm(year)

if req_mm == "02":
    if check_leap(year):
        if int(req_dd) <= int("29"):
            palindrone=1
    else:
        if(int(req_dd) <= int(mon_day[req_mm])):
            palindrone==1
else:
    if(int(req_dd) <= int(mon_day[req_mm])):
        palindrone==1
print(palindrone)
