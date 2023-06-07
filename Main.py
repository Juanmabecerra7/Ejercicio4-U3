from ManejadorEmpleado import ManejadorEmpleados

if __name__=="__main__":
    dimension = int(input("ingrese la dimension del arrelos"))
    ME = ManejadorEmpleados(dimension=4)
    ME.cargarEmpleados()
    ME.mostrarEmpleados()
    dni = int(input("ingrese el dni de un empleado: "))
    horas = int(input("ingrese las cantidasd de horas trabajadas en el dia: "))
    ME.buscarDni (dni,horas)
    tarea = input("Ingrese una Tarea a buscar: ")
    ME.buscarTarea(tarea)
    ME.ayudaEconomica()
    ME.mostrarSalario()