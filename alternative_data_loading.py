
# In this script we present the alternative way we firstly used for the data loading with respect to the one showed in the notebook
# the main difference is the fact that here we collect all the data without distinction between haricot/mais and the teams

dataset_dir = os.path.join(cwd, '/content/drive/My Drive/weeds_localizator/Development_Dataset/')


# Collecting all the data and storing them in a dictionary of Images and Masks.

# we create a dictionary of 'Images' and 'Masks' as keys
files = {"Images": [], "Masks": []}
for r, d, f in os.walk(dataset_dir + 'Training/'):
    for file in f:
        # if what it finds is a .png or .jpg file, i.e. it is an image or a mask
        if('.png' in file or '.jpg' in file):

            # if it is an image we append to the Images key the path and the name of that file
            if(r.split("/")[-1] == "Images"):
                files["Images"].append({
                    "path": r,
                    "name": file
                })

            # if it is a mask we append to the Masks key the path and the name of that file
            elif(r.split("/")[-1] == "Masks"):
                files["Masks"].append({
                    "path": r,
                    "name": file
                })

# Creating a pandas dataframe with the images and their corresponding masks; absolute paths are included.
dataFrame = pd.DataFrame()
for image in files["Images"]:
    i = next((i for (i, dic) in enumerate(files["Masks"]) if dic["name"].split(".")[0] == image["name"].split(".")[0]), None)
    mask = files["Masks"][i]
    
    dataFrame = dataFrame.append({'Image': (image["path"] + "/" + image["name"]), 'Mask': (mask["path"] + "/" + mask["name"])}, ignore_index=True)

# dataFrame reshuffle
dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)

# Distributing the samples in training and validation with the following percentages:
# train_images_dataframe, train_masks_dataframe --> 90% of the samples.
# valid_images_dataframe, valid_masks_dataframe --> 10% of the samples.
train_images_dataframe = pd.DataFrame()
train_masks_dataframe = pd.DataFrame()
valid_images_dataframe = pd.DataFrame()
valid_masks_dataframe = pd.DataFrame()

for index in range(len(dataFrame.index)):
    if(index < math.floor(len(dataFrame.index) * 0.9)):
        train_images_dataframe = train_images_dataframe.append({"filename": dataFrame.iloc[index, :]["Image"]}, ignore_index=True)
        train_masks_dataframe = train_masks_dataframe.append({"filename": dataFrame.iloc[index, :]["Mask"]}, ignore_index=True)
    else:
        valid_images_dataframe = valid_images_dataframe.append({"filename": dataFrame.iloc[index, :]["Image"]}, ignore_index=True)
        valid_masks_dataframe = valid_masks_dataframe.append({"filename": dataFrame.iloc[index, :]["Mask"]}, ignore_index=True)