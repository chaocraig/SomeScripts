<?php

# http://140.131.109.8/auto_vending/avm.php?_line=0ae5adedb3e7c3c91cf5837c1203ce5f290dda1b
#
#
#
#

define("PROD_LINES",  20);
define("KEY_PREFIX",  "CRAYCHAO");
define("KEY_POSTFIX", "0218");

function GenHashedProd() {
    $hashed_prod = array();
    for ($i=0; $i<PROD_LINES; $i++) {
	 $key = sprintf("%s%04d%s", KEY_PREFIX, $i, KEY_POSTFIX);
	 $hashed_prod[$i] = sha1($key);
    }
    return($hashed_prod);
}

function GetProdLine($hashed, $hashed_list) {

    for($i=0; $i<PROD_LINES; $i++) {
	 if ($hashed === $hashed_list[$i]) {
	      return($i);
	 }
    }
    return(-1);
}


$prod_id = array();
$list_hashed_prod = GenHashedProd();
 print_r( $list_hashed_prod );
# printf("<H2>0ae5adedb3e7c3c91cf5837c1203ce5f290dda1b = %d</H2>\n", GetProdLine("0ae5adedb3e7c3c91cf5837c1203ce5f290dda1b", $list_hashed_prod) );
$hashed_line_no = $_GET["_line"];
$line_no = GetProdLine($hashed_line_no, $list_hashed_prod);
printf("<H2>%s = %d</H2>\n", $hashed_line_no, $line_no );


$fp = stream_socket_client("tcp://localhost:6101", $errno, $errstr, 3);
if (!$fp) {
    echo "$errstr ($errno)<br />\n";
} else {
    $str_outset = sprintf("01,productoutset,A0001,123,%02d,", $line_no);
    printf("<H2>%s</H2>", $str_outset);
    fwrite($fp, $str_outset);
    $productoutset = fread($fp, 1024);
    echo "<H3> productoutset: ";
    echo "$productoutset </H3>\n";

    for ($x=1; $x<=20; $x++) { 
    	fwrite($fp, "01,productoutask,A0001,123,");
	fflush($fp);
    	$productoutask = fread($fp, 1024);
    	printf("<H3> %d - productoutask: %s </H1>", $x, $productoutask);
	$reply = explode(",", $productoutask);
	$ok = $reply[2];
	if ($ok==='ack' or $ok==='noout') exit;
	sleep(2);
    }

}


/*

[0] => 0b8a2810c04d081d1937f58080f34a5086ccff45 
[1] => 57cd90015cd37c5b46552b7a91e3041794c3a06d 
[2] => 160241fdb37d8384802832dea5cc5dc1c911e68d 
[3] => a45d082212b8e2ef80c0eb9ee3a7ec1a555344ff 
[4] => 767ce8936d44b05ab4020e90e041d5693fd0f92d 
[5] => ccd7e79177e3b7371c389df26f50cfeee4db6da6 
[6] => bb90b66f6bd691f495f357dc09516847fedbaf9e 
[7] => a1ca142dd6875a3f78b020ed529898e261bbb47c 
[8] => 9a22a7262ad465b3186c4377d49135b59eef0521 
[9] => 503df4e399fd9cb6e270821bd9013e679c915099 
[10] => 778d5e9b3e0072f5ad1b0d76c695c8eb073a2d13 
[11] => 6abc3e89fdb74191a1071a11fb5957141c040c8f 
[12] => acc95ebbc99fdda1df2508b33c569546a64b9365 
[13] => d3122c397652d1f5d0e0b96d5cea37b6b8983c57 
[14] => f23c8b61545a719f5804f7cf1228af8c3c279a7b 
[15] => a88f26fbc90b5951f9293cc9c7aa01068b6fab52 
[16] => 7c1b4f4d87a9fea3351cd24bc8e3a71eea03ef8d 
[17] => ba15ac74122eabb9bdb04563ef8a9ea18ecc2c1f 
[18] => 34ced5cec54f3f91b8edc2e329bcad018d045a73 
[19] => 52293f831341b0fabf5f1b5602dbbd8e4f7d4697

*/

?>


