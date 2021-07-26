import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailHandler:
    """Handle sending email containing all the matched jobs title and link"""

    def __init__(self, subject, jobs, sender_email, receiver_email, password):
        self.subject = subject
        self.jobs = jobs
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password
    
    def create_text(self):
        text = "Here are your new job postings:\n"
        for job in self.jobs:
            text += f"{job['title']} {job['url']}\n"

        return text

    def create_html(self):
        rows = ''
        for job in self.jobs:
            link = f"<a href='{job['url']}'>{job['title']}</a>"
            rows += f"<tr><td>{link}</td><td>{job['source']}</td></tr>"
        html = f"""\
        <html>
        <body>
            <h1>Here are your new job postings:</h1>
            <table>
                <tr>
                    <th>Title</th>
                    <th>Source</th>
                </tr>
                {rows}
            </table>
        </body>
        </html>
        """
        return html

    def send_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(self.create_text(), "plain")
        part2 = MIMEText(self.create_html(), "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string()
            )