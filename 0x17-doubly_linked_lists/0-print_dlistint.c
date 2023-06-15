#include <stdio.h>
#include "lists.h"

/**
* print_dlistint - prints all the elements of a dlistint_t list.
* @h: first node
*
* Return: always success
*/

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *node = h;
	size_t count = 0;

	while (node != NULL)
	{
		printf("%d\n", node->n);
		count++;
		node = node->next;
	}

	return (count);
}
