<?php
if(isset($_POST['submit'])) {
	$name = $_POST['name'];
	$mailFrom = $_POST['email'];
	$subject = $_POST['subject'];
	$message = $_POST['message'];

	$to = 'desmond.lee@baruchmail.cuny.edu';
	$mailHeaders = "From: " . $name . "<". $mailFrom .">\r\n";
    
	
    mail($to, $subject, $message, $mailHeaders);
}
?>