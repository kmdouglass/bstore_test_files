# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:50:05 2016

@author: douglass
"""
import bstore.parsers  as pr
import bstore.database as db
from pathlib import Path

directory = Path('./')
parser    = pr.MMParser(readTiffTags = True)
myDB      = db.HDFDatabase('test_experiment_db.h5')
myDB.build(parser, directory)