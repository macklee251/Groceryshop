from datetime import datetime, date
class Categoria:
    def __init__(self, name:str, description:str) -> None:
        self.name = name 
        self.description = description
        
    def __str__(self) -> str:
        return f'name: {self.name} - description: {self.description}'