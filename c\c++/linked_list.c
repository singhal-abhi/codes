#include<stdio.h>
#include<stdlib.h>
struct node
{
    int d;  //data
    struct  node *link;  //link
};
struct node* reverse (struct node *head)
{
    struct node *prev=(struct node*)malloc(sizeof(struct node)),*ptr=(struct node*)malloc(sizeof(struct node)),*next=(struct node*)malloc(sizeof(struct node));
    prev= NULL;
    ptr=next=head;
    while(ptr!=NULL)
    {
        next=ptr->link;
        ptr->link=prev;
        prev=ptr;
        ptr=next;
    }
    head=prev;
    return head;


}
struct node* insert(struct node *head)
{

    int d;
    struct node *temp=(struct node*)malloc(sizeof(struct node)),*ptr=(struct node*)malloc(sizeof(struct node));
    ptr=head;
    printf("enter data\n\t\t\t\t");
    scanf("%d",&d);
    temp->d=d;
    temp->link=NULL;
    if (head==NULL)
      head=temp;
    else
    {
        while(ptr->link!=NULL)
            ptr=ptr->link;
        ptr->link=temp;
    }
    return head;
}
void display_(struct node *head)
{
    struct node *ptr;
    ptr=head;
    printf("Linked list contains\n");
    while(ptr!=NULL)
    {
        printf("%d\t",ptr->d);
        ptr=ptr->link;
    }
    printf("\n");
}
void main()
{
    struct node* head=(struct node*)malloc(sizeof(struct node));
    head=NULL;
    int i=5;

    while(1000)
    {
    printf("enter\n1 to insert\n2 to reverse\n3 to display\nany other key to quit\n");
    scanf("%d",&i);
    if(i==1)
        head=insert(head);
    else if(i==2)
        head=reverse(head);
    else if(i==3)
        display_(head);
    else
        break;
    }
}

