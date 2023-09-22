# Help Desk ticketing System Prototype

# A ticketing system that allows customers to submit tickets and to be resolved by assistance

This project is a ticketing system that internal customers can use to submit tickets about any issues
that they may have, whether that be they would like to generate a new password or they need a new monitor.
The functions of this system are:

* Submitting a ticket (internal customers only)
* Viewing the tickets submitted (assistances ony)
* Resolving tickets submitted (assistances ony)
* Reopening tickets submitted (assistances ony)

The ticket details consist of:

* Ticket number
* Ticket creator
* Staff ID
* Email address
* Description

## How the project works
When the project first starts up a menu will be displayed with the four following options:

1. Submit a ticket
2. View the tickets
3. Respond to a ticket
4. Reopen a ticket

Each option leads to a different section.
The submitting a ticket section works by displaying each piece of information and getting the user to fill them out.
Once all the information is entered it displays the information and asks if the user wants any changes made.
If so it goes back to the start and if the user says no it sends the user back to the menu.

The viewing a ticket section first tells the user how many tickets have been created, how many are resolved and
how many have been solved, it then prints all the created tickets in order by ticket number.
To get to the menu the user just has to press enter.

The resolving and reopening tickets section both work in the same way, the system displays all of the open
or closed tickets (depending on the section), the system then gets the user to enter the staff ID of the ticket
they want to reopen or close.
If the user is in the closing tickets section it will display the issue and get the user to enter their solution.
If the user is in the reopening tickets section it will reopen the ticket and send you back to the menu.
