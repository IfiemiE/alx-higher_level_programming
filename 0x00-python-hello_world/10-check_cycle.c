#include "lists.h"

/**
  * check_cycle - checks a singly linked list whether there
  * is a loop/cycle or not
  * @list: a pointer to a (head of a) singly linked list
  *
  * Return: 0 if list has no cycle in it, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = slow = list;
	if (list == NULL)
		return (0);


	while ((fast != NULL) && (fast->next != NULL) && (slow != NULL))
	{
		slow = slow->next;
		fast = fast->next->next;
		if ((slow == fast)
			return (1);
	}

	return (0);
}
