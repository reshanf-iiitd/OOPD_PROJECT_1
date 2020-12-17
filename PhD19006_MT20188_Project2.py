#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import *


# list for the diffrent types of object


Applicants=[]
Hr_Admins=[]
Jobs=[]
Shortlisted_Candidates=[]
Selected_Candidates=[]
Employees=[]
Ex_Employees=[]



# In[74]:


class Person:
    def __init__(self,name):
        self.name=name
        
    ##################################### SHOWING Selected Candidates ######################################
    def show_selected_candidates():
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")
        y1=Label(show_job_screen,text="Selected Candidates" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Sr.no")
        y4=Label(show_job_screen,text="name")    
        y5=Label(show_job_screen,text="experience")    
        y6=Label(show_job_screen,text="board percentage")    
        y7=Label(show_job_screen,text="cpi")    
        y8=Label(show_job_screen,text="job_id")  

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        y6.grid(row=3,column=3)
        y7.grid(row=3,column=4)
        y8.grid(row=3,column=5)


        i=4

        for applicant in Selected_Candidates:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=applicant.name)
            x3=Label(show_job_screen,text=applicant.experience)
            x4=Label(show_job_screen,text=applicant.board_percentage)
            x5=Label(show_job_screen,text=applicant.cpi)
            x6=Label(show_job_screen,text=applicant.job_id)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
            x5.grid(row=i,column=4)
            x6.grid(row=i,column=5)
            i=i+1
        show_job_screen.mainloop()
    #show_selected_candidates()


# In[75]:


class Applicant(Person):
    def __init__(self,name,experience,board_percentage,cpi,job_id):
        super().__init__(name)
        
        self.experience=experience
        self.board_percentage=board_percentage
        self.cpi=cpi
        self.job_id=job_id
        
    def Register_on_Applicant_array(self):
        Applicants.append(self)
    
        


# In[76]:


class Job:
    def __init__(self,job_description,position,salary):
        self.job_description=job_description
        self.position=position
        self.salary=salary
        
    def Register(self):
        Jobs.append(self)
        

    ##################################### SHOWING JOB AVAIBLE ######################################
    def show_jobs_available(): 
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")

        y1=Label(show_job_screen,text="Available Jobs" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Job_code")
        y4=Label(show_job_screen,text="Job description")    
        y5=Label(show_job_screen,text="Position")    
        y6=Label(show_job_screen,text="Salary in thousands")      

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        y6.grid(row=3,column=3)


        i=4

        for job in Jobs:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=job.job_description)
            x3=Label(show_job_screen,text=job.position)
            x4=Label(show_job_screen,text=job.salary)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
            i=i+1
        show_job_screen.mainloop()
    #show_jobs_available()

##################################### SHOWING Applied CANDIDATES ######################################
    def show_applied_candidates():
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")
        y1=Label(show_job_screen,text="Applied candidates" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Sr.no")
        y4=Label(show_job_screen,text="name")    
        y5=Label(show_job_screen,text="experience")    
        y6=Label(show_job_screen,text="board percentage")    
        y7=Label(show_job_screen,text="cpi")    
        y8=Label(show_job_screen,text="job_id")  

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        y6.grid(row=3,column=3)
        y7.grid(row=3,column=4)
        y8.grid(row=3,column=5)


        i=4

        for applicant in Applicants:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=applicant.name)
            x3=Label(show_job_screen,text=applicant.experience)
            x4=Label(show_job_screen,text=applicant.board_percentage)
            x5=Label(show_job_screen,text=applicant.cpi)
            x6=Label(show_job_screen,text=applicant.job_id)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
            x5.grid(row=i,column=4)
            x6.grid(row=i,column=5)
            i=i+1
        show_job_screen.mainloop()
    #show_applied_candidates()
    


    ##########################################Creating new job #################################################
    ############################################################################################################
    def take_new_job_details():  

        def take_can():
            def close():
                temp2.destroy()
            job_description=name_entry.get()
            position=pos.get()
            salary=float(sal.get())
            job=Job(job_description,position,salary)
            job.Register()


            take_job_screen.destroy()
            temp2=tk.Tk()
            temp2.geometry("700x700")
            temp2.title("HR Recriting System")
            Label(temp2, text="Job Created Successfully !!!").pack()
            Label(temp2, text="").pack()
            Button(temp2, text="Close and Go Back", width=10, height=1,command=close).pack()

        take_job_screen=tk.Tk()
        take_job_screen.geometry("700x700")
        take_job_screen.title("HR Recruting System")

        Label(take_job_screen, text="Please enter New Job Details").pack()
        Label(take_job_screen, text="").pack()
        Label(take_job_screen, text="Job Description").pack()
        Label(take_job_screen, text="").pack()
        name = StringVar()
        name_entry = Entry(take_job_screen)
        name_entry.pack()
        Label(take_job_screen, text="Enter Salary").pack()
        salary = StringVar()
        sal = Entry(take_job_screen)
        sal.pack()
        Label(take_job_screen, text="").pack()

        Label(take_job_screen, text="Position").pack()
        position = StringVar()
        pos = Entry(take_job_screen)
        pos.pack()
        Label(take_job_screen, text="").pack()

        Button(take_job_screen, text="Submit", width=10, height=1,command=take_can).pack()
        take_job_screen.mainloop()



    #take_new_job_details()


# In[77]:


class Employee(Person):
    def __init__(self,name,job):
        super().__init__(name)
        self.job=job
        self.reason=None
    def Register(self):
        Employees.append(self)
        
    def Resign(self,id,reason):
        self.reason=reason
        Employees.pop(id-1)
        Ex_Employees.append(self)
        
        
        
        


# In[78]:


class hradmin(Person):
    def __init__(self,name,username,password):
        super().__init__(name)
        
        self.username=username
        self.password=password

    ##################################### SHOWING Previous Employee ######################################
    def show_ex_employees():
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")
        y1=Label(show_job_screen,text="Previous Employees" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Sr.no")
        y4=Label(show_job_screen,text="name")    
        y5=Label(show_job_screen,text="job_description") 
        y6=Label(show_job_screen,text="reason for leaving")

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        i=4

        for Employee in Ex_Employees:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=Employee.name)
            x3=Label(show_job_screen,text=Employee.job.job_description)
            x4=Label(show_job_screen,text=Employee.reason)
           # x4=Label(show_job_screen,text=Employee.job.position)
           # x5=Label(show_job_screen,text=Employee.job.salary)
            #x6=Label(show_job_screen,text=Employee.job.job_code)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
           # x5.grid(row=i,column=4)
            #x6.grid(row=i,column=5)
            i=i+1
        show_job_screen.mainloop()
        
        
    ##################################### SHOWING Employee Register ######################################
    def show_employee_register():
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")
        y1=Label(show_job_screen,text="Employee Register" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Sr.no")
        y4=Label(show_job_screen,text="name")    
        y5=Label(show_job_screen,text="job_description")    
        y6=Label(show_job_screen,text="position")    
        y7=Label(show_job_screen,text="salary in thousands")    
       # y8=Label(show_job_screen,text="job_id")  

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        y6.grid(row=3,column=3)
        y7.grid(row=3,column=4)
       # y8.grid(row=3,column=5)


        i=4

        for Employee in Employees:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=Employee.name)
            x3=Label(show_job_screen,text=Employee.job.job_description)
            x4=Label(show_job_screen,text=Employee.job.position)
            x5=Label(show_job_screen,text=Employee.job.salary)
            #x6=Label(show_job_screen,text=Employee.job.job_code)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
            x5.grid(row=i,column=4)
            #x6.grid(row=i,column=5)
            i=i+1
        show_job_screen.mainloop()
    #show_employee_register()
    
    ##################################### SHOWING Shortlisted Candidates ######################################
    def show_shortlisted_candidates():
        show_job_screen=tk.Tk()
        show_job_screen.geometry("700x700")
        show_job_screen.title("HR Recruting System")
        y1=Label(show_job_screen,text="Shortlisted Candidates" )
        y2=Label(show_job_screen,text=" ")
        y3=Label(show_job_screen,text="Sr.no")
        y4=Label(show_job_screen,text="name")    
        y5=Label(show_job_screen,text="experience")    
        y6=Label(show_job_screen,text="board percentage")    
        y7=Label(show_job_screen,text="cpi")    
        y8=Label(show_job_screen,text="job_id")  

        y1.grid(row=0,column=3)
        y2.grid(row=1,column=3)
        y3.grid(row=3,column=0)
        y4.grid(row=3,column=1)
        y5.grid(row=3,column=2)
        y6.grid(row=3,column=3)
        y7.grid(row=3,column=4)
        y8.grid(row=3,column=5)


        i=4

        for applicant in Shortlisted_Candidates:
            x1=Label(show_job_screen,text=i-3)
            x2=Label(show_job_screen,text=applicant.name)
            x3=Label(show_job_screen,text=applicant.experience)
            x4=Label(show_job_screen,text=applicant.board_percentage)
            x5=Label(show_job_screen,text=applicant.cpi)
            x6=Label(show_job_screen,text=applicant.job_id)
            x1.grid(row=i,column=0)
            x2.grid(row=i,column=1)
            x3.grid(row=i,column=2)
            x4.grid(row=i,column=3)
            x5.grid(row=i,column=4)
            x6.grid(row=i,column=5)
            i=i+1
        show_job_screen.mainloop()
    #show_shortlisted_candidates()
    
######################################## INTERVIEW PROCESS ##################################################
    def interview():

        def take_can():
            def take_can1():
                temp2.destroy()

            job_idd=int(job_code.get())
            no=int(number.get())
            arr=[]

            for applicant in Shortlisted_Candidates:
                if applicant.job_id==job_idd:
                    arr.append(applicant)

            import random
            res=random.sample(arr,no)

            for items in res :
                Selected_Candidates.append(items)

            shorlisting_screen.destroy()
            temp2=tk.Tk()
            temp2.geometry("700x700")
            temp2.title("HR Recriting System")
            Label(temp2, text="Interview  done !!!").pack()
            Label(temp2, text="").pack()
            Button(temp2, text="Close and Go Back", width=15, height=1,command=take_can1).pack() 
        shorlisting_screen=tk.Tk()
        shorlisting_screen.geometry("700x700")
        shorlisting_screen.title("HR Recruting System")

        Label(shorlisting_screen, text="Please enter job code for interview").pack()
        Label(shorlisting_screen, text="").pack()

        job_code = Entry(shorlisting_screen)
        job_code.pack()

        Label(shorlisting_screen, text="Enter number of candidates to be selected").pack()
        Label(shorlisting_screen, text="").pack()

        number = Entry(shorlisting_screen)
        number.pack()


        Button(shorlisting_screen, text="Take interview", width=10, height=1,command=take_can).pack()
        shorlisting_screen.mainloop()

    #interview()

    ################################## SHortlisting Candidates ##############################################
    def shortlist():


        def take_can():
            def take_can1():
                temp2.destroy()
            exp=int(name_entry.get())
            per=float(percentage.get())
            cpi=float(cpii.get())
            job_code=int(job.get())

            for applicant in Applicants:
                if applicant.job_id==job_code:

                    if applicant.experience>=exp and applicant.board_percentage>=per and applicant.cpi>=cpi:
                        Shortlisted_Candidates.append(applicant)






            shorlisting_screen.destroy()
            temp2=tk.Tk()
            temp2.geometry("700x700")
            temp2.title("HR Recriting System")
            Label(temp2, text="Shorlisting Successfully !!!").pack()
            Label(temp2, text="").pack()
            Button(temp2, text="Close and Go Back", width=15, height=1,command=take_can1).pack()







        shorlisting_screen=tk.Tk()
        shorlisting_screen.geometry("700x700")
        shorlisting_screen.title("HR Recruting System")

        Label(shorlisting_screen, text="Please enter Shorlisting Criteria").pack()
        Label(shorlisting_screen, text="").pack()
        Label(shorlisting_screen, text="Experience Required").pack()
        Label(shorlisting_screen, text="").pack()
        name = StringVar()
        name_entry = Entry(shorlisting_screen)
        name_entry.pack()
        Label(shorlisting_screen, text="Enter Minimum High School Percentage").pack()
        per = StringVar()
        percentage = Entry(shorlisting_screen)
        percentage.pack()
        Label(shorlisting_screen, text="").pack()

        Label(shorlisting_screen, text="Enter Minimun College CPI").pack()
        cpi = StringVar()
        cpii = Entry(shorlisting_screen)
        cpii.pack()
        Label(shorlisting_screen, text="").pack()

        Label(shorlisting_screen, text="Enter Job _code").pack()
        job_id = StringVar()
        job = Entry(shorlisting_screen)
        job.pack()
        Label(shorlisting_screen, text="").pack()


        Button(shorlisting_screen, text="Shortlist", width=10, height=1,command=take_can).pack()
        shorlisting_screen.mainloop()

    #shortlist()

    


# In[79]:


#################### making entry in Applicants list for testing  ###############
A1=Applicant('Shadman',2,90.6,8.2,1)
A1.Register_on_Applicant_array()
A2=Applicant('Vikash',3,86,7.9,2)
A2.Register_on_Applicant_array()
A3=Applicant('Sachin',4,93,8.4,1)
A3.Register_on_Applicant_array()
A4=Applicant('Vijay',1,76,9.5,3)
A4.Register_on_Applicant_array()
A5=Applicant('Ali',5,79,8.3,3)
A5.Register_on_Applicant_array()
A6=Applicant('Gautam',3,75,7.3,3)
A6.Register_on_Applicant_array()
A7=Applicant('Sunil',5,89,8.8,3)
A7.Register_on_Applicant_array()





################### making entry in Jobs list for testing ########################
J1=Job('software_developer','dept-manager',75)
J1.Register()
J2=Job('Accountant','clerk',48)
J2.Register()
J3=Job('Hr','manager',85)
J3.Register()



####################  making entry in Employees for testing ####################
E1=Employee('Rahul',J1)
E1.Register()
E2=Employee('Virat',J1)
E2.Register()
E3=Employee('Hardik',J2)
E3.Register()
E4=Employee('Ravindra',J2)
E4.Register()
E5=Employee('Chahal',J3)
E5.Register()
E6=Employee('Rohit',J3)
E6.Register()


# In[80]:


# class Ex_Employee(Employee):
#     def __init__(self,employee,reason):
#         self.name=employee.name
#         self.job_description.employee.job_description
#         self.reason=reason


# In[81]:


# for applicant in Applicants:
#     print (applicant.name,applicant.experience)
    
    
# for job in Jobs:
#     print (job.job_description,job.position,job.salary)
    
# for candidate in Shortlisted_Candidates:
#     print(candidate.name)

# for candidate in Selected_Candidates:
#     print(candidate.name) 
# Employees.remove(2)
for em in Ex_Employees:
     print(em.name)    


# In[82]:


######################### taking candidate data ##########################################
##########################################################################################
def take_candidate_screen():  
    
    def make_new_job():
        
        def close():
                
                temp2.destroy()
        name=name_entry.get()
        idd=int(job_id.get())
        experience=int(exp_year.get())
        percentage=float(high_school.get())
        cpi=float(college.get())
        A=Applicant(name,experience,percentage,cpi,idd)
        A.Register_on_Applicant_array()
        
        
        
        
        apply_candiate.destroy()
        temp2=tk.Tk()
        temp2.geometry("700x700")
        temp2.title("HR Recriting System")
        Label(temp2, text="Application Submitted!!!").pack()
        Label(temp2, text="").pack()
        Button(temp2, text="Close and Go Back", width=10, height=1,command=close).pack()
        
    
    apply_candiate=tk.Tk()
    apply_candiate.geometry("700x700")
    apply_candiate.title("HR Recruting System")
    
    Label(apply_candiate, text="Please enter your details").pack()
    Label(apply_candiate, text="").pack()
    Label(apply_candiate, text="Enter Name").pack()
    name = StringVar()
    name_entry = Entry(apply_candiate)
    name_entry.pack()
    Label(apply_candiate, text="Enter the job index for applying in the following available jobs").pack()
    idd = StringVar()
    job_id = Entry(apply_candiate)
    job_id.pack()
    Label(apply_candiate, text="").pack()
    
    Label(apply_candiate, text="Enter Work Experience in Years").pack()
    experience = StringVar()
    exp_year = Entry(apply_candiate)
    exp_year.pack()
    Label(apply_candiate, text="").pack()
    
    Label(apply_candiate, text="Enter High School Percentage").pack()
    percentage = StringVar()
    high_school = Entry(apply_candiate)
    high_school.pack()
    Label(apply_candiate, text="").pack()
    
    Label(apply_candiate, text="Enter College CPI").pack()
    cpi = StringVar()
    college = Entry(apply_candiate)
    college.pack()
    Label(apply_candiate, text="").pack()
    
    Button(apply_candiate, text="Submit", width=10, height=1,command=make_new_job).pack()
    apply_candiate.mainloop()
    

    
#take_candidate_screen()


# In[83]:


def Separate_Employee():
    
    def take_can():
        def take_can1():
            temp2.destroy()
        
        emp_idd=int(emp_id.get())
        reasonn=reason.get()
        i=0
        for i in range(len(Employees)):
            
            if i==emp_idd:
                Employees[i-1].Resign(i,reasonn)
        
        
        
       
        
        shorlisting_screen.destroy()
        temp2=tk.Tk()
        temp2.geometry("700x700")
        
        temp2.title("HR Recriting System")
        Label(temp2, text="Resignation Process done !!!").pack()
        Label(temp2, text="").pack()
        Button(temp2, text="Close and Go Back", width=15, height=1,command=take_can1).pack()
    
        
        
        
            
        
    
    shorlisting_screen=tk.Tk()
    shorlisting_screen.geometry("700x700")
    shorlisting_screen.title("HR Recruting System")
    
    Label(shorlisting_screen, text="Please Enter Employee Sr.no to be separated").pack()
    Label(shorlisting_screen, text="").pack()
    
    emp_id = Entry(shorlisting_screen)
    emp_id.pack()
    
    Label(shorlisting_screen, text="Mention the reason for separation").pack()
    Label(shorlisting_screen, text="").pack()
    
    reason = Entry(shorlisting_screen)
    reason.pack()
    
    
    Button(shorlisting_screen, text="Confirm", width=10, height=1,command=take_can).pack()
    shorlisting_screen.mainloop()
    
#Separate_Employee()
    
    


# In[84]:


def candidate_login_page():
    
    
    def back_to_main_page():
        
        candidate_login_screen.destroy()
        
        
    candidate_login_screen=tk.Tk()
    candidate_login_screen.geometry("700x700")
    candidate_login_screen.title("HR Recruting System")

    head=Label(candidate_login_screen,fg="lightcoral" ,bg="#7A1E0B",text="WELCOME  APPLICANT",font=('Helvetica',17,'bold'))
    head.pack()
    head.place(x=280,y=50)
    check_opening=Button(candidate_login_screen,text="Check Available Opening",bg="purple",fg="white",height=4,width=32,command = Job.show_jobs_available)#,command = hrloginwindow
    check_opening.place(x=300,y=100)
    
    apply=Button(candidate_login_screen,text="Apply For Job",bg="purple",fg="white",height=4,width=32,command=take_candidate_screen)#,command = hrloginwindow
    apply.place(x=300,y=200)
    
    show_selected=Button(candidate_login_screen,text="Selected Candidate",bg="purple",fg="white",height=4,width=32,command=Applicant.show_selected_candidates)#,command = hrloginwindow
    show_selected.place(x=300,y=300)


    go_to_back=Button(candidate_login_screen,text="Log Out and Go back to main Menu",bg="purple",fg="white",height=4,width=40,command =back_to_main_page)
    go_to_back.place(x=300,y=400)
    
    candidate_login_screen.mainloop()
    
#candidate_login_page()


# In[85]:


def recruitment_process_page():
    
    def back_to_admin_page():
        recruitment_process_screen.destroy()
        o5 = admin_window()
        
        o5.admin_page()
    recruitment_process_screen=tk.Tk()
    recruitment_process_screen.geometry("700x800")
    recruitment_process_screen.title("HR Recruting System")

    head=Label(recruitment_process_screen,fg="lightcoral" ,bg="#7A1E0B",text="Welcome Admin",font=('Helvetica',17,'bold'))
    head.pack()
    head.place(x=300,y=50)
    
    show_applied=Button(recruitment_process_screen,text="Show applied candidates",bg="purple",fg="white",height=4,width=32,command = Job.show_applied_candidates)#,command = hrloginwindow
    show_applied.place(x=300,y=170)
    
    create_new_job=Button(recruitment_process_screen,text="Create new Opening",bg="purple",fg="white",height=4,width=32,command = Job.take_new_job_details)#,command = hrloginwindow
    create_new_job.place(x=300,y=240)
    
    do_shortlisting=Button(recruitment_process_screen,text="Do Shortlisting",bg="purple",fg="white",height=4,width=32,command=hradmin.shortlist)#,command = hrloginwindow
    do_shortlisting.place(x=300,y=310)
    
    take_interview=Button(recruitment_process_screen,text="Interview ",bg="purple",fg="white",height=4,width=32,command=hradmin.interview)#,command = hrloginwindow
    take_interview.place(x=300,y=380)
    
    show_shortlisted=Button(recruitment_process_screen,text="Show Shortlisted Candidates",bg="purple",fg="white",height=4,width=32,command = hradmin.show_shortlisted_candidates)
    show_shortlisted.place(x=300,y=450)

    show_selected=Button(recruitment_process_screen,text="Show Selected Candidate",bg="purple",fg="white",height=4,width=32,command = hradmin.show_selected_candidates)
    show_selected.place(x=300,y=510)

    go_to_back=Button(recruitment_process_screen,text=" Go back to main Menu",bg="purple",fg="white",height=4,width=32,command =back_to_admin_page)
    go_to_back.place(x=300,y=570)
    
    recruitment_process_screen.mainloop()

#recruitment_process_page()


# In[86]:


class admin_window:
    def __init__(self):
        self.window_size="700x700"
        self.title = "HR Recruting System"
    

    def admin_page(self):


        def back_to_main_page():
            admin_screen.destroy()
        def go_to_recruitment_process_page():
            admin_screen.destroy()
            recruitment_process_page()
        def go_to_employee_management_process():
            admin_screen.destroy()
            employee_management_process()

        admin_screen=tk.Tk()
        admin_screen.geometry(self.window_size)
        admin_screen.title(self.title)

        head=Label(admin_screen,fg="lightcoral" ,bg="#7A1E0B",text="Welcome Admin",font=('Helvetica',17,'bold'))
        head.pack()
        head.place(x=290,y=50)
        recruitment_process=Button(admin_screen,text="Recruitement Process",bg="purple",fg="white",height=6,width=22,command =go_to_recruitment_process_page)#,command = hrloginwindow
        recruitment_process.place(x=300,y=100)

        employee_management=Button(admin_screen,text="Employee Management",bg="purple",fg="white",height=6,width=22,command = go_to_employee_management_process)
        employee_management.place(x=300,y=250)

        go_to_back=Button(admin_screen,text="Go Back ",bg="purple",fg="white",height=6,width=22,command = back_to_main_page)
        go_to_back.place(x=300,y=400)

        admin_screen.mainloop()


class hrwindow:
    

    def __init__(self):
        self.title = "HR Admin Login"
        self.size_window = "500x500"
    
    def hrloginwindow(self): 
        
        def p():
            password=password__login_entry.get()
            username=username_login_entry.get()
            hr1 = hradmin('Reshan','a','a')
            hr2 = hradmin('Shadman','b','b')
            if(hr1.username=="a" and hr1.password=="a" or hr2.username=="b" and hr1.password=="b"):
                login_screen.destroy()
                o3 = admin_window()
                o3.admin_page()
            else:
                login_screen.destroy()
                temp=tk.Tk()

                temp.title("Tmepory schecking")
                temp.geometry("500x500")


                Label(temp, text="Please Enter Correct User Name and Password").pack()
                Label(temp, text="").pack()

                go_to_back=Button(temp,text="Go Back ",bg="purple",fg="white",height=6,width=22,command = main1)
                go_to_back.place(x=300,y=400)


        login_screen=tk.Tk()


        # sets the title of the 
        # Toplevel widget 
        login_screen.title(self.title) 

        # sets the geometry of toplevel 
        login_screen.geometry(self.size_window) 

        # A Label widget to show in toplevel 
        Label(login_screen, text="Please enter login details").pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Username").pack()
        username = StringVar()
        username_login_entry = Entry(login_screen)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password").pack()
        password = StringVar()
        password__login_entry = Entry(login_screen, show= '*')
        password__login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1,command=p).pack()


def employee_management_process():
    def back_to_main_page():
        employee_management_screen.destroy()
        o4 = admin_window()
        o4.admin_page()
        
    employee_management_screen=tk.Tk()
    employee_management_screen.geometry("700x700")
    employee_management_screen.title("HR Recruting System")

    head=Label(employee_management_screen,fg="lightcoral" ,bg="#7A1E0B",text="Welcome Admin",font=('Helvetica',17,'bold'))
    head.pack()
    head.place(x=310,y=50)
    show_employee_list=Button(employee_management_screen,text="Show the Name of Employees",bg="purple",fg="white",height=4,width=32,command=hradmin.show_employee_register)#,command = hrloginwindow
    show_employee_list.place(x=300,y=100)
    
    
    show_left=Button(employee_management_screen,text="Show Empployee Who Left",bg="purple",fg="white",height=4,width=32,command=hradmin.show_ex_employees)#,command = hrloginwindow
    show_left.place(x=300,y=200)
    
    separate_employee=Button(employee_management_screen,text="Separate Employee",bg="purple",fg="white",height=4,width=32,command=Separate_Employee)
    separate_employee.place(x=300,y=300)

    go_to_back=Button(employee_management_screen,text=" Go back to main Menu",bg="purple",fg="white",height=4,width=32,command =back_to_main_page )
    go_to_back.place(x=300,y=400)
    
    
    employee_management_screen.mainloop()
#employee_management_process()


# In[89]:


class userGUI:
    title = "Welcome to IIITD HR Recruting Process"
    admin_login = "HR Admin Login"
    applicant_login= "Applicant Login"
    l_sel_stu = "List of Selected candidate"
    
    

    def main1(self):
        window=tk.Tk()
        window.geometry("700x700")
        window.title("HR Recruting System")

        head=Label(window,fg="lightcoral" ,bg="#7A1E0B",text=self.title,font=('Helvetica',17,'bold'))
        head.pack()
        head.place(x=190,y=50)
        o2 = hrwindow()
        hrlogin=Button(window,text=self.admin_login,bg="purple",fg="white",height=6,width=32,command = o2.hrloginwindow)
        hrlogin.place(x=300,y=100)

        positions=Button(window,text=self.applicant_login,bg="purple",fg="white",height=6,width=32,command = candidate_login_page)
        positions.place(x=300,y=250)

        selected=Button(window,text=self.l_sel_stu,bg="purple",fg="white",height=6,width=32,command=Person.show_selected_candidates)
        selected.place(x=300,y=400)


        window.mainloop()

start = userGUI()
start.main1()


# In[ ]:





# In[ ]:




