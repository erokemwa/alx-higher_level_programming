#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: start of linked list
 *@number: the number stored in the node to insert
 *Return: the address of the new node or NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *nhead;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	nhead = *head;
	current = *head;

	while(current->next != NULL && current->next->n < number)
	{
		current = current->next;
		if (nhead->next == NULL)
			break;
		nhead = nhead->next;
	}

	if (nhead != NULL)
	{
		nhead = nhead->next;
		new->next = nhead;
	}
	else
		new->next = NULL;
	current->next = new;
	return (new);
}
