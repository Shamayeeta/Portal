const constraints = {
    video: true
  };
  
const captureVideoButton =
    document.querySelector('#video-button');
    
captureVideoButton.onclick = function() {
    captureVideoButton.setAttribute('style','display: none;');
    loginButton.removeAttribute("style");
    navigator.mediaDevices.getUserMedia(constraints).
    then(handleSuccess).catch(handleError);
    };
