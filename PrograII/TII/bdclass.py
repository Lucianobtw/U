from dataclasses import dataclass 
import mysql.connector as mysql
import matplotlib.pyplot as plt

@dataclass
class student:

    id: int ; name: str ; lname: str ; email: str ; age: int

try:
    mydb = mysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='Dataclasses'
        )

    if mydb.is_connected():
        print('\nSe ha conectado a la base de datos\n')

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM student")
    sentence = mycursor.fetchall()
    print(sentence)

except mysql.Error as x:
    print(x) ; exit(1)


def main():
    matrix = []
    with open('student.txt', 'a') as x:
        for y in range(5):
            matrix.append([])
        for i in sentence:
            object = (student(i[0], i[1], i[2], i[3], i[4]))
            x.write(f'{object.id} {object.name} {object.lname} {object.email} {object.age}\n')
            
            #print(object)

            matrix[0].insert(0, object.id)
            matrix[1].insert(1, object.name)
            matrix[2].insert(2, object.lname)
            matrix[3].insert(3, object.email)
            matrix[4].insert(4, object.age)

    plt.subplot(1,5,1)
    plt.title("Id")
    plt.hist(matrix[0])

    plt.subplot(1,5,2)
    plt.title("Names")
    plt.ylim(top=1,bottom=0)
    plt.yticks([0,1])
    plt.xticks(rotation=90)
    plt.xticks([1,10,20,30,40,50,60,70,80,90])
    plt.hist(matrix[1])

    plt.subplot(1,5,3)
    plt.title("Last Names")
    plt.ylim(top=1,bottom=0)
    plt.yticks([0,1])
    plt.xticks(rotation=90)
    plt.xticks([1,10,20,30,40,50,60,70,80,90])
    plt.hist(matrix[2])
    
    plt.subplot(1,5,4)
    plt.title("Emails")
    plt.ylim(top=1,bottom=0)
    plt.yticks([0,1])
    plt.xticks(rotation=90)
    plt.xticks([1,10,20,30,40,50,60,70,80,90])
    plt.hist(matrix[3])

    plt.subplot(1,5,5)
    plt.title("Ages")
    plt.hist(matrix[4])

    plt.show()

if __name__ == "__main__":
    main()
