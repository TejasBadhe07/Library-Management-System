from sre_parse import State
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import tkinter
import datetime



    

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
        
        # Make window responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Store data in memory instead of database
        self.library_data = []
        
        # Variable declarations
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
        
        # Custom colors - Modern and professional color scheme
        self.bg_color = "#f8f9fa"  # Light gray background
        self.header_bg = "#1a237e"  # Deep blue header
        self.frame_bg = "#ffffff"   # White frame background
        self.button_bg = "#1976d2"  # Material blue buttons
        self.button_fg = "#ffffff"  # White button text
        self.accent_color = "#d32f2f"  # Red accent
        self.text_color = "#212121"  # Dark gray text
        self.border_color = "#e0e0e0"  # Light gray borders
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        
        # Title
        lbltitle=Label(self.root,text="Library Management System", 
                      bg=self.header_bg, fg="white", bd=20, relief=RIDGE, 
                      font=("Segoe UI", 30, "bold"), padx=235, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        # Main frame
        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg=self.frame_bg)
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Make main frame responsive
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
        # Left Frame
        DataFrameLeft=LabelFrame(frame, text="Library Membership", 
                               bg=self.frame_bg, fg=self.header_bg, bd=12, 
                               relief=RIDGE, font=("Segoe UI", 12, "bold"))
        DataFrameLeft.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Make left frame responsive
        DataFrameLeft.grid_rowconfigure(0, weight=1)
        DataFrameLeft.grid_columnconfigure(0, weight=1)
        DataFrameLeft.grid_columnconfigure(1, weight=1)
        
        # Right Frame
        DataFrameRight=LabelFrame(frame, text="Book Details",
                                bg=self.frame_bg, fg=self.header_bg, bd=12, 
                                relief=RIDGE, font=("Segoe UI", 12, "bold"))
        DataFrameRight.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Make right frame responsive
        DataFrameRight.grid_rowconfigure(0, weight=1)
        DataFrameRight.grid_columnconfigure(0, weight=1)
        DataFrameRight.grid_columnconfigure(1, weight=1)
        
        # Button Frame
        framebuttons=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg=self.frame_bg)
        framebuttons.pack(fill=X, padx=10, pady=10)
        
        # Make button frame responsive
        framebuttons.grid_columnconfigure(0, weight=1)
        framebuttons.grid_columnconfigure(1, weight=1)
        framebuttons.grid_columnconfigure(2, weight=1)
        framebuttons.grid_columnconfigure(3, weight=1)
        framebuttons.grid_columnconfigure(4, weight=1)
        framebuttons.grid_columnconfigure(5, weight=1)
        
        # Details Frame
        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg=self.frame_bg)
        FrameDetails.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Make details frame responsive
        FrameDetails.grid_rowconfigure(0, weight=1)
        FrameDetails.grid_columnconfigure(0, weight=1)
        
        # Create and style buttons
        button_style = {
            "font": ("Segoe UI", 11, "bold"),
            "width": 23,
            "bg": self.button_bg,
            "fg": self.button_fg,
            "bd": 0,
            "relief": FLAT,
            "activebackground": "#1565c0",
            "activeforeground": "white",
            "cursor": "hand2"
        }
        
        # Create buttons with improved styling
        btnAddData=Button(framebuttons, command=self.add_data, text="Add Data", **button_style)
        btnAddData.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        btnShowData=Button(framebuttons, command=self.showData, text="Show Data", **button_style)
        btnShowData.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        btnUpdate=Button(framebuttons, command=self.update, text="Update", **button_style)
        btnUpdate.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        btnDelete=Button(framebuttons, command=self.delete, text="Delete", **button_style)
        btnDelete.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        
        btnReset=Button(framebuttons, command=self.reset, text="Reset", **button_style)
        btnReset.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        
        btnExit=Button(framebuttons, command=self.Exit, text="Exit", **button_style)
        btnExit.grid(row=0, column=5, padx=5, pady=5, sticky="ew")
        
        # Style for labels
        label_style = {
            "font": ("Segoe UI", 11),
            "bg": self.frame_bg,
            "fg": self.text_color,
            "padx": 2,
            "pady": 6
        }
        
        # Style for entries
        entry_style = {
            "font": ("Segoe UI", 11),
            "width": 27,
            "bd": 1,
            "relief": SOLID,
            "bg": "white",
            "fg": self.text_color,
            "highlightthickness": 1,
            "highlightbackground": self.border_color,
            "highlightcolor": self.button_bg
        }
        
        # Create and style all labels and entries
        lblMember=Label(DataFrameLeft, text="Member Type", **label_style)
        lblMember.grid(row=0, column=0, sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft, font=("Segoe UI", 11), width=27, 
                             textvariable=self.member_var, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1, sticky="ew")
        
        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO.", font=("Segoe UI", 11, "bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.prn_var,width=27)
        txtPRN_NO.grid(row=1, column=1)
        
        lblFirstName = Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "First Name",padx=2, pady=6, bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.firstname_var,width=27)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName = Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Last Name",padx=2, pady=6, bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        lblLastName=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.lastname_var,width=27)
        lblLastName.grid(row=4, column=1)
        
        lblAddress1 = Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Address 1",padx=2, pady=6, bg="powder blue")
        lblAddress1.grid(row=5, column=0,sticky=W)
        lblAddress1=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.address1_var, width=27)
        lblAddress1.grid(row=5, column=1)
        
        lblAddress2= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Address 2",padx=2, pady=6, bg="powder blue")
        lblAddress2.grid(row=6, column=0,sticky=W)
        lblAddress2=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.address2_var, width=27)
        lblAddress2.grid(row=6, column=1)
        
        lblPostCode= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Pin Code ",padx=2, pady=6, bg="powder blue")
        lblPostCode.grid(row=7, column=0,sticky=W)
        lblPostCode=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"),textvariable=self.postcode_var, width=27)
        lblPostCode.grid(row=7, column=1)
        
        lblMobile= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Mobile Number ",padx=2, pady=6, bg="powder blue")
        lblMobile.grid(row=8, column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.mobile_var,width=27)
        lblMobile.grid(row=8, column=1)
        
        #-----------------------------------Column 2 Data frame left-----------------------------------------------
        
        lblBook_Id= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Book ID ",padx=2, pady=6, bg="powder blue")
        lblBook_Id.grid(row=0, column=2,sticky=W)
        lblBook_Id=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.bookid_var, width=27)
        lblBook_Id.grid(row=0, column=3)
        
        
        lblBook_Title= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Book Title ",padx=2, pady=6, bg="powder blue")
        lblBook_Title.grid(row=1, column=2,sticky=W)
        lblBook_Title=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.booktitle_var, width=27)
        lblBook_Title.grid(row=1, column=3)
        
        
        lblAuther= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "AutherName",padx=2, pady=6, bg="powder blue")
        lblAuther.grid(row=3, column=2,sticky=W)
        lblAuther=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.auther_var, width=27)
        lblAuther.grid(row=3, column=3)
        
        
        lblDateBorrowed= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Date Borrowed",padx=2, pady=6, bg="powder blue")
        lblDateBorrowed.grid(row=4, column=2,sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.borrowed_var, width=27)
        lblDateBorrowed.grid(row=4, column=3)
        
        
        lblDueDate= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Date Due",padx=2, pady=6, bg="powder blue")
        lblDueDate.grid(row=5, column=2,sticky=W)
        lblDueDate=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.duedate_var, width=27)
        lblDueDate.grid(row=5, column=3)
              
        
        lblLateReturnFine= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Late Return Fine",padx=2, pady=6, bg="powder blue")
        lblLateReturnFine.grid(row=6, column=2,sticky=W)
        lblLateReturnFine=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.latereturnfine_var, width=27)
        lblLateReturnFine.grid(row=6, column=3)
        
        
        lblDateOverDue= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Date OverDue",padx=2, pady=6, bg="powder blue")
        lblDateOverDue.grid(row=7, column=2,sticky=W)
        lblDateOverDue=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.overdue_var, width=27)
        lblDateOverDue.grid(row=7, column=3)
        
        
        lblActualPrice= Label(DataFrameLeft, font = ("Segoe UI", 11, "bold"),text = "Actual Price",padx=2, pady=6, bg="powder blue")
        lblActualPrice.grid(row=8, column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,font=("Segoe UI",11,"bold"), textvariable=self.actualprice_var, width=27)
        lblActualPrice.grid(row=8, column=3)
        
        
        #--------------------------------------Data Frame Right------------------------------------------------------
        
        self.txtBox=Text(DataFrameRight, font=("Segoe UI",12,"bold"),width=31, height=14, padx=1, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        self.listBox=Listbox(DataFrameRight, font=("Segoe UI", 11), width=18, height=13,
                       bg=self.frame_bg, fg=self.text_color, bd=1, relief=SOLID,
                       highlightthickness=1, highlightbackground=self.border_color,
                       highlightcolor=self.button_bg)
        self.listBox.bind("<<ListboxSelect>>", self.select_book)
        self.listBox.grid(row=0, column=0, padx=1, pady=6, sticky="nsew")
        
        listScrollbar.config(command=self.listBox.yview)
        
        # Add books to listbox
        listBooks = ["Clean Code: A Handbook of Agile Software Craftsmanship",
                    "Introduction to Algorithms",
                    "Structure and Interpretation of Computer Programs",
                    "The Clean Coder: A Code of Conduct for Professional Programmers",
                    "Code Complete: A Practical Handbook of Software Construction",
                    "Design Patterns: Elements of Reusable Object-Oriented Software",
                    "The Pragmatic Programmer",
                    "Head First Design Patterns: A Brain-Friendly Guide",
                    "Refactoring: Improving the Design of Existing Code",
                    "The Art of Computer Programming, Volumes 1-4",
                    "2666",
                    "All About Love",
                    "Desert Solitaire",
                    "Disgrace",
                    "Geek Love",
                    "Gilead",
                    "Giovanni's Room",
                    "A Good Man Is Hard to Find and Other Stories."]
        
        for item in listBooks:
            self.listBox.insert(END, item)
        
        # =============================================Button Frames===========================================================
        
        
        # =============================================Information Frames===========================================================
        
        # Create a container frame for the table with modern styling
        Table_frame = Frame(FrameDetails, bd=0, relief=FLAT, bg="#ffffff",
                          highlightthickness=0)
        Table_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Create a label for the table section with modern styling
        table_label = Label(Table_frame, text="LIBRARY RECORDS", 
                          font=("Segoe UI", 16, "bold"), 
                          bg="#2c3e50", fg="white", 
                          padx=15, pady=10)
        table_label.pack(fill=X)
        
        # Create a frame for the table and scrollbars with modern styling
        table_container = Frame(Table_frame, bg="#ffffff", padx=15, pady=15)
        table_container.pack(fill=BOTH, expand=True)
        
        # Configure scrollbars with modern styling
        style = ttk.Style()
        style.configure("Custom.Horizontal.TScrollbar", 
                      background="#ecf0f1",
                      troughcolor="#ffffff",
                      bordercolor="#ffffff",
                      arrowcolor="#2c3e50",
                      relief=FLAT)
        
        style.configure("Custom.Vertical.TScrollbar", 
                      background="#ecf0f1",
                      troughcolor="#ffffff",
                      bordercolor="#ffffff",
                      arrowcolor="#2c3e50",
                      relief=FLAT)
        
        xscroll = ttk.Scrollbar(table_container, orient=HORIZONTAL, style="Custom.Horizontal.TScrollbar")
        yscroll = ttk.Scrollbar(table_container, orient=VERTICAL, style="Custom.Vertical.TScrollbar")
        
        # Create the table with modern styling
        self.library_table = ttk.Treeview(table_container, 
                                        columns=("Member Type", "PRN No", "First Name", "Last Name",
                                                "Address 1", "Address 2", "Post ID", "Mobile No.", "Book Id",
                                                "Book Title", "Book Author", "Date Borrowed", "Due Date",
                                                "Late Return Fine", "Date Overdue", "Actual Price"),
                                        xscrollcommand=xscroll.set, 
                                        yscrollcommand=yscroll.set,
                                        height=15,  # Increased height
                                        style="Custom.Treeview")  # Custom style
        
        # Configure modern table style
        style.configure("Custom.Treeview",
                       background="white",
                       foreground="#2c3e50",
                       rowheight=35,  # Slightly reduced row height
                       fieldbackground="white",
                       borderwidth=1,
                       font=("Segoe UI", 11))
        
        # Enhanced header styling for maximum visibility
        style.configure("Custom.Treeview.Heading",
                      background="#f8f9fa",  # Light background
                      foreground="#000000",  # Black text
                      font=("Segoe UI", 13, "bold"),
                      padding=(15, 15),
                      relief=RAISED,
                      borderwidth=2)
        
        # Add border to headers for better visibility
        style.layout("Custom.Treeview.Heading", [
            ('Treeheading.cell', {'sticky': 'nswe'}),
            ('Treeheading.border', {'sticky': 'nswe', 'children': [
                ('Treeheading.padding', {'sticky': 'nswe', 'children': [
                    ('Treeheading.image', {'side': 'right', 'sticky': ''}),
                    ('Treeheading.text', {'sticky': 'we'})
                ]})
            ]}),
        ])
        
        # Configure selection colors
        style.map("Custom.Treeview",
                 background=[('selected', '#3498db')],
                 foreground=[('selected', 'white')])
        
        # Configure scrollbars
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        # Configure table headings and columns with modern widths
        columns = ("Member Type", "PRN No", "First Name", "Last Name",
                  "Address 1", "Address 2", "Post ID", "Mobile No.", "Book Id",
                  "Book Title", "Book Author", "Date Borrowed", "Due Date",
                  "Late Return Fine", "Date Overdue", "Actual Price")
        
        # Set column widths based on content with better visibility
        column_widths = {
            "Member Type": 130,
            "PRN No": 110,
            "First Name": 130,
            "Last Name": 130,
            "Address 1": 160,
            "Address 2": 160,
            "Post ID": 110,
            "Mobile No.": 130,
            "Book Id": 110,
            "Book Title": 220,
            "Book Author": 160,
            "Date Borrowed": 130,
            "Due Date": 130,
            "Late Return Fine": 160,
            "Date Overdue": 130,
            "Actual Price": 130
        }
        
        # Configure headings with better visibility
        for col in columns:
            self.library_table.heading(col, text=col, anchor="center")
            self.library_table.column(col, width=column_widths[col], anchor="center", minwidth=100)
            
        # Pack the table first
        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=True)
        
        # Add a separator line below headers
        separator = Frame(table_container, height=3, bg="#e0e0e0")  # Light gray separator
        separator.place(in_=self.library_table, relx=0, rely=0, relwidth=1, height=3)
        
        # Add hover effect for better interaction
        def on_enter(e):
            self.library_table['cursor'] = 'hand2'
            
        def on_leave(e):
            self.library_table['cursor'] = ''
            
        self.library_table.bind('<Enter>', on_enter)
        self.library_table.bind('<Leave>', on_leave)
        
        # Configure alternating row colors
        self.library_table.tag_configure('oddrow', background='#f8f9fa')
        self.library_table.tag_configure('evenrow', background='white')
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        
    def add_data(self):
        # Store data in memory instead of database
        data = (
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
        )
        self.library_data.append(data)
        self.fetch_data()
        messagebox.showinfo("Success","Member Has Been Added Successfully!!!")    
        
    def update(self):
        # Update data in memory
        prn = self.prn_var.get()
        for i, data in enumerate(self.library_data):
            if data[1] == prn:  # Check PRN number
                self.library_data[i] = (
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
                )
                break
        self.fetch_data()
        self.reset()
        messagebox.showinfo("Success", "Member Has Been Updated!!!")
        
    def fetch_data(self):
        # Clear existing data in table
        self.library_table.delete(*self.library_table.get_children())
        
        # Add all data from memory to table
        for data in self.library_data:
            self.library_table.insert("", END, values=data)

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
        # Delete data from memory
        prn = self.prn_var.get()
        self.library_data = [data for data in self.library_data if data[1] != prn]
        self.fetch_data()
        self.reset()
        messagebox.showinfo("Success","Member Has Been Deleted!!!")
        
    def select_book(self, event=""):
        try:
            value = str(self.listBox.get(self.listBox.curselection()))
            x = value
            if x == "Clean Code: A Handbook of Agile Software Craftsmanship":
                self.bookid_var.set("0001")
                self.booktitle_var.set("Clean Code: A Handbook of Agile Software Craftsmanship")
                self.auther_var.set("Robert Cecil Martin")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 650")
                
            elif x == "Introduction to Algorithms":
                self.bookid_var.set("0002")
                self.booktitle_var.set("Introduction to Algorithms")
                self.auther_var.set("Thomas H. Cormen")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 600")
            
            elif x == "Structure and Interpretation of Computer Programs":
                self.bookid_var.set("0003")
                self.booktitle_var.set("Structure and Interpretation of Computer Programs")
                self.auther_var.set("Gerald Jay Sussman")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 670")
                
            elif x == "The Clean Coder: A Code of Conduct for Professional Programmers":
                self.bookid_var.set("0004")
                self.booktitle_var.set("The Clean Coder: A Code of Conduct for Professional Programmers")
                self.auther_var.set("Robert Cecil Martin")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 800")
                
            elif x == "Code Complete: A Practical Handbook of Software Construction":
                self.bookid_var.set("0005")
                self.booktitle_var.set("Code Complete: A Practical Handbook of Software Construction")
                self.auther_var.set("Steven C. McConnell")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 720")
                
            elif x == "Design Patterns: Elements of Reusable Object-Oriented Software":
                self.bookid_var.set("0006")
                self.booktitle_var.set("Design Patterns: Elements of Reusable Object-Oriented Software")
                self.auther_var.set("Erich Gamma, Richard Helm")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 630")
                
            elif x == "The Pragmatic Programmer":
                self.bookid_var.set("0007")
                self.booktitle_var.set("The Pragmatic Programmer")
                self.auther_var.set("Andrew Hunt and David Thomas")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 600")
                
            elif x == "Head First Design Patterns: A Brain-Friendly Guide":
                self.bookid_var.set("0008")
                self.booktitle_var.set("Head First Design Patterns: A Brain-Friendly Guide")
                self.auther_var.set("Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 570")
                
            elif x == "Refactoring: Improving the Design of Existing Code":
                self.bookid_var.set("0009")
                self.booktitle_var.set("Refactoring: Improving the Design of Existing Code")
                self.auther_var.set("Kent Beck and Martin Fowler")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 1599")
                
            elif x == "The Art of Computer Programming, Volumes 1-4":
                self.bookid_var.set("0010")
                self.booktitle_var.set("The Art of Computer Programming, Volumes 1-4")
                self.auther_var.set("Donald Knuth")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 780")
                
            elif x == "2666":
                self.bookid_var.set("0011")
                self.booktitle_var.set("2666")
                self.auther_var.set("Roberto Bolaño")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 700")
                
            elif x == "All About Love":
                self.bookid_var.set("0012")
                self.booktitle_var.set("All About Love")
                self.auther_var.set("Bell Hooks")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 780")
                
            elif x == "Desert Solitaire":
                self.bookid_var.set("0013")
                self.booktitle_var.set("Desert Solitaire")
                self.auther_var.set("Edward Abbey")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 390")
                
            elif x == "Disgrace":
                self.bookid_var.set("0014")
                self.booktitle_var.set("Disgrace")
                self.auther_var.set("J. M. Coetzee")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 450")
                
            elif x == "Geek Love":
                self.bookid_var.set("0015")
                self.booktitle_var.set("Geek Love")
                self.auther_var.set("Katherine Dunn")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 345")
                
            elif x == "Gilead":
                self.bookid_var.set("0016")
                self.booktitle_var.set("Gilead")
                self.auther_var.set("Marilynne Robinson")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 465")
                
            elif x == "Giovanni's Room":
                self.bookid_var.set("0017")
                self.booktitle_var.set("Giovanni's Room")
                self.auther_var.set("James Baldwin")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 410")
                
            elif x == "A Good Man Is Hard to Find and Other Stories.":
                self.bookid_var.set("0018")
                self.booktitle_var.set("A Good Man Is Hard to Find and Other Stories.")
                self.auther_var.set("Mary Flannery O'Connor")
                
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.borrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.overdue_var.set("No")
                self.actualprice_var.set("Rs. 777")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error selecting book: {str(e)}")
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
