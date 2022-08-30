#include <Python.h>




/**
 * print_python_list_info - print info.
 * @p: list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len  = PyList_Size(p), i;

	printf("[*] Size of the python List = %lu\n", len);
	printf("[*] Allocated = %li\n", (((PyObject *)(p))->allocated)

	for (i = 0, i < len; i++)
	{
		printf("Element %li: %s\n", i, Py_TYPE((((PyObject *)(p))->ob_item[i])->tp_name);
	}
}
