#!/usr/bin/env python3
"""This module contains functions for inserting data into the database"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a school into the database"""
    mongo_collection.insert_one(kwargs)
    return (kwargs.get(u'_id'))