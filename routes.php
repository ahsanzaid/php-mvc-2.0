<?php



$router->get('mvc/Product','ProductController@Index');



$router->post('mvc/productsubmit','DistributorController@SaveProduct');



$router->get('mvc/distributor','DistributorController@Index');



$router->post('mvc/productSubmit','ProductController@SubmitProduct');


$router->get('mvc','PageController@Index');

