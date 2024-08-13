class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def addLabToFile(self, laboratories_dict):
        laboratories_dict[self.lab_name] = self.cost
        self.writeListOfLabsToFile(laboratories_dict)

    def formatLabInfo(self):
        return f"{self.lab_name} {self.cost}"

    @staticmethod
    def readLaboratoriesFile():
        laboratories_dict = {}
        try:
            with open("laboratories.txt", "r") as file:
                lines = file.readlines()[1:]  
                for line in lines:
                    if line.strip():  
                        lab_name, cost = line.strip().split('_')
                        laboratories_dict[lab_name] = cost
        except FileNotFoundError:
            print("The file 'laboratories.txt' does not exist.")
        return laboratories_dict

    @staticmethod
    def writeListOfLabsToFile(laboratories_dict):
        with open("laboratories.txt", "w") as file:
            file.write("Lab_Cost\n") 
            for lab_name, cost in laboratories_dict.items():
                file.write(f"{lab_name}_{cost}\n")

    @staticmethod
    def enterLaboratoryInfo():
        lab_name = input("Enter Laboratory facility:\n\n").strip()  
        cost = input("Enter Laboratory cost:\n\n").strip() 
        return Laboratory(lab_name, cost)

    @staticmethod
    def displayLabsList(laboratories_dict):
        print(f"{'Lab':<20}{'Cost':<10}\n")  
        for lab_name, cost in laboratories_dict.items():
            print(f"{lab_name:<20}{cost:<10}\n")
        print("Back to the previous Menu")

    @staticmethod
    def laboratoriesMenu():
        while True:
            laboratories_dict = Laboratory.readLaboratoriesFile()

            print("Laboratories Menu:")
            print("1 - Display laboratories list")
            print("2 - Add laboratory")
            print("3 - Back to the Main Menu\n")

            choice = input().strip()
            if choice == "1":
                Laboratory.displayLabsList(laboratories_dict)
            elif choice == "2":
                new_lab = Laboratory.enterLaboratoryInfo()
                new_lab.addLabToFile(laboratories_dict)
                print("\nBack to the previous Menu")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

def main():
   
    print(f"{'***Welcome to Alberta Hospital Laboratories Management System!***':^75}")
   
    Laboratory.laboratoriesMenu()  

if __name__ == "__main__":
    main()
