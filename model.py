class Categoria:
    def __init__(self, name:str, description:str) -> None:
        self._name = name 
        self._description = description

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name:str) -> None:
        if isinstance(new_name, str):
            self._name = new_name
            
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, new_description:str) -> None:
        if isinstance(new_description, str):
            self._description = new_description