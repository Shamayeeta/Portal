
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from django.contrib import messages
import json
from tensorflow import Graph
from django.contrib.auth.decorators import login_required

# Create your views here.


img_height, img_width=256,256

  
# JSON string:
# Multi-line string
x = r"""{"0" : "Bacterial Pneumonia", "1" : "COVID", "2" : "Normal", "3" : "Tuberculosis", "4" : "Viral Pneumonia"}"""
labelInfo = json.loads(x)

model_graph = Graph()

@login_required(login_url='/')
def scanxray(request):
    context={'a':1}
    return render(request,'scanxray/scanxrayindex.html',context)

@login_required(login_url='/')
def predictImage(request):
    import os
    import numpy as np
    fileObj=request.FILES['filePath']
    try:
        fs=FileSystemStorage()
        filePathName=fs.save(fileObj.name,fileObj)
        filePathName1=fs.url(filePathName)
        cwd= os.getcwd()
        source = os.path.join(cwd,filePathName1[1:])
        destination = os.path.join(cwd,'media',request.user.username,'databasexray',filePathName)
        os.renames(source,destination)
        img = tf.keras.preprocessing.image.load_img(destination, target_size=(256,256))
    
        with model_graph.as_default():
            tf_session = tf.compat.v1.Session()
            with tf_session.as_default():
                img = tf.keras.preprocessing.image.load_img(destination, target_size=(256, 256))
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                img_array = tf.expand_dims(img_array, 0) 
                model = tf.keras.models.load_model("./models/XrayClassificationModel.h5")
                predi=model.predict(img_array,steps=1)

        print(np.argmax(predi[0]))
        predictedLabel=labelInfo[str(np.argmax(predi[0]))]
        predictedlabel = ""
        predictedLabel=labelInfo[str(np.argmax(predi[0]))]
        if len(predictedLabel.split())>1:
            for i in predictedLabel.split():
                predictedlabel+=i

        destination1 = destination.split('.')[0]
        destination2 = destination.split('.')[-1]
        finalimgpath = destination1 + '-' +predictedlabel +'.'+destination2
        os.rename(destination,finalimgpath)
        imgsrc = './media/'+request.user.username+'/databasexray/'+filePathName.split('.')[0] +'-' +predictedlabel +'.'+destination2
    

        context={'filePathName1':filePathName1,'predictedLabel':predictedLabel, 'imgsrc':imgsrc}
        return render(request,'scanxray/predictxray.html',context) 
    except FileExistsError:
        context={'a':1}
        messages.success(request,f"This file already exists in your database")
        return render(request,'scanxray/scanxrayindex.html',context)

    except :
        context={'a':1}
        messages.success(request,f"Please upload a file of valid format(such as .jpg,.png,etc")
        return render(request,'scanxray/scanxrayindex.html',context)

@login_required(login_url='/')
def viewDataBase(request):
    import os
    username = request.user.username
    try:    
        listOfImages=os.listdir('./media/'+username+'/databasexray')  
        print("length",len(listOfImages))
        if len(listOfImages):  
            listOfImagesPath=['./media/'+username+'/databasexray/'+ i for i in listOfImages]            
            context={'listOfImagesPath':listOfImagesPath}
            return render(request,'scanxray/viewDBxray.html',context)
        else:
            return render(request,'database/dbempty.html')
    except:
        print("dbempty")
        return render(request,'database/dbempty.html')
     
