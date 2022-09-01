#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *loop;
	size_t i = 0;

	loop = h;

	while (loop)
	{
		print("%d", loop->n);
		loop = loop->next;
		i++;
	}

	return (i);
}