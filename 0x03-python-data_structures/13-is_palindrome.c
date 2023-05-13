#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow->next;

	while (curr != NULL)
	{
		listint_t *next = curr->next;

		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *a = *head;
	listint_t *b = prev;

	while (a != NULL && b != NULL)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}
