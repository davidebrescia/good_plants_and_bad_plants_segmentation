# Bad weeds localizator

We have topview pictures (RGB) of a cultivation, like the one on the left. We want to develop a software that segmentates the image in three classes, as shown in the figure on the right:

![weeds](https://user-images.githubusercontent.com/92381157/137196796-8c3d8cc2-aeb1-4f98-aa57-00a6876899d8.png)

The three classes are:  
White = crop = good plants   
Red = weeds = bad plants   
Black = background  

This might be useful for an hypothetical smart machine, so it can recognize the bad plants to remove. 

For details, please look at "Report.pdf". For the dataset, contact me.

## Results
Maximum achieved meanIoU (Intersection of Union) = 47.6%
