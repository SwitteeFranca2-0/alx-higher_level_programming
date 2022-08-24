#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node.
 * @head: head.
 * @number: number
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if(new == NULL)
		return (NULL);


	temp = *head;

	new->n = number;
	
	if (*head == NULL || (*head)->n >= number) 
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (temp && temp->next && (temp->next)->n < number)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;

	return (new);
}
