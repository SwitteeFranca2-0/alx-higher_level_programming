#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - free list.
 * @head: head.
 * Return: none.
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *h;

	h = head;
	while (h)
	{
		head = head->next;
		free(h);
		h = head;
	}

}
