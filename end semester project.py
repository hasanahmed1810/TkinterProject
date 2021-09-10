import tkinter # enables tkinter
from tkinter import messagebox #enables the use of messageboxes

window1 = tkinter.Tk()
window1.title("Easy Mail")
window1.geometry("500x900")

#Label at the top that is 2 columns long
FillLabel = tkinter.Label(window1, text=" Fill in your details", width=25, font=("Times New Roman", 14))
FillLabel.grid(row=0,column=0, columnspan=3)

#A label for sender's Name
s_nameLabel = tkinter.Label(window1, text="Sender's Name *", width=25)
s_nameLabel.grid(row=1, column=0, pady=10)

#An entry box for the sender's Name
s_name = tkinter.Entry(window1)
s_name.grid(row=1, column=1, sticky="W")

#Label for sender's phone number
phonenumLabel = tkinter.Label(window1, text="Sender' Phone Number *", width=25)
phonenumLabel.grid(row=2, column=0, pady=10)

#Entry box for sender's phone number
phonenum = tkinter.Entry(window1)
phonenum.grid(row=2, column=1, sticky="W")

#A label for receiver's Name
r_nameLabel = tkinter.Label(window1, text="Receiver's Name *", width=25)
r_nameLabel.grid(row=3, column=0, pady=10)

#An entry box for the receiver's Name
r_name = tkinter.Entry(window1)
r_name.grid(row=3, column=1, sticky="W")

#Label for receiver's Last Name       
r_titleLabel = tkinter.Label(window1, text="Receiver's Title*", width=25)
r_titleLabel.grid(row=4, column=0, pady=10)

#Entry box for receiver's Last Name
r_title = tkinter.Entry(window1)
r_title.grid(row=4, column=1, sticky="W")

#Label for Sender's Email Address
s_emailLabel = tkinter.Label(window1, text="Sender's Email Address *", width=25)
s_emailLabel.grid(row=5, column=0, pady=10)

#Entry box for Sender's Email Address
s_email = tkinter.Entry(window1)
s_email.grid(row=5, column=1, sticky="W")

#Label for password
PasswordLabel = tkinter.Label(window1, text="Password *", width=25)
PasswordLabel.grid(row=6,column=0,pady=10)

#encripted entry box for password
PassWord = tkinter.Entry(window1, show="*")#each letter is replaced is a *
PassWord.grid(row=6,column=1,sticky="W")

#Label for Receiver's Email Address
r_emailLabel = tkinter.Label(window1, text="Receiver's Email Address*", width=25)
r_emailLabel.grid(row=7, column=0, pady=10)

#entry box for Receiver's Email Address
r_email = tkinter.Entry(window1)
r_email.grid(row=7, column=1)

#label for Qualifications
qualLabel = tkinter.Label(window1, text="Qualifications *", width=25)
qualLabel.grid(row=9, column=0, pady=10)#pady is used to give space above and below the label

#entry box for Qualifications
qual = tkinter.Entry(window1)
qual.grid(row=9, column=1)

Example2 = tkinter.Label(window1, text="(Example: BSc,MSc,PHD)")
Example2.grid(row=9,column=2)

#label for subject
subjectLabel = tkinter.Label(window1, text="Enter your Subject *", width=25)
subjectLabel.grid(row=8, column=0, pady=10)

#entry box for subject
subj = tkinter.Entry(window1)
subj.grid(row=8, column=1, sticky="W")

#label for major
MajorLabel = tkinter.Label(window1, text="Major *", width=25)
MajorLabel.grid(row=10,column=0,pady=10)

#entry box to enter major
Major = tkinter.Entry(window1)
Major.grid(row=10,column=1,sticky="W")

Example = tkinter.Label(window1, text="(Example: Engineering,Accounting)")
Example.grid(row=10,column=2)

#label for university
uniLabel = tkinter.Label(window1, text="University *", width=25)
uniLabel.grid(row=11,column=0,pady=10)

#entry box to enter university
uni = tkinter.Entry(window1)
uni.grid(row=11,column=1,sticky="W")

#label for uni year
yearLabel = tkinter.Label(window1, text="Year In University *", width=25)
yearLabel.grid(row=11, column=2, pady=10)

#drop down box for uni year
year = {"first year": 0,
          "second year": 1,
          "third year":2,
          "forth year":3}

years = tkinter.StringVar()
years.set("Year")
Dropdownyear = tkinter.OptionMenu(window1, years, *year.keys())
Dropdownyear.config(takefocus=1)
Dropdownyear.grid(row=12, column=2)

#label for gpa
gpaLabel = tkinter.Label(window1, text="GPA *", width=25)
gpaLabel.grid(row=12,column=0,pady=10)

#entry box to enter gpa
gpa = tkinter.Entry(window1)
gpa.grid(row=12,column=1,sticky="W")

#label for skills
skillsLabel = tkinter.Label(window1, text="Skills *", width=25)
skillsLabel.grid(row=13,column=0,pady=10)

#entry box to enter skills
skills = tkinter.Entry(window1)
skills.grid(row=13,column=1,sticky="W")

#label for positive positive attribute
attriLabel = tkinter.Label(window1, text="Positive Attributes *", width=25)
attriLabel.grid(row=13, column=2, pady=10)

#drop down box for positive attribute
attri = {"hard working":0,
         "result oriented":1,
         "detail oriented":2,
         "team oriented":3,
         "enthusiastic":4,
         "efficient":5,
         "ambitious":6,
         "articulate":7,
         "productive":8,
         "autonomous":9,
         "organized":10,
         "neurotic":11}

attris = tkinter.StringVar()
attris.set("Attribute")
Dropdownattri = tkinter.OptionMenu(window1, attris, *attri.keys())
Dropdownattri.config(takefocus=1)
Dropdownattri.grid(row=14, column=2)

#label for position
posLabel = tkinter.Label(window1, text="Position You Are applying For *", width=25)
posLabel.grid(row=14,column=0,pady=10)

#entry box to enter position
pos = tkinter.Entry(window1)
pos.grid(row=14,column=1,sticky="W")

#label for templates
templateLabel = tkinter.Label(window1, text="Choose your Template *", width=25)
templateLabel.grid(row=15, column=0, pady=10)

#drop down box for templates
template = {"Job": 0,
          "Internship": 1}

templates = tkinter.StringVar()
templates.set("Template")
Dropdowntemplates = tkinter.OptionMenu(window1, templates, *template.keys())
Dropdowntemplates.config(takefocus=1)
Dropdowntemplates.grid(row=15, column=1)

#label for media of info
infoLabel = tkinter.Label(window1, text="Media Of Info *", width=25)
infoLabel.grid(row=7, column=2, pady=10)

#drop down box for media of info
info = {"news paper":0,
        "website":1,
        "seminar":2,
        "social media":3,
        "word of mouth":4}       
infos = tkinter.StringVar()
infos.set("Media")
Dropdowninfo = tkinter.OptionMenu(window1, infos, *info.keys())
Dropdowninfo.config(takefocus=1)
Dropdowninfo.grid(row=8, column=2)


#cancel button to close the window1
cancelButton = tkinter.Button(window1, text="Cancel", command=window1.destroy)
cancelButton.grid(row=16,column=0,pady=20)

#new function for window2
def create_window():
    if templates.get()=="Job":
        mailbody="""Dear {} {},

My name is {}. I am grateful for the opportunity to apply for the vacant {} role in your company. The job description alludes that you want to hire a versatile candidate who can handle multiple aspects of this role. Based on my experience, I am certain that I would perform excellently in this role.

I have a degree of {} with a GPA of {} from {}. My colleagues have consistently classified me as a {} person. During my career I have developed proven skills such as {} and I hope to leverage these skills at your company.

I hope that I am the resourceful, qualified candidate you are looking for. I look forward to elaborating how my diverse skillset and abilities will benefit your organization. Please contact me at {} or by email to schedule a meeting.

I appreciate you considering my application and look forward to further correspondence from you.

Yours sincerely,

{}
""".format(r_title.get(),r_name.get(),s_name.get(),pos.get(),qual.get(),gpa.get(),uni.get(),attris.get(),skills.get(),phonenum.get(),s_name.get())

    if templates.get()=="Internship":
        mailbody="""Dear {} {},

I am writing about the {} role that you advertised recently. I came across the job posting through a {} and I am delighted that my academic achievements meet all the necessary requirements. I am looking for a challenging but rewarding internship and I was drawn to this exciting opportunity.

As a {} student in {} at {}, I have acquired skills in {}. I currently have a CGPA of {}.

I would like to avail the opportunity to meet you personally. Do not hesitate to contact me as soon as possible. Thank you for your time and your consideration.

Yours sincerely,

{}
""".format(r_title.get(),r_name.get(),pos.get(),infos.get(),years.get(),Major.get(),uni.get(),skills.get(),gpa.get(),s_name.get())
    if templates.get()=="Template":
        mailbody="No template chosen"

    #algorithm for mailing
    def mailer():
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            sen_email=s_email.get()
            password=PassWord.get()
            rec_email=r_email.get()
            subject=subj.get()
            message=mailbody

            msg=MIMEMultipart()
            msg['From']=sen_email
            msg['To']=rec_email
            msg['Subject']=subject
            msg.attach(MIMEText(message,'plain'))

            server=smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sen_email,password)
            server.send_message(msg)
            server.quit()
            tkinter.messagebox.showinfo("","Mail sent")
        except:
            tkinter.messagebox.showinfo("","Mail not sent")
    
    window2 = tkinter.Tk()
    window2.title("Your Info")
    window2.geometry("1010x450")

    #label for details
    detailLabel = tkinter.Label(window2,text="Mailing Details",font=("Times New Roman",14))
    detailLabel.grid(row=0,column=0,columnspan=2)
    detailLabel.configure(anchor="center")#anchor is used to place it in the centre of the 2 columns

    #this displays the subject of the email
    subjlabel = tkinter.Label(window2,text="Subject: "+subj.get(),width=45)
    subjlabel.grid(row=2,column=1)

    #this displays the Sender's Email Address entered by the user in the form  
    EmailA = tkinter.Label(window2, text="Sender's Email Address: " + s_email.get(), width=45)
    EmailA.grid(row=3,column=1)

    #this displays the Receiver's Email Address entered by the user in the form
    EmailB = tkinter.Label(window2, text="Receivers's Email Address: " + r_email.get(), width=45)
    EmailB.grid(row=4,column=1)

    #this displays the template chosen by the user
    temp = tkinter.Label(window2, text="Template chosen: " + templates.get(), width=45)
    temp.grid(row=5,column=1)

    #this displays the mailbody
    mbody = tkinter.Message(window2, text="The mail body: " +'\n'+mailbody, width=1000)
    mbody.grid(row=6,column=1)

    #cancel button to close the window2
    cancelButton2 = tkinter.Button(window2, text="Cancel", command=window2.destroy)
    cancelButton2.grid(row=8,column=1,pady=5)

    #function to display message box to confirm that the mail is sent
    def sendmail():
        mailer()
        window2.destroy()#used to close window2

    #button to send an email
    sendbutton = tkinter.Button(window2,text="Send",command=sendmail)
    sendbutton.grid(row=7,column=1,)           

    window2.mainloop()

#to check if all fields are filled in
def confirm():
    if len(s_name.get())==0 or len(r_name.get())==0 or len(r_title.get())==0 or len(phonenum.get())==0 or len(uni.get())==0 or len(skills.get())==0 or len(Major.get())==0 or len(gpa.get())==0 or len(qual.get())==0 or len(pos.get())==0 or len(r_email.get())==0 or len(s_email.get())==0 or len(subj.get())==0 or len(PassWord.get())==0 or attris.get()=='Attribute' or templates.get()=='Template' or years.get()=='Year' or infos.get()=='Media':
        tkinter.messagebox.showinfo("","Please fill in all the fields")
    else:
        create_window()        
    
#button to open a new window
confirmbutton = tkinter.Button(window1, text="Confirm", command=confirm)
confirmbutton.grid(row=16,column=1,pady=20)


window1.mainloop()
