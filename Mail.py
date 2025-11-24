#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from prettytable.colortable import ColorTable, Themes

class Mail:
    """ """
    # DO NOT CHANGE CLASS OR METHOD NAMES
    def  __init__(self,m_id,frm,to,date,subject,tag,body):
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # reference to Outlook mail folder email is stored in
                             # e.g. tag0 = inbox, tag1 = bin, tag2 = private, tag3 = bank_acct, tag4 = COMP1811, etc.
        self._body = body
        self._flag = False   # Boolean indicating whether email is important
        self._read = False   # Boolean indicating whether the email is read or not.

    # Format should be done from pretty print.
    def __str__(self):
        return f"m_id:{self.m_id}\tfrom:{self.frm}\t|{self.to}\t|{self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    # Pre: value in tags.
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

# FEATURES A (Partner A)
    # FA.2
    #
    def show_email(self):
        showedMail = self.get_email(self.id)
        if not showedMail:
            print("No email found with that ID.")
            input("☆ Press Enter to continue ☆")
            return
        mail_obj = showedMail[0]
        gottedEmail = ColorTable(theme=Themes.OCEAN)
        # If the email has a conf label, output this format
        # Anyhting else, output the other format under the else statement
        # Uses f"" so that it doesn't show the curly brackets
        if mail_obj.tag == "conf":
            gottedEmail.add_column("CONFIDENTIAL", ["CONFIDENTIAL"])
            gottedEmail.add_column("From", [f"{mail_obj.from_email}"])
            gottedEmail.add_column("Date", [f"{mail_obj.date}"])
            gottedEmail.add_column("Subject", [f"{mail_obj.subject}"])
            gottedEmail.add_column("Encrypted Body Text", [f"{mail_obj.body}"])
            gottedEmail.add_column("Flagged?", [f"{mail_obj.flag}"])
        else:
            gottedEmail.add_column("ID", [f"{mail_obj.id}"])
            gottedEmail.add_column("From", [f"{mail_obj.from_email}"])
            gottedEmail.add_column("To", [f"{mail_obj.to_email}"])
            gottedEmail.add_column("Date", [f"{mail_obj.date}"])
            gottedEmail.add_column("Subject", [f"{mail_obj.subject}"])
            gottedEmail.add_column("Tag", [f"{mail_obj.tag}"])
            gottedEmail.add_column("Body", [f"{mail_obj.body}"])
            gottedEmail.add_column("Flag", [f"{mail_obj.flag}"])
            gottedEmail.add_column("Read", [f"{mail_obj.read}"])
        print(gottedEmail)
        input("☆ Press Enter to continue ☆")
