let enter = document.getElementById('enter')


enter.addEventListener('click', (e)=>{
  console.log("Ding");
  var sound = new Audio('../sound/sound.mp3');
  if(sound === true);
    sound.play();
})
