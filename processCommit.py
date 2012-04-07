import smtplib, subprocess, sys
import email.utils
from email.mime.text import MIMEText

repo = sys.argv[1]
rev = sys.argv[2]
repository = 'This_is_the_name_in_the_email'
sender = 'subversion@emailserver.com'                     # Change to any email address
receivers = ['recp1@your.com', 'recp2@your.com']          # List of email recipients

# Get subversion information
# 'svnlook changed' returns what files / paths have changed
# 'svnlook info' returns author, date/time, log message
cmd = 'c:\\program files\\Path to SVN\\bin\\svnlook changed %s -r %s' % (repo, rev)
changed = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
cmd = 'c:\\program files\\Path to SVN\\bin\\svnlook info %s -r %s' % (repo, rev)

commitMsg = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
message = """A commit has been made to the %s repository
*** Commit Information ***
""" % (repository)

message = message + commitMsg.decode('utf-8') + '\n*** Changed Files ****\n\n' + changed.decode('utf-8')
msg = MIMEText(message)
msg['To'] = ', '.join(receivers)          # Generate string containing recpts. comma separated.
msg['From'] = email.utils.formataddr(('Subversion', 'subversion@emailserver.com'))
msg['Subject'] = 'Subversion Commit | %s' % (repository)

try:
    session=smtplib.SMTP('SMTPSERVER')      # Your SMTP Server
    session.sendmail(sender, receivers, msg.as_string())
    print('Notification of commit sent')
except SMTPException:
    print('Unable to send notification')
