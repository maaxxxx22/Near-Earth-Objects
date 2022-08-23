"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`."""


import csv
import json
import os

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    neos_lst_total=[*csv.DictReader(open(neo_csv_path))]
    neos_lst = []
    for i in neos_lst_total:
        neos_lst.append(NearEarthObject(i["pdes"], i["name"], i["diameter"],i["pha"]))
    
    """Return a colection of Near Earth Objects in a list"""
    return neos_lst




def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    with open(cad_json_path) as d:
        cad_lst_total = json.load(d)
        cad_lst = []
        data_list = cad_lst_total["data"]
    
     
    for i in data_list:
        cad_lst.append(CloseApproach(i[0], i[3], i[4], i[7]))
        
    """Return a colection of close approach objects in a list"""
    return cad_lst


