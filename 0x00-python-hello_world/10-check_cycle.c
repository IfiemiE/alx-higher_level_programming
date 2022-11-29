#include "lists.h"

/**
  * @list: a pointer to a (head of a) singly linked list
  *
  * Return: 0 if list has no cycle in it, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *knot, *p;

	knot = p = list;
	if (list == NULL)
		return (0);
	while (knot != NULL)
	{
		while (p != NULL)
		{
			p = p->next;
			if (p == knot)
				return (1);
