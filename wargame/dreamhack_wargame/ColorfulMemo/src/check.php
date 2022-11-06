<?php
if($_SERVER["REMOTE_ADDR"] == '127.0.0.1' || $_SERVER["REMOTE_ADDR"] == '::1'){
    $id = $_GET['id'];
    $mysqli = new mysqli('localhost','user','password','colorfulmemo');
    // I believe admin
    // 로컬 서버로만 접근해야 하기 때문에 submit.php -> bot.py 를 통해 접근해야함

    $result = $mysqli->query('SELECT adminCheck FROM memo WHERE id = '.$id);  //객체지향 mysqli db 쿼리 수행
    if($result){
        $row = mysqli_fetch_row($result); //숫자 인덱스 배열을 반환
        if($row){

            if($row[0] != 1){       //memo 테이블의 adminCheck 열인 id 값이 1이 아니라면 값을 1로 바꿔줌 
                $stmt = $mysqli->prepare('UPDATE memo SET adminCheck = 1 WHERE id = ?');
                $stmt->bind_param('i',$id);     //id 값을 int형으로 바인딩 해주기 때문에 injection 불가
                $stmt->execute();
                $stmt->close();
            }
        }
    }
}
else{
    die("no hack");
}
?>