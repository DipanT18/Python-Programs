dinner_list=['Arbin', 'Dipan', 'Dristi','Manjil', 'Wagle', 'Sita', 'Ravi']
print("Dinner is served for: ", dinner_list)
message=f"The first person coming for the dinner is {dinner_list[0]}."
print(message)
dinner_list[0]='Sachin'
message=f"Arbin has to catch flight. So, the person coming for the dinner is {dinner_list[0]}."
print(message)
dinner_list.insert(1, 'Rahul')
print("Dinner is served for : ", dinner_list, "(Updated)")