from os import system
import random
class Users:
    def __init__(self):
        self.users_list = []
        
    def create_user(self):
        try:
            system("cls")
            name_complete = input("Ingrese su nombre completo: ")
            age = input("Ingrese su edad: ")
            email = input("Ingrese su correo: ")
            user_id = random.randint(1000, 9999)
            user = {
                "id" : user_id,
                "name" : name_complete,
                "age" : age,
                "email" : email 
            }
            self.users_list.append(user)
            input(f"El id del usuario es {user_id}")
            input("Presiona Enter para continuar...")  
        except ValueError:
            print("La edad debe ser un número entero")
            input("Presiona Enter para continuar...") 
        
    def visualizate_information(self):
        try: 
            system("cls")
            enter_id = int(input("Ingrese su id: "))
            user_Found = False
            for user in self.users_list:
                if user['id'] == enter_id:
                    user_Found = True
                    print(f"Información del usuario: \nNombre: {user['name']}\nEdad: {user['age']} \nCorreo: {user['email']}")
                    break
                if not user_Found:
                    print("El id es incorrecto")
            input("Presiona Enter para continuar...")
        except ValueError:
            print("ERROR EN VISUAZAR USUARIO")
            input("Presiona Enter para continuar...") 
            
    def visualizate_all_users(self):
        if not self.users_list:
            print("No hay usuarios para mostrar")
        else:
            print("Listados de usuarios: ")
            for user in self.users_list:
                print(f"ID: {user['id']} - Nombre: {user['name']}, Edad: {user['age']}, Correo: {user['email']}")
        input("Presiona Enter para continuar...")
        
    def delete_user(self):
        try:
            system("cls")
            enter_id = int(input("Ingrese el id del usuario"))
            not_Found = False
            for user in self.users_list:
                if user['id'] == enter_id:
                    self.users_list.remove(user)
                    not_Found = True
                    print("Su usuario fue eliminado correctamente")
                    break
            if not not_Found:
                print("El id es un correcto")
            print("Presiona enter para continuar")
            
        except ValueError:
            print("Error al eliminar un usuario")
            print("Presiona enter para continuar")
    
    def update_user(self):
        try:
            system('cls')
            enter_id = int(input("Ingrese el id del usuario: "))
            for user in self.users_list:
                if user['id'] != enter_id:
                    print("Usuario no encontrado")
                else:
                    user['name'] = input("Ingrese el nombre completo del usuario: ")
                    user['age'] = input("Ingrese la edad: ")
                    user['email'] = input("Ingrese el correo: ")
                    print("Usuario editado correctamente")
                    input("Presione enter para continuar")
                input("Presione enter para continuar")
        except ValueError:
            print("Error al editar usuario")
            input("Presiona enter para continuar")
                    
    def main(self):
        while True:
            system("cls")
            print('***********************************************************************')
            print('******************** Menu principal de usuarios **********************')
            print('***********************************************************************')
            print("1. Crear Usuario")
            print("2. Visualizar Usuario por ID")
            print("3. Visualizar Todos los Usuarios")
            print("4. Eliminar Usuario por ID")
            print("5. Editar usuario")
            print("0. Salir")
            print("**********************************************************")
            option = input('Ingrese su opción: ')
            if option == "1":
                self.create_user()
                
            elif option == "2":
                self.visualizate_information()
                
            elif option == "3":
                self.visualizate_all_users()
            
            elif option == "4":
                self.delete_user()
            
            elif option == "5":
                self.update_user()
                
            elif option == "0":
                break
            else:
                print("**************** DATO INVALIDO ***************")
                input("Presiona Enter para continuar...")

if __name__ == '__main__':
    users = Users()
    users.main()
