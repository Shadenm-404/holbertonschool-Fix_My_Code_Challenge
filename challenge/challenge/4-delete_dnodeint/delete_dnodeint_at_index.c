#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes a node at a specific index
 * @head: pointer to the head of the list
 * @index: index of the node to delete
 *
 * Return: 1 if successful, -1 if failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int i;

	if (head == NULL || *head == NULL)
		return (-1);

	tmp = *head;
	for (i = 0; tmp != NULL && i < index; i++)
		tmp = tmp->next;

	if (tmp == NULL)
		return (-1);

	if (tmp->prev != NULL)
		tmp->prev->next = tmp->next;
	else
		*head = tmp->next;

	if (tmp->next != NULL)
		tmp->next->prev = tmp->prev;

	free(tmp);
	return (1);
}
