<?php
if(isset($_POST['field1']) && isset($_POST['field2']) && isset($_POST['field3'])) {
    $data = '{
        "title":' + $_POST['field3'] + ' de ' + $_POST['field1'] + ',
        "date:"' + $_POST['field2']'}' + "\n";
    $ret = file_put_contents('/provas.php', $data, FILE_APPEND | LOCK_EX);
    
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}