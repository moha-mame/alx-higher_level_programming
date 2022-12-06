#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list_info - C function that prints some basic info
 * about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int saved, size, i = 0;
	PyObject *obj;

	saved = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", saved);
	for (; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
