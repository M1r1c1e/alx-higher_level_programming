#include "lists.h"

/**
 * check_cycle - checking for the cycle in the singly linked list
 * @list: the head of the list
 * Return: if it is a no 0 or  1 if yes
 */

int check_cycle(listint_t *list)
{
	listint_t *speed, *calm = list;

	if (list == NULL)
		return (0);

	speed = list->next;
	while (calm != NULL && speed != NULL && speed->next != NULL)
	{
		if (calm == speed)
			return (1);
		speed = speed->next->next;
		calm = calm->next;
	}
	return (0);
}
