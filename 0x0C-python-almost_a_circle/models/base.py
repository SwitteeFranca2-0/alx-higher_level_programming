#!/usr/bin/python3
"""This module contains a base class for all future classes in this project"""
import json
import csv


class Base:
    """This class declares a base"""
    ___nb_objects = 0

    def __init__(self, id=None):
        """This function initialises the class"""
        if id is not None:
            self.id = id
        else:
            type(self).___nb_objects += 1
            self.id = self.___nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns the json string of the argument"""
        if list_dictionaries is None:
            return("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This is a class mtehod that saves a json string to a file"""
        if list_objs is None:
            return ("[]")
        f = cls.__name__ + ".json"
        with open(f, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_o = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_o))

    @staticmethod
    def from_json_string(json_string):
        """This function converts json strings to dictionaries"""
        if json_string is None:
            return ("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This module returns an instance wiith all attr. already set"""
        if cls.__name__ == 'Rectangle':
            new_o = cls(1, 1)
        else:
            new_o = cls(1)
        new_o.update(**dictionary)
        return new_o

    @classmethod
    def load_from_file(cls):
        """loads sbclasss from file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                return [cls.create(**dic) for dic in
                        Base.from_json_string(f.read())]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This saves the arg to a csv file"""
        filename = cls.__name__ + ".csv"
        list_o = [o.to_dictionary() for o in list_objs]
        with open(filename, 'w', encoding="utf-8") as f:
            c = csv.writer(f)
            if cls.__name__ == 'Rectangle':
                for o in list_o:
                    c.writerow([o['id'], o['width'],
                                o['height'], o['x'], o['y']])
            if cls.__name__ == 'Square':
                for o in list_o:
                    c.writerow([o['id'], o['size'], o['x'], o['y']])

    @classmethod
    def load_from_file_csv(cls):
        """This function loads from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                rec = []
                for row in f:
                    if cls.__name__ == 'Rectangle':
                        c_r = row.split(",")
                        rec.append({
                            'id': int(c_r[0]),
                            'width': int(c_r[1]),
                            'height': int(c_r[2]),
                            'x': int(c_r[3]),
                            'y': int(c_r[4])
                        })
                    if cls.__name__ == 'Square':
                        c_r = row.split(",")
                        rec.append({
                            'id': int(c_r[0]),
                            'size': int(c_r[1]),
                            'x': int(c_r[2]),
                            'y': int(c_r[3])
                        })
                return [cls.create(**dic) for dic in rec]
        except IOError:
            return []
