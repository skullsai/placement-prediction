def removeWeirdChars(events):
    weirdchars='<>'
    for event in events:
        for char in weirdchars:
            if char in event:
                event=event.replace(char,"")
    return events


def csvToFormat(work_df):
    
    for i in range(len(work_df)):
        if (i%1000==0):
            print(i)
        work_df['companies'][i]=removeWeirdChars(work_df['companies'][i])
        work_df.skills[i]=work_df.skills[i].lstrip('[').rstrip(']').replace("'","").split(',')
        work_df.schools[i]=work_df.schools[i].lstrip('[').rstrip(']').replace("'","").split(',')  
        work_df.interests[i]=work_df.interests[i].lstrip('[').rstrip(']').replace("'","").split(',')   
        work_df.majors[i]=work_df.majors[i].lstrip('[').rstrip(']').replace("'","").split(',') 
    return work_df
