# Mod Enabler - Model Converter

This program let's you convert most popular model formats to the Mod Enabler format. This is done with the help of [AssImp](http://www.assimp.org/).
Bindposes and bone weights are not (yet) supported. The exported files will be saved to the same folder as the source file. You can supply multiple files as arguments. You can use the `-optimize` argument to let it run [Mesh.Optimize](https://docs.unity3d.com/ScriptReference/Mesh.Optimize.html) the unity optimizer on import. Use `-calculateNormals` argument to run [Mesh.RecalculateNormals](https://docs.unity3d.com/ScriptReference/Mesh.RecalculateNormals.html) on import. 
It's best to do these arguments before the files since otherwise the files before won't be affected. Example: `python Model_Converter.py -optimize file.blend file2.obj`
