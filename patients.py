# from PIL import Image
class Patients:
    def __init__(self , name, age, gender, email, phone_number, dob,image=None,id=None, disease=[], medicines=[], notes="",
                 date_of_visits=[]):
        self.id=id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.dob=dob
        self.image = image
        self.diseases = disease
        self.medicines = medicines
        self.notes = notes
        self.date_of_visit = date_of_visits

    #Function for testing if patient object is created or not

    def printDetails(self):
        print(self.name)
        print(self.gender)
        print(self.email)
        print(self.phone_number)
        print(self.age)
        print(self.dob)



    # Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getEmail(self):
        return self.email

    def getPhoneNumber(self):
        return self.phone_number

    def getImage(self):
        return self.image

    def getDiseases(self):
        return self.diseases

    def getMedicines(self):
        return self.medicines

    def getNotes(self):
        return self.notes

    def getDates(self):
        return self.date_of_visit

    # Setters
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender

    def setEmail(self, email):
        self.email = email

    def setPhoneNumber(self, phone_num):
        self.phone_number = phone_num

    def setImage(self, image):
        self.image = image

    def setDiseases(self,disease):
        disease = disease.split(',')
        self.diseases.extend(disease)

    def setMedicines(self,med):
        med = med.split(',')
        self.medicines.extend(med)

    def setNotes(self,notes):
        self.notes += notes

    def setDate(self,date):
        self.date_of_visit.extend(date)
