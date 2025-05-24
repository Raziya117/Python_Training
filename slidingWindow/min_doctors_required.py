#print the maximum number of doctors to check all patients,patient arrival and end timings is given
a=[900,945,1110,1230,1235,1245,1340,1700]
e=[930,1130,1120,1250,1250,1415,1400,1730]
i,j=0,0
d=1
while i<len(a) and j<len(e):
    if a[i]<=e[j]:
        d+=1
        i+=1
    else:
        d-=1
        j+=1
print(d)

#PRINT the number of patients a doctor can attend
a = [900, 945, 1110, 1230, 1235, 1245, 1340, 1700]
e = [930, 1130, 1120, 1250, 1250, 1415, 1400, 1730]
appointments = list(zip(a, e))
appointments.sort(key=lambda x: x[1])
count = 0
last_end = 0
for start, end in appointments:
    if start >= last_end:
        count += 1
        last_end = end
print(count)
       
        
    
