#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * sum_dlistint - sum of list.
 * @head: head.
 * Return: int.
 */
int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *h = head;

	if (head == NULL)
		return (0);

	while (h)
	{
		sum += h->n;
		h = h->next;
	}

	return (sum);
}
