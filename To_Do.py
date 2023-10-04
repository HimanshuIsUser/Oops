from typing import Any

class Task:
    priority_options = {"Low","Medium","High"}
    def __init__(self,title,description,due_date,priority = "Low") -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False
        if priority in self.priority_options:
            self.priority = priority
        else:
            return ValueError(f'Invalid type of priority {self.priority}')
        
    def __str__(self) -> str:
        return print(f'{self.title} : {self.status}')

class To_Do:
    task_list = []

    def AddTask(self,obj):
        self.task_list.append(obj)
        return print(str(obj.title))
    
    def printlist(self):
        data = [i.title for i in self.task_list]
        return data
    
    def getlist(self):
        data = [i for i in self.task_list]
        return data
    
    def getAllDetials(self):
        data = [f'{i.title} , {i.description} , {i.due_date} , {i.priority} , {i.status}' for i in self.task_list]
        strdata = "\n".join(data)
        return print(strdata)
    
    def complete(self,obj):
        if isinstance(obj,Task):
            obj.status = "Completed"
            return self.getAllDetials()
    
    def remove(self,obj):
        if isinstance(obj,Task):
            self.task_list.remove(obj)
            print("Task removed !!")
            return self.getAllDetials()
        
def get_object_index(user_object):
    data = user_object.printlist()
    print(data)
    user_input = 0
    length = len(data) + 1
    while user_input<=0 or user_input > length:
        user_input = int(input("\nEnter the index number to select any task or Y to Exit : "))
        if user_input == "Y": 
            break
    userdata = user_object.getlist()
    final = userdata[user_input-1]
    return final

if __name__=="__main__":

    print("\n\nWelcome to   ***  To Do List  ***   programe")
    user_object = ""
    while True:
        print("\n\n\t\t** Menu **")
        print("1 Add Task\t\t\t","2 List Task\n","\n3 Mark Task as Completed\t","4 Remove Task\n\n","\t\t5 Exit\n")
        user_input = int(input("Choose Your option : "))
        if user_input >5 or user_input <1:
            print("\n\nPlease choose a valid Options !!  Try again....")
            user_input = str(input("\nEnter any key to continue Or press X to Exit : "))
            if user_input=="X":
                break
            else:
                continue
        elif user_input==1:
            title = str(input("Enter the title for your task : "))
            description = str(input("Enter your task description : "))
            due_date = str(input("Enter your task due date : "))
            priority = str(input("Enter the priority for this task (Optional) : "))

            task_object = Task(title,description,due_date,priority)
            user_object = To_Do()
            user_object.AddTask(task_object)
        elif user_input == 5:
            break
        elif user_input==2:
            user_object.getAllDetials()
        elif user_input==3:
            object = get_object_index(user_object)
            user_object.complete(object)
        elif user_input == 4:
            object = get_object_index(user_object)
            user_object.remove(object)



# obj = Task("FirstTask","it is testing","3-10-2023")
# t =To_Do()
# t.AddTask(obj)
# obj2 = Task("secondTask","it is testing","3-10-2023")
# # obj.getlist/
# t.AddTask(obj2)
# t.getlist()
# t.complete(obj2)
# t.remove(obj2)