function enterApp(){
  window.location.href = "main.html";
}

function cleanSystem(){
  const tempDir = document.getElementById('tempDir').value;
  eel.clean_system(tempDir)(function(status){
    document.getElementById('status').innerText = status;
  });
}