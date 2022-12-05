#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the first element in the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *node_up = NULL, *node_down = NULL;
	int len = 0, i;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	node_up = *head;
	node_down = *head;
	while (node_down->next != NULL)
	{
		node_down = node_down->next;
		len = len + 1;
	}
	while (len >= 0)
	{
		if (node_up->n != node_down->n)
			return (0);
		node_up = node_up->next;
		node_down = node_up;
		len = len - 2;
		for (i = 1; i <= len; i++)
			node_down = node_down->next;
	}
	return (1);
}
