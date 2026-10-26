student_data={
    "idk1":{"name":"sara","class":"v","subject_integration":"science,maths,english"},
    "idk2":{"name":"david","class":"v","subject_integration":"science,maths,english"},
    "idk3":{"name":"sara","class":"v","subject_integration":"science,maths,english"},
    "idk4":{"name":"surya","class":"v","subject_integration":"science,maths,english"}
}
result={}
seen_keys=[]
for studentid,details in student_data.items():
    unique_key=(details["name"],details["class"],details["subject_integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[studentid]=details
for k,v in result.items():
    print(k,":",v)