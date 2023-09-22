id_list = ["2001", "2002", "2003"]
name_list = ["Inna", "Maria", "John"]
staffid_list = ["INNAM", "MARIAH", "JOHNS"]
email_list = ["inna@whitecliffe.co.nz", "maria@whitecliffe.co.nz", "john@whitecliffe.co.nz"]
issue_list = ["My monitor stopped working", "Request for a videocamera to conduct webinars", "Password change"]
response = ["Not Yet Provided", "Not Yet Provided", "New password generated: JOJoh"]
ticket_status = ["Open", "Open", "Closed"]
tickets_solved = 0
class ticket:

    def __init__(self, Staff_id, creator_name, email, issue):
        self.id = Staff_id
        self.id = staffid_list.append(staff_id)
        self.name = creator_name
        self.name = name_list.append(creator)
        self.email = email
        self.email = email_list.append(email)
        self.issue = issue
        self.issue = issue_list.append(description)
        self.TicketId = 2000 + len(name_list)
        self.TicketId = id_list.append(str(self.TicketId))
        self.auto_response = "Not Yet Provided"
        self.auto_response = response.append(self.auto_response)
        self.auto_status = "Open"
        self.auto_status = ticket_status.append(self.auto_status)


def ticket_view():
    tickets_solved = 0
    for i in range(len(ticket_status)):
        if ticket_status[i-1] == "Closed":
            tickets_solved +=1
    tick_created = int(len(id_list))
    tick_resolved = int(tickets_solved)
    tick_to_solve = tick_created - tick_resolved
    text = "Displaying Ticket Statistics\n\n"
    text = text + "Tickets Created: " + str(tick_created) + "\n"
    text = text + "Tickets Resolved: " + str(tick_resolved) + "\n"
    text = text + "Tickets To Solve: " + str(tick_to_solve) + "\n\n"
    
    text = text + "Printing Tickets:\n"
    for item in range(len(id_list)):
        text = text + "Ticket number: " + id_list[item] + "\n"
        text = text + "Ticket Creator: " + name_list[item].capitalize() + "\n"
        text = text + "Staff ID: " + staffid_list[item] + "\n"
        text = text + "Email Address: " + email_list[item] + "\n"
        text = text + "Description: " + issue_list[item].capitalize() + "\n"
        text = text + "Response: " + response[item] + "\n"
        text = text + "Ticket Status: " + ticket_status[item] + "\n\n"

    exit = input(text + "Enter anything to continue\n")
    menu()


def ticket_respond():
    index = []
    for i in range(len(id_list)):
        if ticket_status[i] == "Open":
            index.append(i)
    if index == []:
        print("There are no open tickets.")
        menu()
    text = ""
    item = 0
    for i in range(len(index)):
        item = int(index[i])
        text = text + "Ticket number: " + id_list[item] + "\n"
        text = text + "Ticket Creator: " + name_list[item] + "\n"
        text = text + "Staff ID: " + staffid_list[item] + "\n"
        text = text + "Email Address: " + email_list[item] + "\n"
        text = text + "Description: " + issue_list[item] + "\n"
        text = text + "Response: " + response[item] + "\n"
        text = text + "Ticket Status: " + ticket_status[item] + "\n\n"
    ticket_choice = input(text + "Enter the Staff ID of the ticket you want to respond to.\n").upper()
    if ticket_choice is None:
        menu()
    ticket_choice = staffid_list.index(ticket_choice)
    solution = input(issue_list[ticket_choice] + "\nEnter your solution:")
    if solution is None:
        menu()
    response[ticket_choice] = solution
    ticket_status[ticket_choice] = "Closed"
    menu()


def ticket_reopen():
    index = []
    for i in range(len(id_list)):
        if ticket_status[i] == "Closed":
            index.append(i)
    if index == []:
        print("There are no tickets to reopen.")
        menu()
    text = ""
    item = 0
    for i in range(len(index)):
        item = int(index[i])
        text = text + "Ticket number: " + id_list[item] + "\n"
        text = text + "Ticket Creator: " + name_list[item] + "\n"
        text = text + "Staff ID: " + staffid_list[item] + "\n"
        text = text + "Email Address: " + email_list[item] + "\n"
        text = text + "Description: " + issue_list[item] + "\n"
        text = text + "Response: " + response[item] + "\n"
        text = text + "Ticket Status: " + ticket_status[item] + "\n\n"
    ticket_choice = input(text + "Enter the Staff ID of the ticket you want to reopen.\n").upper()
    if ticket_choice is None:
        menu()
    ticket_choice = staffid_list.index(ticket_choice)
    response[ticket_choice] = "Not Yet Provided"
    ticket_status[ticket_choice] = "Open"
    menu()
    

def ticket_create():
    global text, details
    print(text)
    Staff_ID = input("Enter Staff ID\n").upper()
    if Staff_ID is None:
        menu()
    details.append(Staff_ID)
    creator_name = input("Enter name\n").capitalize()
    if creator_name is None:
        menu()
    details.append(creator_name)
    Contact_email = input("Enter email\n")
    if Contact_email is None:
        menu()
    details.append(Contact_email)
    Issue_Description = input("What is your issue?\n").lower()
    if Issue_Description is None:
        menu()
    details.append(Issue_Description)
    if details is None:
        menu()
    error_check()

def error_check():
    global text, details, names, staff_id, creator, email, description
    while 1:
        if details == None:  # checks if the user fills in all the information
            break
        text = ''
        for i in range(len(details)):
            if details[i].strip() == '':
                text = text + '''"%s" is  required.\n''' % details[i]
        if text != '':  # no problems found
            error_check()
        break   
    staff_id = details[0]
    creator = details[1].capitalize()
    email = details[2]
    description = details[3]
    redo = input("\n\nWould you like to make any changes?\n\n" + "Staff ID: " + staff_id + "\n" + "Ticket creator name: " + creator + "\n" + "Contact Email: " + email + "\n" + "Issue Description: " + description + "\nyes, no\n")
    if redo == "yes":
        error_check()
    
    description = description.lower()
    if "password" in description and "change" in description:
        new_pswd = ""
        staff_id_temp = list(staff_id)
        creator_temp = list(creator)
        new_pswd = new_pswd + staff_id_temp[0] + staff_id_temp[1] + creator_temp[0] + creator_temp[1] + creator_temp[2]

    new_ticket = ticket(staff_id, creator, email, description)
    if "password" in description and "change" in description:
        item = len(id_list)
        item = item - 1
        response[item] = "New password generated: " + new_pswd
        ticket_status[item] = "Closed"
    menu() 

def menu():
    global details, text
    text = "Ticket submission\n\n1.Submit a Ticket\n2.View tickets\n3.Respond To a Ticket\n4.Reopen a ticket\n"
    menu = input(text)
    if menu == "1":
        details = []
        text = "Enter Ticket details below"
        ticket_create()
    elif menu == "2":
        ticket_view()
    elif menu == "3":
        ticket_respond()
    elif menu == "4":
        ticket_reopen()


menu()