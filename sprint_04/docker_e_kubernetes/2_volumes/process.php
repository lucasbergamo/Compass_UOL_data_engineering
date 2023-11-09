<?php

    $message = $_POST["message"];

    $files = scandir("./messages");
    $num_files = count($files) - 2;
    # o diretório cria 2 nomes o . e .., utilizamos o -2 para retornar o dado correto

    $fileName = "msg-{$num_files}.txt";

    $file = fopen("./messages/{$fileName}", "x");
        # fileName é o nome do arquivo e o X, indica todas permissões
    
    fwrite($file, $message);

    fclose($file);

    header("Location: index.php");