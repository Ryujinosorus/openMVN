#!/usr/bin/python3

import argparse
import os

from utils import *

def main(args):
    if not args.output[-1]=='/':
         args.output+= "/"

    os.makedirs(args.output, exist_ok = True)

    focal = args.focal
    if focal is None:
        print("Auto calc focal not implement yet")
        exit()
    
    ImageListing(args.input,args.output,focal)
    ComputeFeatures(args.output)
    ComputeMatches(args.output)
    IncrementalSFM(args.output)
    ComputeSFMDataColor(args.output)
    ComputeStructureFromKnownPoses(args.output)
    openMVG2openMVS(args.output)
    DensifyPointCloud(args.output)
    ReconstructMesh(args.output)
    RefineMesh(args.output)
    TextureMesh(args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Anonymise la video')
    parser.add_argument('-i', '--input', type=str,required=False, default="data/input/monstree/",help="Path to the input picture")
    parser.add_argument('-o', '--output', type=str,required=False, default="data/output", help="Output path")
    parser.add_argument('-f', '--focal', type=str,required=False, help="Output path")
    main(parser.parse_args())
