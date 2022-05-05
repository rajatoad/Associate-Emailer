from models.technology import TechStack
from models.users import Receiver, Sender
from dataclasses import dataclass

@dataclass
class BaseEmail:
    sender: Sender
    receiver: Receiver
    technology: TechStack

    def setup_email_body(self) -> str:
        return f"""<p>Hello {self.receiver.name},</p>
        
<p>I’d like to introduce myself, my name is {self.sender.name}, and I will be your trainer and manager for the next {self.technology.length} weeks with the {self.technology.name} track.
You are set to begin on the {self.technology.start_date}, but before that it is required for you to have these essentials before beginning:</p>

<ul>
    <li>Business Formal / Casual</li>
    <ul>
        <li>On Mondays it is required to wear business formal even though we are in remote work</li>
        <li>This is more essential to meeting with your eventual employers as they will require a dress code too</li>
    </ul>
    <li>Programming Environment setup</li>
    <ul>
        <li>The pace of the programming is fast so it is essential for you to have the essentials prepared before you start training</li>
        <li>Here are the requirements and a guide to help you get it all started before you start training</li>
        <li><a href="{self.technology.repo_link}"> Github Repo </a></li>
        <li>All the coding examples will be done within Visual Studio Code and pushed to this repository</li>
        <li>You will see the first day training study guide, so if you want to start early then you are welcome too</li>
        <li>All the examples and study guides will be pushed to this repository</li>
    </ul>
    <li>GitHub Account</li>
    <ul>
        <li>If you have not got a GitHub account then it is required you get it ASAP</li>
    </ul>
    <li>Web Camera & Microphone</li>
    <ul>
        <li>This should have already been told to you, but a web camera and microphone is needed during your training</li>
    </ul>
    <li>Windows Device</li>
    <ul>
        <li>If you are not using a windows device then you will have to do a lot of self-learning on your own OS</li>
        <li>Any others will be told to you by HR before you begin training</li>
    </ul>
</ul>
<p>The goal is to begin training right away, the more prepared you are, the easier it will all be.
Your first assignment is a starter course on Git, join the link below and add yourself to the Git Classroom under your name:</p>
<ul>
    <li><a href="{self.technology.classroom_link}"> Git Classroom First Assignment </a></li>
</ul>
<p>Here is the zoom link to where your trainings will be, please arrive on the {self.technology.start_date} for 10:00 AM EST:
<ul>
    <li><a href="{self.technology.zoom_link}"> Zoom Meeting Room </a></li>
</ul>
</p>
<p>Here is the Slack for where any announcements or links will be provided outside of your meetings:</p>
<ul>
    <li><a href="{self.technology.slack_link}"> Slack </a></li>
    <li>Slack will exclusively be for announcements and notices, not for discussions</li>
</ul>
<p>Finally, a survey for me to get to know you:</p>
<ul>
    <li><a href="{self.technology.survey_link}"> Survey </a></li>
</ul>

<p>You will be placed into teams on your first day, and it is highly recommended you create a Discord or personal slack to communicate with each other.
If you need to reach out to me, I am available during trainings, email, or you can schedule a 1-on-1 with me which will be explained on your first day how.</p>

<p>Your schedule will be provided on the first day too.</p>

<br>
<div>
<p>Here are the links altogether, incase you may have missed one: </p>
<ul>
    <li><a href="{self.technology.repo_link}">Github Repo</a></li>
    <li><a href="{self.technology.classroom_link}">Git Classroom First Assignment</a></li>
    <li><a href="{self.technology.zoom_link}">Zoom Meeting Room</a></li>
    <li><a href="{self.technology.slack_link}">Slack</a></li>
    <li><a href="{self.technology.survey_link}">Survey</a></li>
</ul>
</div>

<br>
<p>Good Luck!</p>
<p>{self.sender.name}</p></div>
"""

    def setup_email_head(self) -> str:
        return f"""From: From Person <{self.sender.email}>
To: To Person <{self.receiver.email}>
MIME-Version: 1.0
Content-type: text/html
Subject: Welcome to Revature and your Training
"""
    def setup_email_total(self, head, body) -> str:
        return head + body