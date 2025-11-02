#J1.LP0021
class Student:
    def __init__(self, student_id, name, semester, course_name ):
        self.student_id = student_id
        self.name = name
        self.semester = semester
        self.course_name = course_name
    def display_info(self):
        return f"{self.student_id:^10} {self.name:<20} {self.semester:^10} {self.course_name:^10}"

class StudentManager:
    def __init__(self):
        self.students = []
    
    def create_student(self):
        while True:
            try:
                student_id = int(input("Nhập ID hsinh: "))
                if any(student.student_id == student_id for student in self.students):
                    print("ID da ton tai, nhap cai khac di")
                    continue
                break
            except ValueError:
                print("ID sai dinh dang")

        name = input(f"Nhap ten hsinh: ").strip()
        while not name:
            print("Nhap ten vao")
            name = input("Nhap ten hsinh: ").strip()

        while True: 
            try: 
                semester = int(input("Nhap ky hoc: "))
                if semester <= 0:
                    print("Ki hoc sai dinh dang")
                    continue
                break
            except ValueError:
                print("Ki hoc sai dinh dang")


        print("Chọn: ")
        print("1. Java")
        print("2. .NET")
        print("3. C/C++")

        while True:
            choice = input("Chon khoa hoc tu 1-3: ")
            if choice == '1':
                course_name = "Java"
                break
            elif choice == '2':
                course_name = ".NET"
            elif choice == '3':
                course_name = "C/C++"
                break
            else: 
                print("Chon so di: ")

        new_student = Student(student_id, name, semester, course_name)
        self.students.append(new_student)
        print(f"Đã thêm học sinh {name} thành công!")

    def find_and_sort(self):
        if not self.students:
            print("Dsach trong")
            return
        
        search_name = input("Nhap ten hoc sinh: ").strip().lower()
        if search_name:
            filtered_students = [student for student in self.students if search_name in students.name.lower()]
        else:
            filtered_students = self.students.copy()
        
        if not filtered_students:
            print("Khong thay ai ca")
            return
        filtered_students.sort(key=lambda x:x.name)
        
        