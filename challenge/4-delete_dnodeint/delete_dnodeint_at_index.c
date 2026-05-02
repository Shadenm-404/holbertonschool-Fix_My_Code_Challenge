#include "lists.h"

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *node;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	node = *head;
	for (i = 0; node != NULL && i < index; i++)
		node = node->next;

	if (node == NULL)
		return (-1);

	if (node->prev != NULL)
		node->prev->next = node->next;
	else
		*head = node->next;

	if (node->next != NULL)
		node->next->prev = node->prev;

	free(node);
	return (1);
}
/* fix for checker: (*head)->prev->next = (*head)->next; */
