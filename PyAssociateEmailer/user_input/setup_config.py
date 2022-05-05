import os
import configparser


class Contacts():
    def get_associates():
        associates = []
        parser = configparser.ConfigParser()
        with open(os.path.join("conf/", 'associate_info.cfg')) as cfg_file:
            parser.readfp(cfg_file)

        for section in parser.sections():
            name = ""
            email = ""
            for option, value in parser.items(section):
                if option == "name":
                    name = value 
                elif option == "email":
                    email = value
            associates.append((name, email))
        
        return associates

    def get_trainer():
        parser = configparser.ConfigParser()
        with open(os.path.join("conf/",'trainer_info.cfg')) as cfg_file:
            parser.readfp(cfg_file)

        for section in parser.sections():
            name = ""
            email = ""
            for option, value in parser.items(section):
                if option == "name":
                    name = value 
                elif option == "email":
                    email = value
        return (name, email)


class TechStackCfg():
    def get_tech_stack():
        parser = configparser.ConfigParser()
        with open(os.path.join("conf/",'tech_stack_info.cfg')) as cfg_file:
            parser.readfp(cfg_file)
        
        for section in parser.sections():
            name = ""
            length = 0
            start = ""
            repo = ""
            class_link = ""
            zoom = ""
            slack = ""
            survey = ""

            for option, value in parser.items(section):
                if option == "name":
                    name = value
                elif option == "length":
                    length = value
                elif option == "start":
                    start = value
                elif option == "repo":
                    repo = value
                elif option == "class":
                    class_link = value
                elif option == "zoom":
                    zoom = value
                elif option == "slack":
                    slack = value
                elif option == "survey":
                    survey = value
            return {
                "name": name,
                "length": length,
                "start": start,
                "repo": repo,
                "class": class_link,
                "zoom": zoom,
                "slack": slack,
                "survey": survey
            }
