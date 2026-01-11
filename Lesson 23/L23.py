student  = {'id1':{
    'name' : ['Sara'],
    'class' : ['V'],
    'subject' : ['English' , 'Math' , 'Science']
    },
    'id2':{
        'name' : ['Sam'],
        'class' : ['V'],
        'subject' : ['English' , 'Math' , 'Science']
    },
    'id3':{
        'name' : ['Sara'],
        'class' : ['V'],
        'subject' : ['English' , 'Math' , 'Science']
    },
    'id4':{
        'name' : ['John'],
        'class' : ['V'],
        'subject' : ['English' , 'Math' , 'Science']
    }

}
print(student)
result = {}
for key,value in student.items():
    if value not in result.values():
        result[key] = value
print(result)