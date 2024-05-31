student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
print(student)
print(type(student))
#add data into dict
student['city']= 'hyd'
print(student)
#how to fetch data from dict
n=student.get('city')
print(n)
print(student['name'])
#how to update data of dict
student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
student['name']='reddy'
print(student)
#how to delete data from dict
#1.del()
#2.pop()
student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
student.pop('marks')
del student['city']
print(student)

#key() method in dict
student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
student.keys()
print(student.keys())

#values() 
student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
student.values()
print(student.values())

#items()
student={'name':'vanna','id':'1234','city':'banglore','marks':'99'}
student.items()
print(student.items())
