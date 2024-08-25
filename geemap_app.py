import geemap.foliumap as geemap 
import ee

ee.Initialize()

Map = geemap.Map()

Map.to_streamlit(width=1000)
