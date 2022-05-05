# Python Associate Emailer

A Python script that automates the process of sending out emails to associates. The automation uses the outlook app so it will need to be downloaded. This automation also assumes you are using a windows device, I have not tested in anything else.
The only setup needed is to prepare the config files located inside the projects /conf/ directory. Include within it the needed information in the format below.

Before you begin, make sure to create a new virtual environment either manually or with `virtualenv` within the python folder.

```
pip install virtualenv
virtualenv .venv
source .venv/Scripts/activate
```

Then go to where the requirments.txt file is and run the following to get the needed packages

```
pip install -r requirements.txt
```

Now you are ready to run, but make sure you setup the config files to your needs. Then run

```
python main.py
```

And it will start.


### Trainer Information

```
[Trainer]
name=John Doe
email=johndoe@email.com
```
Don't include quotes and don't change the key values.

### Tech Stack Information

```
[Tech Stack]
name=TechStack
length=99
start=1/1/1111
repo=link
class=link
zoom=link
slack=link
survey=link
```
This is up to you, change it depending on the template you want to use in your emails. In my case I provide them with all of these in that welcome email. If you do not want to then you will need to change it in the `email_setup/base_email.py` file to reflect what you want.


### Associate Information

```
[associate 1]
name=Jane Doe
email=jane.doe@email.com
[associate 2]
name=Johnny Does
email=johnny.does@email.com
```

Each associate needs its own section ([associate 1]) and the name, email keys are essential. Make sure you use valid emails too!