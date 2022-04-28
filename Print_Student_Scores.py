print("**********************STUDENT SCORES**********************")
def calculate_note(index):
    index = index[:-1]
    list = index.split(":")
    studentName = list[0]

    notes = list[1].split(",")
    print(notes)

    visaOne = int(notes[0])
    visaTwo = int(notes[1])
    final = int(notes[2])
    average = visaOne * (30/100) + visaTwo * (30/100) + final * (40/100)
    if average >= 90 and average <= 100:
        letter = "AA"
    if average >= 85 and average <= 89:
        letter = "BA"
    elif average >= 80 and average <= 84:
        letter = "BB"
    elif average >= 75 and average <= 79:
        letter = "CB"
    elif average >= 70 and average <= 74:
        letter = "CC"
    elif average >= 65 and average <= 69:
        letter = "DC"
    elif average >= 60 and average <= 64:
        letter = "DD"
    elif average >= 50 and average <= 59:
        letter = "FD"
    else:
        letter = "FF"
    return studentName + ":" + letter + "\n"

def read_averages():
    with open("exam_notes.txt", "r", encoding="utf = 8") as file:
        for index in file:
            print(calculate_note(index))

def enter_note():
    name = input("Student Name : ")
    surname = input("Student Surname : ")
    visaOne = (input("Visa 1 : "))
    visaTwo = (input("Visa 2 : "))
    final = (input("Final : "))
    with open("exam_notes.txt", "a", encoding="utf = 8") as file:
        file.write(name+" "+surname+":"+visaOne+","+visaTwo+","+final+"\n")
def save_note():
    with open("exam_notes.txt", "r", encoding="utf = 8") as file:
        letterNote = []
        for i in file:
            letterNote.append(calculate_note(i))
        with open("result.txt", "w", encoding="utf-8") as file2:
            for i in letterNote:
                file2.write(i)

while True:
    choice = input("1-Read notes\n2-Enter the note\n3-Save the notes\n4-Exit\n")
    if choice == "1":
        read_averages()
    elif choice == "2":
        enter_note()
    elif choice == "3":
        save_note()
    else:
        break
