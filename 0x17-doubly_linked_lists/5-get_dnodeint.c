#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
 * get_dnodeint_at_index - Get the dnodeint at index.
 * @head: head.
 * @index: index.
 * Return: dlistint_t*
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *h;
	int i = 0;

	h = head;

	while (h)
	{
		h =	h->next;
		i++;

		if (i == index)
		{
			return (h);
		}
	}

	return (NULL);
}
