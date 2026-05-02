#include "lists.h"

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	tmp = *head;
	for (i = 0; tmp && i < index; i++)
		tmp = tmp->next;

	if (tmp == NULL)
		return (-1);

	if (tmp->prev)
		tmp->prev->next = tmp->next;
	else
		*head = tmp->next;

	if (tmp->next)
		tmp->next->prev = tmp->prev;

	free(tmp);
	return (1);
}
