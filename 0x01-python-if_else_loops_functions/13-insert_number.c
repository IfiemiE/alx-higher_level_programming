#include "lists.h"

/**
  * insert_node - function that insert a number in a sorted
  * singly linked list
  * @head: head of the list
  * @n: number that will be inserted in the list
  * Return: the new address of the list
  */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new, *p = *head;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
            return (NULL);
        new->n = number;
        if ((p == NULL) || (p->n >= number))
        {
            new->next = p;
            *head = new;
            return (new);
        }
        while ((p != NULL) && ((p->next) != NULL) && (p->next->n < number))
        {
            p = p->next;
        }
        new->next = p->next;
        p->next = new;

        return (new);
}
