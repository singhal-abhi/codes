#include<stdio.h>
#include<stdlib.h>
struct node
{
    int d;
    struct node *link;
};
struct node* create(struct node *head)
{
    int d;
    scanf("%d",&d);
    head->d=d;
    head->link=NULL;
    return head;
}
struct node* delete_(struct node *head)
{
    struct node *ptr,*temp;
    temp=ptr=head;
    int d;
    printf("enter info to be deleted");
    scanf("%d",&d);
    while(ptr->d!=d)
    {
        temp=ptr;
        ptr=ptr->link;
    }
    temp->link=ptr->link;
    return head;
}
struct node* display(struct node *head)
{
    struct node *ptr;
    ptr=head;
    while(ptr!=NULL)
        printf("%d\t",ptr->d);
    return head;
}
struct node* insert(struct node *head)
{
    struct node *temp,*ptr;
    ptr=head;
    int d;
    printf("enter data to insert");
    scanf("%d",&d);
    temp->d=d;
    temp->link=NULL;
    while(ptr->link!=NULL)
        ptr=ptr->link;
    ptr->link=temp;
    return head;
};
void main()
{
    struct node *head;
    head=(struct node *)malloc(sizeof(struct node));
    int d;
    printf("Enter\n1 to create\n2 to insert at end\n3 to delete using value\n 4 to display\n5 to exit\n");
    scanf("%d",&d);
    while(1)
    switch(d)
    {
        case 1:head=create(head);
        break;
        case 2:head=insert(head);
        break;
        case 3:head=delete_(head);
        break;
        case 4:head=display(head);
        break;
        case 5:
            exit(0);
    }
}
