# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:50:05 2016

@author: douglass
"""
import bstore.parsers  as pr
import bstore.database as db
from pathlib import Path

directory = Path('./')
myDS      = db.HDFDatabase('test_experiment_db.h5')

parser = pr.MMParser()
filenameStrings = {
    'Localizations'  : '_locResults.dat',
    'LocMetadata'    : '_locMetadata.json',
    'WidefieldImage' : 'WF*ome.tif'}
myDS.build(parser, directory, filenameStrings, readTiffTags = True)