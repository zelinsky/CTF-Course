function login(){
    var user = document.getElementById("user").value;
    var pass = document.getElementById("pass").value;
    if ( user == "admin" && pass == "youcantguessme"){
	alert ("UDCTF{d0nT_put_p4assw0rds_in_th3_s0urc3}");
	return false;
    }
    else{
	alert("Login failed!");
	return false;
    }
}
