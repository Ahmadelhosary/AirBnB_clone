#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "/home/vagrant/AirBnB_clone/file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[class_name] = obj
    
    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)
    
    def reload(self):
        if os.path.exists(FileStorage.__file_path) and os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)

