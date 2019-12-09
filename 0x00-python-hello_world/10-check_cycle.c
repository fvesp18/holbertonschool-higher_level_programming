#include "lists.h"
/**
 * check_cycle - checks if theres a loop inside of a linked list
 * @list: a list of links
 * Return: 0, 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slo = list, *fas = list;

	while (slo && fas && fas->next)
	{
		slo = slo->next;
		fas = fas->next->next;

		if (slo == fas)
			return(0);
	}
	return(1);
}
