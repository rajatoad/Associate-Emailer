from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str


@dataclass
class Sender(Contact):
    pass
    
@dataclass
class Receiver(Contact):
    pass
