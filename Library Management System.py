#from fileinput import close
#from sqlite3 import connect
from sre_parse import State
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime



    

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
        
    #=================================================variable==============================================================================
    
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.borrowed_var = StringVar()
        self.duedate_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.overdue_var = StringVar()
        self.actualprice_var = StringVar()
        self.daysonbook = StringVar()
        
        
        
        
        lbltitle=Label(self.root,text="Library Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"),padx=235, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0, y=130, width=1350, height=600)
        
        
        
        #================================================Data Frame Left=====================================================================
        
        DataFrameLeft=LabelFrame(frame,text="Library Membership ", bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=790, height=315)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type", font=("times new roman", 11, "bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",11,"bold"),width=27,textvariable=self.member_var, state="readonly")
        comMember["value"]=("Admin Staff", "Student","Lecturer")
        comMember.grid(row=0, column=1)
        
        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO.", font=("times new roman", 11, "bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.prn_var,width=27)
        txtPRN_NO.grid(row=1, column=1)
        
        lblFirstName = Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "First Name",padx=2, pady=6, bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.firstname_var,width=27)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName = Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Last Name",padx=2, pady=6, bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        lblLastName=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.lastname_var,width=27)
        lblLastName.grid(row=4, column=1)
        
        lblAddress1 = Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Address 1",padx=2, pady=6, bg="powder blue")
        lblAddress1.grid(row=5, column=0,sticky=W)
        lblAddress1=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.address1_var, width=27)
        lblAddress1.grid(row=5, column=1)
        
        lblAddress2= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Address 2",padx=2, pady=6, bg="powder blue")
        lblAddress2.grid(row=6, column=0,sticky=W)
        lblAddress2=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.address2_var, width=27)
        lblAddress2.grid(row=6, column=1)
        
        lblPostCode= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Pin Code ",padx=2, pady=6, bg="powder blue")
        lblPostCode.grid(row=7, column=0,sticky=W)
        lblPostCode=Entry(DataFrameLeft,font=("times new roman",11,"bold"),textvariable=self.postcode_var, width=27)
        lblPostCode.grid(row=7, column=1)
        
        lblMobile= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Mobile Number ",padx=2, pady=6, bg="powder blue")
        lblMobile.grid(row=8, column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.mobile_var,width=27)
        lblMobile.grid(row=8, column=1)
        
        #-----------------------------------Column 2 Data frame left-----------------------------------------------
        
        lblBook_Id= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Book ID ",padx=2, pady=6, bg="powder blue")
        lblBook_Id.grid(row=0, column=2,sticky=W)
        lblBook_Id=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.bookid_var, width=27)
        lblBook_Id.grid(row=0, column=3)
        
        
        lblBook_Title= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Book Title ",padx=2, pady=6, bg="powder blue")
        lblBook_Title.grid(row=1, column=2,sticky=W)
        lblBook_Title=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.booktitle_var, width=27)
        lblBook_Title.grid(row=1, column=3)
        
        
        lblAuther= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "AutherName",padx=2, pady=6, bg="powder blue")
        lblAuther.grid(row=3, column=2,sticky=W)
        lblAuther=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.auther_var, width=27)
        lblAuther.grid(row=3, column=3)
        
        
        lblDateBorrowed= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Date Borrowed",padx=2, pady=6, bg="powder blue")
        lblDateBorrowed.grid(row=4, column=2,sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.borrowed_var, width=27)
        lblDateBorrowed.grid(row=4, column=3)
        
        
        lblDueDate= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Date Due",padx=2, pady=6, bg="powder blue")
        lblDueDate.grid(row=5, column=2,sticky=W)
        lblDueDate=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.duedate_var, width=27)
        lblDueDate.grid(row=5, column=3)
              
        
        lblLateReturnFine= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Late Return Fine",padx=2, pady=6, bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2,sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.latereturnfine_var, width=27)
        lblLateReturnFine.grid(row=6, column=3)
        
        
        lblDateOverDue= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Date OverDue",padx=2, pady=6, bg="powder blue")
        lblDateOverDue.grid(row=7, column=2,sticky=W)
        lblDateOverDue=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.overdue_var, width=27)
        lblDateOverDue.grid(row=7, column=3)
        
        
        lblActualPrice= Label(DataFrameLeft, font = ("arial", 11, "bold"),text = "Actual Price",padx=2, pady=6, bg="powder blue")
        lblActualPrice.grid(row=8, column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,font=("times new roman",11,"bold"), textvariable=self.actualprice_var, width=27)
        lblActualPrice.grid(row=8, column=3)
        
        
        #--------------------------------------Data Frame Right------------------------------------------------------
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=800, y=5, width= 485, height=315)
        
        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=31, height=14, padx=1, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        listBooks = ["Clean Code: A Handbook of Agile Software Craftsmanship","Introduction to Algorithms",
                     "Structure and Interpretation of Computer Programs","The Clean Coder: A Code of Conduct for Professional Programmers",
                     "Code Complete: A Practical Handbook of Software Construction","Design Patterns: Elements of Reusable Object-Oriented Software",
                     "The Pragmatic Programmer","Head First Design Patterns: A Brain-Friendly Guide", 
                     "Refactoring: Improving the Design of Existing Code","The Art of Computer Programming, Volumes 1-4",
                     "2666","All About Love","Desert Solitaire","Disgrace",
                     "Geek Love", "Gilead", "Giovanni's Room",
                     "A Good Man Is Hard to Find and Other Stories."]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Clean Code: A Handbook of Agile Software Craftsmanship"):
                self.bookid_var.set("0001")
                self.booktitle_var.set("Clean Code: A Handbook of Agile Software Craftsmanship")
                self.auther_var.set("Robert Cecil Martin")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 650")
                
            elif (x=="Introduction to Algorithms"):
                self.bookid_var.set("0002")
                self.booktitle_var.set("Introduction to Algorithms")
                self.auther_var.set("Thomas H. Cormen")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 600")
            
            elif (x=="Structure and Interpretation of Computer Programs"):
                self.bookid_var.set("0003")
                self.booktitle_var.set("Structure and Interpretation of Computer Programs")
                self.auther_var.set("Gerald Jay Sussman")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 670")
                
            elif (x=="The Clean Coder: A Code of Conduct for Professional Programmers"):
                self.bookid_var.set("0004")
                self.booktitle_var.set("The Clean Coder: A Code of Conduct for Professional Programmers")
                self.auther_var.set("Robert Cecil Martin")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 800")
                
            elif (x=="Code Complete: A Practical Handbook of Software Construction"):
                self.bookid_var.set("0005")
                self.booktitle_var.set("Code Complete: A Practical Handbook of Software Construction")
                self.auther_var.set("Steven C. McConnell")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 720")
                
                
            elif (x=="Design Patterns: Elements of Reusable Object-Oriented Software"):
                self.bookid_var.set("0006")
                self.booktitle_var.set("Design Patterns: Elements of Reusable Object-Oriented Software")
                self.auther_var.set("Erich Gamma, Richard Helm")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 630")
                
            elif (x=="The Pragmatic Programmer"):
                self.bookid_var.set("0007")
                self.booktitle_var.set("The Pragmatic Programmer")
                self.auther_var.set("Andrew Hunt and David Thomas")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 600")
                
            elif (x=="Head First Design Patterns: A Brain-Friendly Guide"):
                self.bookid_var.set("0008")
                self.booktitle_var.set("Head First Design Patterns: A Brain-Friendly Guide")
                self.auther_var.set("Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 570")
                
            elif (x=="Refactoring: Improving the Design of Existing Code"):
                self.bookid_var.set("0009")
                self.booktitle_var.set("Refactoring: Improving the Design of Existing Code")
                self.auther_var.set("Kent Beck and Martin Fowler")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 1599")
                
            elif (x=="The Art of Computer Programming, Volumes 1-4"):
                self.bookid_var.set("0010")
                self.booktitle_var.set("The Art of Computer Programming, Volumes 1-4")
                self.auther_var.set("Donald Knuth")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 780")
                
            elif (x=="2666"):
                self.bookid_var.set("0011")
                self.booktitle_var.set("2666")
                self.auther_var.set("Roberto Bolaño")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 700")
                
            elif (x=="All About Love"):
                self.bookid_var.set("0012")
                self.booktitle_var.set("All About Love")
                self.auther_var.set("Bell Hooks")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 780")
                
            elif (x=="Desert Solitaire"):
                self.bookid_var.set("0013")
                self.booktitle_var.set("Desert Solitaire")
                self.auther_var.set("Edward Abbey")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 390")
                
            elif (x=="Disgrace"):
                self.bookid_var.set("0014")
                self.booktitle_var.set("Disgrace")
                self.auther_var.set("J. M. Coetzee")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 450")
                
            elif (x=="Geek Love"):
                self.bookid_var.set("0015")
                self.booktitle_var.set("Geek Love")
                self.auther_var.set("Katherine Dunn")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 345")
                
            elif (x=="Gilead"):
                self.bookid_var.set("0016")
                self.booktitle_var.set("Gilead")
                self.auther_var.set("Marilynne Robinson")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 465")
                
            elif (x=="Giovanni's Room"):
                self.bookid_var.set("0017")
                self.booktitle_var.set("Giovanni's Room")
                self.auther_var.set("James Baldwin")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 410") 
                
            elif (x=="A Good Man Is Hard to Find and Other Stories."):
                self.bookid_var.set("0018")
                self.booktitle_var.set("A Good Man Is Hard to Find and Other Stories.")
                self.auther_var.set("Mary Flannery O'Connor")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 777")
                
                
                
                
                
            
                
                
                
                
        
        
        
        listBox=Listbox(DataFrameRight,font=("arial",11,"bold"),width=18,height=13)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0, padx=1, pady=6)
        listScrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END, item)
        
        # =============================================Button Frames===========================================================
        
        
        framebuttons=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebuttons.place(x=0, y=470, width=1350, height=57)
        
        btnAddData=Button(framebuttons, command=self.add_data, text="Add Data", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnAddData=Button(framebuttons, command=self.showData, text="Show Data", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=1)
        
        btnAddData=Button(framebuttons, command=self.update, text="Update", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=2)
        
        btnAddData=Button(framebuttons, command=self.delete, text="Delete", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=3)
        
        btnAddData=Button(framebuttons, command=self.reset, text="Reset", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=4)
        
        btnAddData=Button(framebuttons, command=self.Exit, text="Exit", font =("arial",11,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0, column=5)
        # =============================================Information Frames===========================================================
        
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0, y=510, width=1350, height=225)
        
        
        Table_frame=Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2,width=1290, height=195)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame, column=("Member Type","PRN No","First Name","Last Name","Address 1",
                                                           "Address 2","Post ID","Mobile No.","Book Id","Book Title","Book Auther",
                                                           "Date Borrowed","Due Date","Late Return Fine","Date Overdue","Actual Price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("Member Type", text ="Member Type")
        self.library_table.heading("PRN No", text ="PRN No")
        self.library_table.heading("First Name", text ="First Name")
        self.library_table.heading("Last Name", text ="Last Name")
        self.library_table.heading("Address 1", text ="Address 1")
        self.library_table.heading("Address 2", text ="Address 2")
        self.library_table.heading("Post ID", text ="Post ID")
        self.library_table.heading("Mobile No.", text ="Mobile No")
        self.library_table.heading("Book Id", text ="Book Id")
        self.library_table.heading("Book Title", text ="Book Title")
        self.library_table.heading("Book Auther", text ="Book Auther")
        self.library_table.heading("Date Borrowed", text ="Date Borrowed")
        self.library_table.heading("Due Date", text ="Due Date")
        self.library_table.heading("Late Return Fine", text ="Late Return Fine")
        self.library_table.heading("Date Overdue", text ="Date Overdue")
        self.library_table.heading("Actual Price", text ="Actual Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("Member Type",width=100)
        self.library_table.column("PRN No",width=100)
        self.library_table.column("First Name",width=100)
        self.library_table.column("Last Name",width=100)
        self.library_table.column("Address 1",width=100)
        self.library_table.column("Address 2",width=100)
        self.library_table.column("Post ID",width=100)
        self.library_table.column("Mobile No.",width=100)
        self.library_table.column("Book Id",width=100)
        self.library_table.column("Book Title",width=100)
        self.library_table.column("Book Auther",width=100)
        self.library_table.column("Date Borrowed",width=100)
        self.library_table.column("Due Date",width=100)
        self.library_table.column("Late Return Fine",width=100)
        self.library_table.column("Date Overdue",width=100)
        self.library_table.column("Actual Price",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Rudra@0702", database="library_managemnt_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.auther_var.get(),
                                                                                                            self.borrowed_var.get(),
                                                                                                            self.duedate_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.overdue_var.get(),
                                                                                                            self.actualprice_var.get()
        ))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        
        messagebox.showinfo("Success","Member Has Been Added Successfully!!!")    
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rudra@0702",database="library_managemnt_system")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s, ID=%s, First_Name=%s, Last_Name=%s, Address1=%s, Address2=%s, Post_Id=%s, Mobile_No=%s, Book_Id=%s, Book_Title=%s, Date_Auther=%s, Borrowed_Date=%s, Due_Date=%s, Late_Return_Fine=%s, Date_OverDue=%s, Actual_Price=%s where PRN_NO=%s",(
                                                                                                            self.member_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.auther_var.get(),
                                                                                                            self.borrowed_var.get(),
                                                                                                            self.duedate_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.overdue_var.get(),
                                                                                                            self.actualprice_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success", "Member Has Been Updated!!!")
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rudra@0702",database="library_managemnt_system")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.firstname_var.set(row[2]),
        self.lastname_var.set(row[3]),
        self.address1_var.set(row[4]),
        self.address2_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobile_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.booktitle_var.set(row[9]),
        self.auther_var.set(row[10]),
        self.borrowed_var.set(row[11]),
        self.duedate_var.set(row[12]),
        self.latereturnfine_var.set(row[13]),
        self.overdue_var.set(row[14]),
        self.actualprice_var.set(row[15])
        
    
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address 1\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address 2\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post ID\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No.\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book Id\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Book Auther\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed\t\t"+ self.borrowed_var.get() + "\n")
        self.txtBox.insert(END,"Due Date\t\t"+ self.duedate_var.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date Overdue\t\t"+ self.overdue_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price\t\t"+ self.actualprice_var.get() + "\n")
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.borrowed_var.set(""),
        self.duedate_var.set(""),
        self.latereturnfine_var.set(""),
        self.overdue_var.set(""),
        self.actualprice_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Library Management System","Do You Want To Exit")
        if Exit>0:
            self.root.destroy()
            return
        
        
        
    def delete(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Rudra@0702",database="library_managemnt_system")  
            my_cursor=conn.cursor()
            query="delete from library where PRN_No=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member Has Been Deleted!!!")
        
                
                                                                                                            
                                                                                                            
        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()