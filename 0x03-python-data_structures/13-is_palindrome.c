#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - is palindrome.
 * @head: head.
 * Return: int.
 */
int is_palindrome(listint_t **head)
{
	int *p;
	int j = 0, i = 0, c;
	listint_t *temp;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		i++;
	}

	temp = *head;
	p = malloc(sizeof(int) * i);
	if (p == NULL)
		return (0);

	while (temp)
	{
		p[j] = temp->n;
		temp = temp->next;
		j++;
	}

	for (c = 0, j = (i - 1); c < i / 2; c++, j--)
	{
		if (p[c] != p[j])
		{
			free(p);
			return (0);
		}
	}

	free(p);
	return (1);
}
