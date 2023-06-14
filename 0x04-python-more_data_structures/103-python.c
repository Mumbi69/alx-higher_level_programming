#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints basic information on python bytes
 * @p: Python object pointer
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, s, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (s = 0; s < limit; i++)
		if (string[s] >= 0)
			printf(" %02x", string[s]);
		else
			printf(" %02x", 256 + string[s]);

	printf("\n");
}

/**
 * print_python_list - prints basic information on python lists
 * @p: python Object pointer
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, s;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (s = 0; s < size; s++)
	{
		obj = ((PyListObject *)p)->ob_item[s];
		printf("Element %ld: %s\n", s, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
