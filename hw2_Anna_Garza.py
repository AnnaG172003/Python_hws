#Single Responsibility Principle(SRP)
#Bad Case
class BookManager:
    #will add book to a catalog
    def add_book(Self,book):
        pass
    #will remove book from catalg
    def remove_book(self,book):
        pass
    #print the catalog to console
    def print_catalog(self):
        pass
    #save catalog to database
    def save_to_database(self):
        pass
#Good Case
class BookCatalog:
    def add_book(self,book):
        pass
    def remove_book(self,book):
        pass
class CatalogPrinter:
    def print(self,catalog):
        pass
class CatalogSaver:
    def save(self,catalog):
        pass
#Explanation
"""The bad case breaks the Single Responsibility Principle by mixing book management, printing,
 and saving in one class. The good case separates these into focused classes,
 each handling one task by making the design cleaner,
 easier to maintain, and true to SRP."""
#Open-Closed Principle(OCP)
#Bad Case
class Notifier:
    def notify(self, type, message):
        if type == "email":
            print(f"Email: {message}")
        elif type == "phone":
            print(f"Calling with message: {message}")
        else:
            raise Exception("Unsupported type")
#Good Case
class Notification:
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print(f"Email: {message}")

class PhoneCall(Notification):
    def send(self, message):
        print(f"Calling with message: {message}")

class Notifier:
    def notify(self, channel: Notification, message):
        channel.send(message)

#Explanation
"""In the bad case, the Notifier class violates the Open-Closed Principle by using conditional logic 
to handle different notification types, meaning that any new type that would require modifying the class itself, making it fragile 
and very hard to extend. In contrast, the good case it embrace polymorphism for each notification type 
inherits from a common Notification interface and implements its own send method.
 This allows the Notifier to remain unchanged while supporting new behaviors, 
 making the system open to extension but closed to modification, exactly what OCP encourages. """
#Liskov Substitution Principle(LSP)
#Bad Case
# It expects all characters to be able to attack
class CombatCharacter:
    def attack(self):
        pass

# Subclass-> Warrior behaves correctly
class Warrior(CombatCharacter):
    def attack(self):
        print("Warrior swings sword")

# Subclass-> Mage behaves correctly
class Mage(CombatCharacter):
    def attack(self):
        print("Mage casts lighting balls")

#subclass->Healer behaves incorrectly
class Healer(CombatCharacter):
    def attack(self):
        raise Exception("Healer can't attack")  
#Good Case
# Base class for combat roles
class CombatCharacter:
    def attack(self):
        pass

# Subclass-> Warrior behaves correctly
class Warrior(CombatCharacter):
    def attack(self):
        print("Warrior swings sword")

# Subclass-> Mage behaves correctly
class Mage(CombatCharacter):
    def attack(self):
        print("Mage casts lighting balls")

# Separate base class for support roles
class SupportCharacter:
    def heal(self):
        pass

# Subclass->Healer behaves correctly
class Healer(SupportCharacter):
    def heal(self):
        print("Healer restores health")
#Explanation
"""The bad case breaks LSP because Healer inherits from CombatCharacter but can't attack, 
violating the expectation that all subclasses can.
 The good case fixes this by separating combat and 
support roles into different base classes, 
so each subclass behaves consistently with its parent."""
#Interface Segregation Principle(ISP)
#Bad Case
class SmartDevice:
    def play_music(self):
        pass

    def navigate_gps(self):
        pass

    def take_photo(self):
        pass

class BasicMP3Player(SmartDevice):
    def play_music(self):
        print("Playing music")

    def navigate_gps(self):
        raise NotImplementedError("GPS not supported")

    def take_photo(self):
        raise NotImplementedError("Camera not supported")
#Good Case
class MusicPlayer:
    def play_music(self):
        pass

class GPSNavigator:
    def navigate_gps(self):
        pass

class Camera:
    def take_photo(self):
        pass

class BasicMP3Player(MusicPlayer):
    def play_music(self):
        print("Playing music")


#Explanation
"""The bad case violates ISP by forcing BasicMP3Player to implement GPS and 
camera methods it doesn’t support, leading to broken behavior. 
The good case splits functionality into focused interfaces like MusicPlayer, GPSNavigator, Camera, 
so each device only depends on what it actually uses keeping implementations clean and aligned with ISP.
 """
#Dependency Inversion Principle(DIP)
#Bad Case
class ConsoleRenderer:
    def render(self, message):
        print(message)

class GameEngine:
    def __init__(self):
        self.renderer = ConsoleRenderer()

    def run(self):
        self.renderer.render("Game started!")

#Good Case
class Renderer:
    def render(self, message):
        pass

class ConsoleRenderer(Renderer):
    def render(self, message):
        print(message)

class GameEngine:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def run(self):
        self.renderer.render("Game started!")

#Explanation
"""The bad case breaks DIP by tightly coupling GameEngine to a concrete ConsoleRenderer,
 making it hard to change  rendering behavior. The good case introduces an abstraction 
 (which is Renderer) that ConsoleRenderer implements, allowing GameEngine to depend on a flexible interface rather 
than a fixed implementation by making the system more modular and testable. """