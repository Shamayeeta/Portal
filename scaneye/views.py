from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from django.contrib import messages
import json
from tensorflow import Graph
from django.contrib.auth.decorators import login_required
import os
import numpy as np

# Create your views here.

img_height, img_width=250,250
  
# list of classes
labelInfo = {"0" : "Age-Related Macular Degeneration", "1" : "Cataract", "2" : "Glaucoma", "3" : "Pathological Myopia", "4" : "Normal"}

model_graph = Graph()

@login_required(login_url='/')
def scaneye(request):
    context={'a':1}
    return render(request,'scaneye/scaneyeindex.html',context)

@login_required(login_url='/')
def predictImage(request):
    fileObj=request.FILES['filePath']
    try:
        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        filePathName1=fs.url(filePathName)
        cwd= os.getcwd()
        source = os.path.join(cwd,filePathName1[1:])
        destination = os.path.join(cwd,'media',request.user.username,'databaseeye',filePathName)
        imgsrc = './media/'+request.user.username+'/databaseeye/'+filePathName
        os.renames(source,destination)
        
        #loads and processes image
        with model_graph.as_default():
            tf_session = tf.compat.v1.Session()
            with tf_session.as_default():
                img = tf.keras.preprocessing.image.load_img(destination, target_size=(256, 256))
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                img_array = tf.expand_dims(img_array, 0) 
                model = tf.keras.models.load_model("./models/eyescanclassificationmodel.h5")
                #predicts the probability of the image being in different classes
                predi=model.predict(img_array,steps=1)

        predictedLabel=labelInfo[str(np.argmax(predi[0]))]
        predictedlabel=predictedLabel

        #ensures that there are no spaces in the predicted label which is appended to the file name
        if len(predictedLabel.split())>1:
            predictedlabel = ""
            for i in predictedLabel.split():
                predictedlabel+=i          

        #renames the file to include the predicted label and saves it 
        destination1 = destination.split('.')[0]
        destination2 = destination.split('.')[-1]
        finalimgpath = destination1 + '-' +predictedlabel +'.'+destination2
        os.rename(destination,finalimgpath)
        imgsrc = './media/'+request.user.username+'/databaseeye/'+filePathName.split('.')[0] +'-' +predictedlabel +'.'+destination2

        context={'filePathName1':filePathName1,'predictedLabel':predictedLabel, 'imgsrc':imgsrc}
        return render(request,'scaneye/predicteyescan.html',context)
         
    except FileExistsError:
        context={'a':1}
        messages.warning(request,f"This file already exists in your database")
        return render(request,'scaneye/scaneyeindex.html',context)

    except:
        context={'a':1}
        os.remove(destination)
        messages.warning(request,f"Please upload a file of valid format(such as .jpg,.png,etc)")
        return render(request,'scaneye/scaneyeindex.html',context)

@login_required(login_url='/')
def viewDataBase(request):
    username = request.user.username
    try:    
        listOfImages=os.listdir('./media/'+username+'/databaseeye')  
        if len(listOfImages):  
            listOfImagesPath=['./media/'+username+'/databaseeye/'+ i for i in listOfImages]            
            context={'listOfImagesPath':listOfImagesPath}
            return render(request,'scaneye/viewDBeye.html',context)
        else:
            return render(request,'database/dbempty.html')
    except:
        return render(request,'database/dbempty.html')