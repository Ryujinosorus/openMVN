#!/usr/bin/python3

import os 

def ImageListing(input,output,focal):
    os.system(f"openMVG_main_SfMInit_ImageListing -i {input} -o {output} -f {focal}")

def ComputeFeatures(output):
    os.system(f"openMVG_main_ComputeFeatures -i {output}sfm_data.json -o {output}")

def ComputeMatches(output):
    os.system(f"openMVG_main_ComputeMatches -i {output}sfm_data.json -o {output}")

def IncrementalSFM(output):
    os.system(f"openMVG_main_IncrementalSfM -i {output}sfm_data.json -m {output} -o {output} ")

def ComputeSFMDataColor(output):
    os.system(f"openMVG_main_ComputeSfM_DataColor  -i {output}sfm_data.bin -o {output}colored.ply ")

def ComputeStructureFromKnownPoses(output):
    os.system(f"openMVG_main_ComputeStructureFromKnownPoses -i {output}sfm_data.bin -m {output} -o {output}robust.bin -f {output}matches.f.bin ")

def openMVG2openMVS(output):
    os.system(f"openMVG_main_openMVG2openMVS -i {output}robust.bin -d {output} -o {output}scene.mvs")

def DensifyPointCloud(output):
    os.system(f"src/openMVS_build/bin/DensifyPointCloud {output}scene.mvs -o {output} ")

def ReconstructMesh(output):
    os.system(f"src/openMVS_build/bin/ReconstructMesh --max-threads=0 {output}scene_dense.mvs ")

def RefineMesh(output):
    os.system(f"src/openMVS_build/bin/RefineMesh {output}scene_dense_mesh.mvs")

def TextureMesh(output):
    os.system(f"src/openMVS_build/bin/TextureMesh {output}scene_dense_mesh_refine.mvs")