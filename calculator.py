def menu():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")
 

def matrix_addition():
    try: 
        rows = int(input("Nhap so hang: "))
        columns = int(input("Nhap so cot: "))
        if rows <=0 or columns <=0: 
            print(f"Loi r, nhap so duong di b oi")
            return
    except ValueError:
        print(f"Hay nhap 1 so hop le ")
        return
    
    print(f"Nhap gia tri cho ma tran A ({rows}x{columns}):")
    matrix1 = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = input(f"Nhap gia tri cho [{i+1}][{j+1}]")
                    num_value=float(value)
                    row.append(num_value)
                    break
                except ValueError:
                    print(f" Sai roi, nhap lai")
        matrix1.append(row)
        
    print(f"Nhap gia tri cho ma tran B ({rows}x{columns}):")
    matrix2 = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = input(f"Nhap gia tri cho [{i+1}][{j+1}]")
                    num_value=float(value)
                    row.append(num_value)
                    break
                except ValueError:
                    print(f" Sai roi, nhap lai")
        matrix2.append(row)
    result = []
    for i in range(rows):
        result_row = []
        for j in range(columns):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)

    print(f"Ket qua")
    print("Ma tran 1: ")
    for row in matrix1:
        print(row)
    print("Ma tran 2: ")
    for row in matrix2:
        print(row)
    print("1 + 2: ")
    for row in result:
        print(row)
        
def matrix_multiplication():
    try: 
        rows1 = int(input(f"Nhap so hang cho ma tran 1: "))
        columns1 = int(input(f"Nhap so cot cho ma tran 1: "))
        
        if rows1 <= 0 or columns1 <=0:
            print(f"Sai r, nhap so duong di")
            return
    except ValueError:
        print("Sai roi, nhap so hop li di")
        return
    
    try: 
       rows2 = int(input(f"Nhap so hang cho ma tran 2: "))
       columns2 = int(input(f"Nhap so cot cho ma tran 2: "))
       
       if rows2 <= 0 or columns2 <=0:
            print(f"Sai r, nhap so duong di")
            return
    except ValueError:
        print("Sai roi, nhap so hop li di")
        return 
    
    if columns1 != rows2:
        print(f"Sai roi, nhap lai di ")
        return
    
    print(f"Nhap gia tri cho ma tran 1 ({rows1}x{columns1}): ")
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(columns1):
            while True:
                try:
                    value = input(f"Nhap gia tri cho [{i+1}][{j+1}]: ")
                    num_value = float(value)
                    row.append(num_value)
                    break
                except ValueError:
                    print("Sai roi, nhap lai di")
        matrix1.append(row)
        
    print(f"Nhap gia tri cho ma tran 2 ({rows2}x{columns2}): ")
    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(columns2):
            while True:
                try:
                    value = input(f"Nhap gia tri cho [{i+1}][{j+1}]: ")
                    num_value = float(value)
                    row.append(num_value)
                    break
                except ValueError:
                    print("Sai roi, nhap lai di")
        matrix2.append(row)
        
    result = []
    for i in range(rows1):
        result_row = []
        for j in range(columns2):
            sum_val = 0
            for k in range(columns1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            result_row.append(sum_val)
        result.append(result_row)
    
    print(f"Ket qua")
    print("Ma tran 1: ")
    for row in matrix1:
        print(row)
    print("Ma tran 2: ")
    for row in matrix2:
        print(row)
    print("1 x 2: ")
    for row in result:
        print("[" + "".join(f"{val:8.2f}" for val in row) + "]")
        
def main():
    print(f"Calculator")
    
    while True:
        menu()
        try: 
            choice = input("Chon yeu cau: ")
            
            if choice == '1':
                matrix_addition()
            elif choice == '2':
                pass
            elif choice == '3':
                matrix_multiplication()
            elif choice == '4':
                print(f"Bye")
                break
            else:
                print("Khong co lua chon nay")
        
        except KeyboardInterrupt:
            print("Bi cat ngang roi. Bye")

if __name__ == "__main__":
    main()
    