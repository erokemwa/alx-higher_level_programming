#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


/**
 *reverse_listint- reverses a listint_t
 *@head: the head of the list to be reversed
 *Return: a pointer to new head (tail)
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (*head)
	{
		next = (*head)->next;

		(*head)->next = prev;

		prev = *head;
		*head = next;
	}
	*head = prev;

	return (*head);
}



/**
 *is_palindrome - checks to see if a listint_t is a palendrome
 *@head: head of the listint_t
 *Return: 0 if is not pal 1 if is
 */

int is_palindrome(listint_t **head)
{
	int i;
	listint_t *back = *head;
	listint_t *begin = *head;

	if (*head == NULL)
		return (1);
	for (i = 0; 1; i++)
	{
		if (back->next == NULL)
		{
			i = 1;
			break;
		}
		if (back->next->next == NULL)
		{
			i = 2;
			break;
		}
		begin = begin->next;
		back = back->next->next;
	}
	back = begin->next;
	begin->next = NULL;
	*head = reverse_listint(head);
	if (i % 2 == 1)
		*head = (*head)->next;
	while (back != NULL && *head != NULL)
	{
		if (back->n != (*head)->n)
			return (0);
		back = back->next;
		*head = (*head)->next;
	}
	return (1);
}
