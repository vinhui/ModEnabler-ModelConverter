from pyassimp import *
from meshSerialization import *
from datetime import datetime
import sys
import os

optimize = False
calculateNormals = False

def parseArgs():
	global optimize
	global calculateNormals

	for index, arg in enumerate(sys.argv):
		if index == 0:
			continue

		if arg == "-calculateNormals":
			calculateNormals = True
		elif os.path.isfile(arg):
			parseFile(arg)
		else:
			print("Argument '" + arg + "' is not valid")
		pass

def parseFile(file):
	print("Loading file '" + file + "'")
	scene = load(file, postprocess.aiProcess_Triangulate)

	if len(scene.meshes) > 0:
		for i, mesh in enumerate(scene.meshes):
			global optimize, calculateNormals

			print("Serializing '" + mesh.name + "'")
			startTime = datetime.now()

			f = open(parseName(file, mesh.name), 'wb')
			serialize(f, mesh, optimize, calculateNormals)
			f.close()
		
			delta = datetime.now() - startTime
			print("Converting mesh is done, it took " + str(delta.microseconds / 1000) + "ms")
	else:
		print("There don't seem to be any meshes in this file")

def parseName(baseFile, meshName):
	return os.path.splitext(baseFile)[0] + "-" + meshName + ".mesh"

print("Starting program")

parseArgs()
print("Finished")