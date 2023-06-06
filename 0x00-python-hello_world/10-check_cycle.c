#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list: list to be checked
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list->next;
	listint_t *fast = list->next->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			slow = list;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
