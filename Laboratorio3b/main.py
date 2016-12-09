
import sys,os,pkgutil

def load_all_modules_from_dir(dirname):
    for importer, package_name, _ in pkgutil.iter_modules([dirname]):
        full_package_name = '%s.%s' % (dirname, package_name)
        if full_package_name not in sys.modules:
            module = importer.find_module(package_name
                        ).load_module(full_package_name)
            print module

def main():
	load_all_modules_from_dir('Ejercicio1')
	load_all_modules_from_dir('Ejercicio2')
	load_all_modules_from_dir('Ejercicio3')
	load_all_modules_from_dir('Ejercicio4')
	load_all_modules_from_dir('Ejercicio5')
	load_all_modules_from_dir('Ejercicio6')
	load_all_modules_from_dir('Ejercicio7')
	print "Archivo principal"

if __name__ == '__main__':
        main()
