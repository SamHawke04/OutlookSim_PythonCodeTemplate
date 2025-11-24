#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
### Partner B:                                                                                ###
###            <Full name as appears on Moodle>, SID<student ID>                              ###
#################################################################################################
from contextlib import nullcontext

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import *
from Confidential import *
from Personal import *
import pprint

class MailboxAgent:
    """<This is the documentation for MailboxAgent. All methods defined in this class are used to manage the mailbox containing emails represented as Mail objects.>"""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

    def getmailbox(self):
        return self._mailbox

# FEATURES A (Partner A)
    # FA.1
    # 
    def get_email(self, inputtedID):
        for e in self.getmailbox():
            #build the check id (for some reason it thinks itself is a list
            idtocheck=""
            for character in inputtedID:
                idtocheck = str(idtocheck)+str(character)
            if idtocheck == str(e.m_id):
                return e
        return False

    # FA.3
    # 
    def del_email(self, m_id):
        if not self.get_email(m_id):
            print("No email found with that ID.")
            return
        self.get_email(m_id).tag = "bin"

    # FA.4
    # 
    def filter(self, frm):
        # substring e in self.getmailbox() to grab everything before the @ using method found in personal
        # loop through mailbox
        # loop through each character to get rid of @
        # check mailbox.frm(with the @ removed) against frm

        filteredemails = []
        for e in self.getmailbox():
            for index, character in enumerate(e.frm):
                if character == "@":
                    UserID = e.frm[:index]
                    if UserID == frm:
                        filteredemails.append(e)
        return filteredemails

    # FA.5
    # 
    def sort_date(self):
        """  """
        pass


# FEATURES B (Partner B)
    # FB.1
    # 
    def show_emails(self):
        headers = ["Id", "From", "To", "Date", "Subject", "Tag", "Body"]

        # Changes the width of the column by looping through each email and finding the highest length in each attribute
        col_widths = [len(h) for h in headers]
        for mail in self.getmailbox():
            values = [mail.m_id, mail.frm, mail.to, mail.date, mail.subject, mail.tag, mail.body]
            for i, v in enumerate(values):
                col_widths[i] = max(col_widths[i], len(v))

        # Build header row (have to use join() to add the spaces)
        header_row = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))

        # Build each row, each row is a new email
        rows = []
        for mail in self.getmailbox():
            values = [mail.m_id, mail.frm, mail.to, mail.date, mail.subject, mail.tag, mail.body]
            row = " | ".join(v.ljust(col_widths[i]) for i, v in enumerate(values))
            rows.append(row)

        # Print each line separately to make output exactly like the coursework FB.1 spec photo
        print(header_row)
        for row in rows:
            print(row)
    # FB.2
    # 
    def mv_email(self, m_id, tag):
        self.get_email(m_id).tag = tag

    # FB.3
    # 
    def markFlag(self, m_id):
        self.get_email(m_id).flag = True

    def markRead(self, m_id):
        self.get_email(m_id).read = True

    # FB.4
    # 
    def find(self, date):
        # search though email_data
        # return list of Mail where Mail.date == date
        for e in self.getmailbox():
            if e.date == date:
                return e
        return False

    # FB.5
    # 
    def sort_from(self):
        """  """
        pass


# FEATURE 6 (Partners A and B)
    # 
    def add_email(self, frm, to, date, subject, tag, body):
        # code must generate unique m_id, must put the id as a string otherwise lst breaks :(
        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                newMail = Confidential(str(len(self.getmailbox())), frm, to, date, subject, tag, body)
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                newMail = Personal(str(len(self.getmailbox())), frm, to, date, subject, tag, body)
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                newMail = Mail(str(len(self.getmailbox())), frm, to, date, subject, tag, body)
        self.getmailbox().append(newMail)