from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
import face_recognition
from .models import *

class FaceIdAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, face_id=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if check_password(password,user.password):
                if self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
                    return user                                                                                   
                                                                                    
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

    def check_face_id(self, face_id=None, uploaded_face_id=None):
        known_image= face_recognition.load_image_file(face_id)
        unknown_image = face_recognition.load_image_file(uploaded_face_id)
    
        face_locations = face_recognition.face_locations(known_image,model="cnn")
        unknown_face_locations = face_recognition.face_locations(unknown_image,model="cnn")

        known_encoding = face_recognition.face_encodings(known_image,known_face_locations=face_locations)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image,known_face_locations=unknown_face_locations)[0]

        results = face_recognition.compare_faces([known_encoding], unknown_encoding)

        if results[0]==True:
            return True
        
        return False