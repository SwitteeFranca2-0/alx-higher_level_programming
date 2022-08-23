#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check cycle.
 * @list: list.
 * Return: int.
 */
int check_cycle(listint_t *list)
{
	listint_t *next;
	listint_t *new;

	next = list;

	while (list != NULL)
	{
		new = list;
		list = list->next;
		while (new && new != list)
		{
			new = new->next;
			if (new == next)
			{
				return (1);
			}
		}
		if (list == next)
		{
			return (1);
		}

	}
	return (0);
}
