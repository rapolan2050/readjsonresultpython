import json


def cargar_sueldos(archivo):
	"""Carga los sueldos desde un archivo JSON."""
	with open(archivo, 'r') as f:
		return json.load(f)


def filtrar_sueldos(sueldos, monto):
	"""Filtra la lista de sueldos mayores al monto especificado."""
	return [
		{'Name': empleado["Name"], 'Salary': empleado["Salary"]}
		for empleado in sueldos
		if empleado["Salary"] > monto
	]


def main():
	# Cargar sueldos desde el archivo
	sueldos = cargar_sueldos('sueldos.json')

	# Solicitar el monto mínimo
	monto_minimo = float(input("Introduce el monto mínimo para filtrar sueldos: "))

	# Filtrar sueldos mayores al monto especificado
	sueldos_filtrados = filtrar_sueldos(sueldos, monto_minimo)

	# Mostrar los resultados
	print("Sueldos mayores a", monto_minimo)
	for empleado in sueldos_filtrados:
		print(empleado)


if __name__ == "__main__":
	main()
