#**********************************************************************
#Finds the 100 best features in an image, and tracks these
#features to the next image.  Saves the feature
#locations (before and after tracking) to text files and to PPM files, 
#and prints the features to the screen.
#**********************************************************************

#include "pnmio.h"
from klt import *
from PIL import Image
from selectGoodFeatures import *
from writeFeatures import *

if __name__=="__main__":

	tc = KLT_TrackingContext()
	nFeatures = 100
	
	KLTPrintTrackingContext(tc)

	img1 = Image.open("img0.pgm")
	img2 = Image.open("img1.pgm")
	ncols, nrows = img1.size

	fl = KLTSelectGoodFeatures(tc, img1, nFeatures)

	print "\nIn first image:"
	for i, feat in enumerate(fl):
		print "Feature #{0}:  ({1},{2}) with value of {3}".format(i, feat.x, feat.y, feat.val)
  
	KLTWriteFeatureListToPPM(fl, img1, "feat1.ppm")
	#KLTWriteFeatureList(fl, "feat1.txt", "%3d")

	#KLTTrackFeatures(tc, img1, img2, ncols, nrows, fl)

	#printf("\nIn second image:\n");
	#for (i = 0 ; i < fl->nFeatures ; i++)
	#	printf("Feature #%d:  (%f,%f) with value of %d\n",
	#	i, fl->feature[i]->x, fl->feature[i]->y,
	#	fl->feature[i]->val)

	#KLTWriteFeatureListToPPM(fl, img2, ncols, nrows, "feat2.ppm")
	#KLTWriteFeatureList(fl, "feat2.fl", NULL)      # binary file 
	#KLTWriteFeatureList(fl, "feat2.txt", "%5.1f")  # text file   




