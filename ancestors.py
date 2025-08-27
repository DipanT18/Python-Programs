#This is a program which uses recursion in python.
#Recursion is a process in which a function calls itself directly or indirectly.
family = {
    "Dipan Timalsina":['Madhav Timalsina','Tara Timalsina'],
    "Madhav Timalsina":['Netra Prasad Timalsina', 'Harimai Timalsina'],
    "Netra Prasad Timalsina":['Prem Narayan Timalsina', 'Sita Timalsina'],
    "Tara Timalsina":['Narayan Prasad Acharya', 'Durga Acharya'],
    "Harimai Timalsina":['Jhamka Sapkota', 'Devi Sapkota'],
    "Prem Narayan Timalsina":['David Timalsina', 'Sweety Timalsina'],
    "Sita Timalsina":['Rocky Ghimire', 'Reema Ghimire'],
    "Narayan Prasad Acharya":['Shankar Acharya', 'Turkey Acharya'],
    "Durga Acharya":['Nirmal Humagain', 'Balkumari Humagain'],

}
def show_ancestors(person, level=0):
    if person not in family:
        return
    for ancestor in family[person]:
        print("  " * level + ancestor)
        show_ancestors(ancestor, level + 1)
        
show_ancestors("Dipan Timalsina")