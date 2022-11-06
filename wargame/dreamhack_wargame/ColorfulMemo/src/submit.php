<?php
$id = $_GET['id'];
if(ctype_digit($id)){ //숫자일 시 true
    exec("python3 /bot.py ".$id);   //id값을 인자값으로 넘겨주며 python실행
}

else{
    die("no hack");
}
die('<script> location.href="/" </script>');
?>

