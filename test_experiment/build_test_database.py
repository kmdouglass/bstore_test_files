# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:50:05 2016

@author: douglass
"""
import bstore.database as db
import bstore.config as cfg
from pathlib import Path
from bsplugins.leb import MMParser

cfg.__Registered_DatasetTypes__ = ['Localizations', 'WidefieldImage', 'LocMetadata']

directory = Path('./')

parser = MMParser()
filenameStrings = {
    'Localizations'  : '_locResults.dat',
    'LocMetadata'    : '_locMetadata.json',
    'WidefieldImage' : 'WF*ome.tif'}

with db.HDFDatastore('test_experiment_db.h5') as myDS:
    myDS.build(parser, directory, filenameStrings, readTiffTags = True)
