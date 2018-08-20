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
linklist *linklist_find(linklist *head,linktype value)
{
    if(head == NULL)
    {
        return NULL;
    }
    linklist *cur = head;
    while(cur != NULL)
    {
        if(cur->data == value)
        {
            return cur;
        }
        cur = cur->next;
    }
    return NULL;
}
linklist *linklist_getenter(linklist *head)
{
    if(head == NULL)
    {
        return;
    }
    else
    {
        linklist *fast = head;
        linklist *slow = head;
        while(fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow )
            {
                linklist *meet = fast;
                linklist *cur = head;
                while(meet != cur)
                {
                    meet = meet->next;
                    cur = cur->next;
                }
                return meet;
            }
        }
        return NULL;
    }
}
linklist *cross(linklist *head1,linklist *head2)
{
    if(head1 == NULL || head2 == NULL)
    {
        return NULL;
    }
    linklist *cur1 = head1;
    linklist *cur2 = head2;
    int len1 = 0;
    int len2 = 0;
    while(cur1->next != NULL)
    {
        ++len1;
        cur1 = cur1->next;
    }
    while(cur2->next != NULL)
    {
        ++len2;
        cur2 = cur2->next;
    }
    if(cur1->data = cur2->data)
    {
        if(len1 > len2)
        {
            linklist *new1 = head1;
            linklist *new2 = head2;
            int len = len1 - len2;
            while(len)
            {
                new1 = new1->next;
                len--;
            }
            while(new1->data != new2->data)
            {
                new1 = new1->next;
                new2 = new2->next;
            }
            return new1;
        }
        else
        {
            linklist *new1 = head1;
            linklist *new2 = head2;
            int len = len2 - len1;
            while(len)
            {
                new2 = new2->next;
                len--;
            }
            while(new1->data != new2->data)
            {
                new1 = new1->next;
                new2 = new2->next;
            }
            return new1;
        }
    }
    return NULL;
}
linklist *linklist_union(linklist *head1,linklist *head2)
{
    if(head1 == NULL)
    {
        return;
    }
    if(head2 == NULL)
    {
        return;
    }
    linklist *cur1 = head1;
    linklist *cur2 = head2;
    linklist *newhead = NULL;
    linklist *newtail = NULL;
    for(;cur1 != NULL;cur1 = cur1->next)
    {
        for(cur2 = head2;cur2 != NULL;cur2 = cur2->next)
        {
            if(cur1->data == cur2->data)
            {
                if(newhead == NULL && newtail == NULL)
                {
                    newhead = newtail = cur2;
                }
                else
                {
                    newtail->next = cur2;
                    newtail = newtail->next;
                }
            }
        }
    }
    return newhead;
}

int main()
{
    linklist *head1;
    linklistinit(&head1);
    linklist_pushback(&head1,'a');
    linklist_pushback(&head1,'b');
    linklist_pushback(&head1,'c');
    linklist_pushback(&head1,'d');
    linklist_pushback(&head1,'e');
    linklist *head2;
    linklistinit(&head2);
    linklist_pushback(&head2,'a');
    linklist_pushback(&head2,'b');
    linklist_pushback(&head2,'c');
    linklist_pushback(&head2,'h');
    linklist_pushback(&head2,'g');
    linklist_pushback(&head2,'j');
    //linklist *cur = linklist_find(head2,'j');
    //cur->next = linklist_find(head1,'d');
    //linklist *cro = cross(head1,head2);
    //linklist *enter = linklist_getenter(head);
    //printf("%c,%p\n",cro->data,cro);
    linklist *cur = linklist_union(head1,head2);
    for(cur;cur != NULL;cur = cur->next)
    {
        printf("%c\n",cur->data);
    }
    return 0;
}
