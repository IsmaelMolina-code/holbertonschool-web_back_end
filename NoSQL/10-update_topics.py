#!/usr/bin/env python3
""" This module contains functions for updating data in the database """

def update_topics(mongo_collection, name, topics):
    """Updates a school's topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return True