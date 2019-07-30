<?php

/**
*
*/
namespace App\Core\Database;

use PDO;
use PDOException;
class Connection{

	public function __construct(){
		# code...
	}
	public static function make($config){
		try{  //return new PDO('mysql:host=localhost;dbname=ustora','root','');
			return new PDO(
				$config['connection'].';dbname='.$config['name'],
				$config['username'],
 				$config['password'],
 				$config['options']
			);
		}
		catch(PDOException $e){
			die($e.getMessage());
 		}
	}
}






?>
