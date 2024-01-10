#include "lists.h"

/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */
void reverse(listint_t **h_r)
{
	listint_t *prev;
	listint_t *crr;
	listint_t *nxt;

	prev = NULL;
	crr = *h_r;

	while (crr != NULL)
	{
		nxt = crr->next;
		crr->next = prev;
		prev = crr;
		crr = nxt;
	}

	*h_r = prev;
}

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if equals, 0 if not
 */
int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prv_slow;
	listint_t *scan_half, *middle;
	int isp;

	slow = fast = prv_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prv_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scan_half = slow;
		prv_slow->next = NULL;
		reverse(&scan_half);
		isp = compare(*head, scan_half);

		if (middle != NULL)
		{
			prv_slow->next = middle;
			middle->next = scan_half;
		}
		else
		{
			prv_slow->next = scan_half;
		}
	}

	return (isp);
}
