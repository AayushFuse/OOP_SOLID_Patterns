"""
[Singleton Design Pattern] Implement a configuration manager using the Singleton Design Pattern. 
The configuration manager should read configuration settings from a file and provide access to these settings throughout the application. 
Demonstrate how the Singleton Design Pattern ensures that there is only one instance of the configuration manager, 
preventing unnecessary multiple reads of the configuration file.
"""
import json


class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType,cls).__call__(*args,**kwds)
        
        return cls._instances[cls]
    
    

class ConfigurationManager(metaclass=SingletonType):
    
    def __init__(self) -> None:
        with open('config.json','r') as f:
            self.__config = json.load(f)
    
    def get_config(self):
        return self.__config    

if __name__ == '__main__':
    conf1 = ConfigurationManager()
    conf2 = ConfigurationManager()
    
    print(conf1.get_config())
    
    
    
    