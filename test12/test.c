#include <stdio.h>
#include <stdlib.h>

typedef char linktype;
typedef struct linklist{
    linktype data;
    struct linklist *next;
}linklist;

void linklistinit(linklist **head)
{
    if(head == NULL)
    {
        return;
    }
    *head = NULL;
}

void linklistprint(linklist *head)
{
    if(head == NULL)
    {
        return;
    }
    linklist *cur = head;
    while(cur != NULL)
    {
        printf("%c",cur->data);
        cur = cur->next;
    }
    printf("\n");
}

linklist * creat(linktype value)
{
    linklist *newnode = (linklist*)malloc(sizeof(linklist));
    if(newnode == NULL)
    {
        return NULL;
    }
    newnode->data = value;
    newnode->next = NULL;
    return newnode;
}

void linklist_pushback(linklist **head,linktype value)
{
    if(head == NULL)
    {
        return;
    }
    if(*head == NULL)
    {
        *head = creat(value);
        return;
    }
    linklist *new = creat(value);
    linklist *cur = *head;
    while(cur ->next != NULL)
    {
        cur = cur->next;
    }
    cur->next = new;
}

linklist *merge1(linklist *head1,linklist *head2)
{
    linklist *newhead = NULL;
    if(head1 == NULL)
    {
        return head2;
    }
    if(head2 == NULL)
    {
        return head1;
    }
    else
    {
        if((head1->data) < (head2->data))
        {
            newhead = head1;
            newhead->next = merge1(head1->next,head2);
        }
        else
        {
            newhead = head2;
            newhead->next = merge1(head1,head2->next);
        }
        return newhead;

    }
}
linklist *merge2(linklist *head1,linklist *head2)
{
    linklist *newtail = NULL;
    linklist *newhead = NULL;
    if(head1 == NULL)
    {
        return head2;
    }
    if(head2 == NULL)
    {
        return head1;
    }
    if(head1->data <= head2->data)
    {
        newhead = head1;
        head1 = head1->next;
    }
    else
    {
        newhead = head2;
        head2 = head2->next;
    }
    newtail = newhead;
    while(head1 && head2)
    {
        if(head1->data < head2->data)
        {
            newtail->next = head1;
            head1 = head1->next;
        }
        else
        {
            newtail->next = head2;
            head2 = head2->next;
        }
        newtail = newtail->next;
    }
    if(head1 == NULL)
    {
        newtail->next = head2;
    }
    else
    {
        newtail->next = head1;
    }
        return newhead;
}
int main()
{
    linklist *head1;
    linklist *head2;
    linklistinit(&head1);
    linklistinit(&head2);
    linklist_pushback(&head1,'1');
    linklist_pushback(&head1,'3');
    linklist_pushback(&head1,'5');
    linklist_pushback(&head1,'7');
    linklist_pushback(&head2,'2');
    linklist_pushback(&head2,'4');
    linklist_pushback(&head2,'6');
    linklist_pushback(&head2,'8');
    linklist *head = merge1(head1,head2);
    linklistprint(head);
    linklist *head3;
    linklist *head4;
    linklistinit(&head3);
    linklistinit(&head4);
    linklist_pushback(&head3,'1');
    linklist_pushback(&head3,'3');
    linklist_pushback(&head3,'5');
    linklist_pushback(&head3,'7');
    linklist_pushback(&head4,'2');
    linklist_pushback(&head4,'4');
    linklist_pushback(&head4,'6');
    linklist_pushback(&head4,'8');
    linklist *head5 = merge2(head3,head4);
    linklistprint(head5);
    return 0;
}
