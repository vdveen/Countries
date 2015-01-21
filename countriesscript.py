#Script to generate a list of countries that are of similar size
import arcpy

arcpy.env.workspace = 'data/'

worldfile = 'data/TM_WORLD_BORDERS-0.3.dbf'
