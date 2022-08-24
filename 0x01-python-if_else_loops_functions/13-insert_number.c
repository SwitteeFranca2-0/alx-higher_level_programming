#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));

	temp = *head;

	new->n = number;
	new->next = NULL;

	if (head == NULL)
	{
		*head = new;
	}

	while(temp)
	{
		if (temp->n < number && temp->next && (temp->next)->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			break;
		}
		if (temp->n > number)
		{
			new->next = temp;
			temp = new;
			*head = temp;
			break;
		}
		temp = temp->next;
	}

	return (new);


}