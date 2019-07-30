<?php
namespace App\Core\Database;

use PDO;

class QueryBuilder{

	protected $pdo;

	function __construct(PDO $pdo){
		$this->pdo = $pdo;
	}
	public function select_all($table){
		$statement =$this->pdo->prepare('select * from '.$table);
			$statement->execute();
			return $statement->fetchAll(PDO::FETCH_OBJ);
		}
	

	public function get_all_type(){
		$sql = "SELECT DISTINCT type FROM product";
		$statement =$this->pdo->prepare($sql);
		$statement->execute();
		return $statement->fetchAll(PDO::FETCH_OBJ);
	}

	public function add_new_product($pname,$type,$pack,$c_id,$sh_id){
		$pname = ucwords($pname);
		$type = ucwords($type);
		$sql = "
		INSERT INTO `product`(`pname`, `type`, `pack`, `c_id`, `sh_id`) 
		VALUES 
		("."'"."$pname"."'".","."'"."$type"."'".",".""."$pack"."
		".",".""."$c_id"."".",".""."$sh_id"."".")";
		$this->pdo->query($sql);
	}//strtoupper()

	public function add_new_company($cname){
		$cname = strtoupper($cname);
		$sql = "INSERT INTO `company`(`cname`) VALUES ("."'"."$cname"."')";
		$this->pdo->query($sql);
	}
	public function view_products(){
		$sql = "select p.p_id,p.pname,p.type,p.pack,c.cname,s.shelf 
		from product p  ,company c , shelf s 
		where 
		p.c_id=c.c_id 
		and 
		p.sh_id=s.sh_id";
		$statement =$this->pdo->prepare($sql);
		$statement->execute();
		return $statement->fetchAll(PDO::FETCH_OBJ);
		}
}
	
?>
