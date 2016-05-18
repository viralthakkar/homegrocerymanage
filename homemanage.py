def menu():
	option = -1;
	print "Welcome to Home Grocery Management Application"
        print "Your Tasks : "
        print "Add New Item : 1"
        print "Update Detail in Existing Item : 2"
        print "Delete Item : 3"
        print "View Item Detail : 4"
        print "Exit : 0"
	while(option):
		option = input("Enter your Action (0 to 4) :");
		if(option>4):
                        print "Please Enter your input between 0 to 4"
                        continue
                options = {
                        0:close,
                        1:add_item,
                        2:edit_item,
                        3:delete_item,
                        4:view_item_detail
                }
                options[option]()
	return
	
def add_item():
	print "Add Item";
	return
		
def edit_item():
	print "Edit Item";
	return
	
def delete_item():
	print "Delete Item";
	return

def view_item_detail():
	print "View Item Detail";
	return

def close():
        print "Thank you for using our application"
        print "You are successfull Exit from our application"
        exit
