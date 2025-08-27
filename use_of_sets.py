#This program demonstrates the use of sets in Python. 
#It includes examples of creating sets, adding and removing elements, and performing set operations like union, intersection, and difference.
#Here are some exciting and real world applications of sets:


'''1. Removing duplicates from a list:'''
students = ['Alice', 'Bob', 'Alice', 'Eve', 'Bob']
unique_students = set(students)
print("Unique students are:", unique_students)



'''2. Checking Mutual friends on social media'''
dipan_friends = {'John', 'Ram', 'Sita', 'Bijaya'}
bijaya_friends = {'Ram', 'Trent', 'Peggy', 'Dipan'}
Trent_friends = {'Dipan', 'Sita', 'Bijaya', 'Karl'}
mutual_friends_1 = dipan_friends.intersection(bijaya_friends) #Mutual friends with Dipan and Bijaya
mutual_friends_2 = dipan_friends.intersection(Trent_friends) #Mutual friends with Dipan and Trent
mutual_friends_3 = bijaya_friends.intersection(Trent_friends) #Mutual friends with Bijaya and Trent
print("Mutual friends with Dipan and Bijaya are:", mutual_friends_1)
print("Mutual friends with Dipan and Trent are:", mutual_friends_2)
print("Mutual friends with Bijaya and Trent are:", mutual_friends_3)



'''Detect Missing Items'''
all_items_in_my_bag = {'Charger', 'Razor', 'Wallet', 'Keys', 'Passport', '$1000'} #Remember variables should not be too much long like these. So create short and sweet variables
what_I_Found_after_reaching = {'Wallet', 'Keys', 'Passport', '$1000'}
missing_items = all_items_in_my_bag.difference(what_I_Found_after_reaching)
print("Missing items are:", missing_items)



'''Recommendation System'''
dipan_watches = {'The Social Network', 'Inception', 'Interstellar', 'Sherlock Holmes', 'The Dark Knight', 'YJHD', 'Jab We Met'}
divya_watches = {'Saiyaara','Zindagi Na Milegi Dobara', 'YJHD', 'Jab We Met', 'Titanic'}
nobita_watches = {'Saiyaara', 'The Dark Knight', 'Jab We Met', 'Titanic'}
doraemon_watches = {'The Social Network', 'Inception', 'Interstellar', 'Sherlock Holmes'}
recommend_when_divya_dipan_together = dipan_watches.difference(divya_watches)
#OR
recommend_when_divya_dipan_together = divya_watches.difference(dipan_watches)
recommend_when_divya_nobita_together = divya_watches.difference(nobita_watches)
#OR
recommend_when_nobita_divya_together = nobita_watches.difference(divya_watches)
recommend_when_dipan_doraemon_together = dipan_watches.difference(doraemon_watches)
#OR
recommend_when_dipan_doraemon_together = doraemon_watches.difference(dipan_watches)
recommend_when_nobita_doraemon_together = nobita_watches.difference(doraemon_watches)
#OR
recommend_when_doraemon_nobita_together = doraemon_watches.difference(nobita_watches)
print("When Divya and Dipan are together, they can watch:", recommend_when_divya_dipan_together)
print("When Divya and Nobita are together, they can watch:", recommend_when_divya_nobita_together)
print("When Dipan and Doraemon are together, they can watch:", recommend_when_dipan_doraemon_together)
print("When Nobita and Doraemon are together, they can watch:", recommend_when_nobita_doraemon_together)
print("When Divya, Dipan and Nobita are together, they can watch:", dipan_watches.intersection(divya_watches).intersection(nobita_watches))
print("When Divya, Dipan and Doraemon are together, they can watch:", dipan_watches.intersection(divya_watches).intersection(doraemon_watches))



'''Spelling Checker'''
dictionary = {'C++', 'JavaScript', 'Ruby on Rails', 'PHP', 'Angular', 'Laravel', 'Python'}
spelled_by_student = {'C++', 'JavaScirpt', 'Pithon', 'Ruby on Ralis', 'Laravel', 'PHP' ,'Angilar'}
# - is also same as difference() method in set. By the way, - is symbolic representation of difference().
misspelled_words = spelled_by_student - dictionary
print("Misspelled words are:", misspelled_words)


'''Unique visitors on website'''
visitors = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]
unique_visitors = set(visitors)
print(len(unique_visitors))  # 3



'''Skills matching with job'''
job_skills = {"Data Manipulation", "AI/ML", "Reinforcement Learning", "Digital Device Networking"}
candidate = {"Data Manipulation", "c++", "ml"}
missing_skills = job_skills - candidate
print(missing_skills)  # {'AI/ML', 'Reinforcement Learning', 'Digital Device Networking'}



'''Essay Similarity'''
statement_1 = set("Python is a great programming language".split())
statement_2 = set("Python is a powerful programming language".split())
similarity = statement_1 & statement_2
print(similarity)

#This much for sets
#Bye Bye dear programmers.