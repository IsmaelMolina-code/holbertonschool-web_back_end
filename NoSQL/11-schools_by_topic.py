#!/usr/bin/env python3
""" This module contains functions for updating data in the database  """


def schools_by_topic(mongo_collection, topic):
    """ Function that returns the list of school having a specific topic """
    return mongo_collection.find({"topics": topic})
