#!/usr/bin/python3
"""Initialize models directory"""
from models.engine.file_storage import CustomFileStorage


custom_storage =CustomFileStorage()
custom_storage.reload()
