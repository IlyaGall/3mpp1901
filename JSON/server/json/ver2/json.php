<?php
// на какие данные рассчитан этот скрипт
header("Content-Type: application/json");
// 1. Получаем данные от страницы
$data = json_decode(file_get_contents("php://input"));
if (empty($data)) {
    // пустой запрос означает, что юзер попросил отарвить ему данные для посмотра, код аналогичен ниже, за исключением, что ничего не добовляем
    $filename = 'data.json';
    // 3. Если есть — запоминаем его содержимое, а если такого файла нет — создаём его отдельной командой.
    if (file_exists($filename)) {
        // Если файл есть — открываем его и читаем данные
        $file = file_get_contents('data.json');
        // Если такого файла нет…
    } else {
    // …то создаём его сами
        $file = fopen("data.json", "a+");
    }
    echo $file;
    unset($file);
    return;
} 
else{

    // 2. Проверяем, есть ли на сервере нужный нам файл с данными — json.data.
    // Берём новую переменную и пишем в неё имя файла
    $filename = 'data.json';
    $flag=false;
    // 3. Если есть — запоминаем его содержимое, а если такого файла нет — создаём его отдельной командой.
    if (file_exists($filename)) {
        // Если файл есть — открываем его и читаем данные
        $file = file_get_contents('data.json');
        // Если такого файла нет…
    } else {
    // …то создаём его сами
        $file = fopen("data.json", "a+");
        $flag=true;
    }
    // 4/ Всё, что было в этом файле, переводим в массив, с которым умеет работать PHP. Таким способом у нас каждая JSON-запись будет храниться в отдельной ячейке массива.
   
   $oldJson= (string) $file;
    //$datas=(file_get_contents("php://input"));
   $newJson= (string) (file_get_contents("php://input"));
    
   $gluingOldAndNew="";
//    echo $oldJson;
//    return;
  if($flag){
    $gluingOldAndNew="{$newJson}";
    $flag=false;
  }else{
     $gluingOldAndNew="{$oldJson},{$newJson}";
  }
   //$gluingOldAndNew = str_replace('"', '\'', $gluingOldAndNew); // надо менять с двойных кавычек на одинарные, иначе начинает чудить
   //file_put_contents('data.json', json_encode($gluingOldAndNew,  JSON_UNESCAPED_UNICODE));
   
   echo json_encode($gluingOldAndNew,  JSON_UNESCAPED_UNICODE);
   
 

   file_put_contents('data.json', json_encode(str_replace('"', '', $gluingOldAndNew),  JSON_UNESCAPED_UNICODE));

   // $fullJsonFile=json_encode($gluingOldAndNew, JSON_UNESCAPED_UNICODE);
  // file_put_contents('data.json',$gluingOldAndNew);

    // 6. Записываем это всё обратно в файл и тут же читаем обратно из него — так мы убедимся, что запись прошла нормально и мы можем с этим работать.
    // Записываем данные в файл…
   // $gluingOldAndNew = str_replace('"', '\'', $gluingOldAndNew); // надо менять с двойных кавычек на одинарные, иначе начинает чудить
   // file_put_contents('data.json', json_encode($gluingOldAndNew,  JSON_UNESCAPED_UNICODE)); //JSON_UNESCAPED_UNICODE без него великий и могучий превращаеться в цифры

    // …и сразу считываем их обратно
   // $file = file_get_contents('data.json'); // Открыть файл data.json
    // 7. Отправляем всё содержимое файла на страницу, чтобы там увидеть, что сервер работает как нужно.
    echo $file;
    // Освобождаем память от переменных, которые нам пока не нужны
    unset($file);
   // unset($taskList);
}