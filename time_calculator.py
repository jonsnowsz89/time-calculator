def add_time(starting_time , ending_time, starting_day =False):
    import re
    result = 'No result, semthing goes wrong ... !'
    
    
    t24f= time24f(starting_time)
    days = 0
    h = t24f[0]
    m = t24f[1]
    
    endtime_arr =strtime2arr(ending_time)
    h1=endtime_arr[0]
    m1=endtime_arr[1]
    
    resultM=(m+m1)%60
    resultH= h+h1 +(m+m1)//60
    days = resultH // 24
    resultH = resultH%24
    
    if days == 0:
        days_message =''
    elif days == 1:
        days_message ='(next day).'
    elif days > 1:
        days_message ='('+str(days)+' days latter).'
    
    if starting_day:
        starting_day = starting_day.title()
        day_name=get_day_name(starting_day, days)
    else:
        day_name=''
    
    if resultM <10 : 
        resultM = '0'+str(resultM)
    else: 
        resultM = str(resultM)
    
    if resultH >= 13 :
        resultH   = str(resultH-12) 
        resultM += ' PM'
    elif resultH == 12 :
        resultH =str(resultH) + ' PM'
    else :
        resultH = str(resultH) 
        resultM += ' AM'
    result = resultH+':'+resultM +' '+day_name + ' '+days_message
    
    print(result) 
    return result
    
    
    
def time24f(time) :
    import re

    hm= strtime2arr(time)
    h= hm[0]
    m= hm[1]
    day_time =re.findall('[a-z,A-Z]+',time)[0]
    if day_time=='PM':
        h = h + 12
    result=[h,m]
    return result
    
    
    
def strtime2arr(time):
    import re

    time_split = time.split(':')
    h=int(time_split[0])
    m = int(re.findall('[0-9]+',time_split[1])[0])
    time_arr = [h,m]
    return time_arr

def get_day_name(name, days):
    week_days={1:'Monday', 2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    
    key_list =  list(week_days.keys())
    val_list = list(week_days.values()) 

    position = val_list.index(name) 
    daynum = key_list[position]
    position = (days%7)+daynum
    if position >7:
        position = (position - 7)
    
    
    day_name = week_days[position]
    
    
    return day_name

#------------------------
